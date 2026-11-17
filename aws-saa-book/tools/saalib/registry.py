"""Registry: `registry build|set|check|show|wave-args` and `coverage` (TOOLS.md section 4).

The registry is data/book.json (seed: _build/registry/book.seed.json). `registry build` also parses the
saved exam guide pages into _build/registry/exam-guide.json and services.json. Standard library only.

Python API for other modules: exam_guide(), services(), service_keys_in_scope().
Paths are read as common.X at call time, so a sandbox (--book-dir) or a test patch takes effect.
"""
from __future__ import annotations

import contextlib
import copy
import json
import os
import re
import urllib.parse
from pathlib import Path

from saalib import common, schemas

SEED_KEYS = ("id", "slug", "title", "part", "tier", "kind", "xl", "wave", "services")
SOURCE_LISTS = ("guides", "pages", "faq", "history", "quotas", "pricing", "whatsnew_tags", "case_tags")
URL_LISTS = ("guides", "pages", "faq", "history", "quotas", "pricing")
PATCH_KEYS = ("sources", "tasks", "bullets", "service_map", "cards", "notes")
NOTES_MAX_CHARS = 2000      # `notes` is a planning note for chapter agents (for example the frequency note), never evidence
DEFAULT_GUIDE = {"root": "https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-associate-03/",
                 "guide_id": "aws-certification-solutions-architect-associate-03"}
# Execution order of the stages (TOOLS.md 3.1: verify-questions runs before review).
STAGE_ORDER = ("plan", "mine", "register", "verify-facts", "brief", "prose", "questions", "tasks", "cards", "speak",
               "diagrams", "edit", "verify-questions", "review", "fix", "finalize")
MAX_TEXT_LINES = 40

_RE_DOMAIN_H1 = re.compile(r"^#\s+Content Domain (\d+):\s*(.+?)\s*$")
_RE_TASK = re.compile(r"^##\s+Task(?: Statement)? (\d+)\.(\d+):\s*(.+?)\s*$")
_RE_WEIGHT = re.compile(r"Content Domain (\d+): (.+?) \((\d+)% of scored content\)")
_RE_HEADING = re.compile(r"^#{1,6}\s")
_RE_IN_SCOPE = re.compile(r"(?i)^#\s+in[- ]scope\b")
_RE_OUT_SCOPE = re.compile(r"(?i)^#\s+out[- ]of[- ]scope\b")
_RE_SHORT = re.compile(r"\(([^()]+)\)\s*$")
_RE_PARENS = re.compile(r"\s*\([^()]*\)")
_RE_BRAND = re.compile(r"^(?:Amazon|AWS)\s+")
_MARKERS = ("+ ", "- ", "* ")


# ---------------------------------------------------------------- paths and small helpers

def _book_path() -> Path:
    return common.DATA / "book.json"


def _seed_path() -> Path:
    return common.REGISTRY / "book.seed.json"


def _guide_path() -> Path:
    return common.REGISTRY / "exam-guide.json"


def _services_path() -> Path:
    return common.REGISTRY / "services.json"


def _spec() -> dict:
    return common.read_json(common.STYLE_DIR / "SPEC.json", {}) or {}


def _corpus():
    try:
        from saalib import corpus
        return corpus
    except Exception:
        return None


def _book_rel(path) -> str:
    try:
        return str(Path(path).resolve().relative_to(Path(common.BOOK).resolve()))
    except ValueError:
        return str(path)


def _finding(code, msg, file=None, line=None, item=None) -> dict:
    return {"code": code, "file": file, "line": line, "item": item, "msg": msg}


def _finding_text(f: dict) -> str:
    if f.get("file"):
        where = f["file"] + (f":{f['line']}" if f.get("line") else "")
    else:
        where = f.get("item") or "registry"
    named = f" [{f['item']}]" if f.get("file") and f.get("item") else ""    # which bullet, service or chapter
    return f"{where}: {f['code']} {f['msg']}{named}"


def _out(args, obj, lines) -> None:
    """--json: the object. Text: a one-line summary, then at most 40 lines."""
    if getattr(args, "json", False):
        common.emit(obj, args)
        return
    lines = list(lines)
    extra = len(lines) - 1 - MAX_TEXT_LINES
    if extra > 0:
        lines = lines[:1 + MAX_TEXT_LINES] + [f"... ({extra} more; use --json --out FILE)"]
    common.emit("\n".join(lines), args)


@contextlib.contextmanager
def _locks(*paths):
    """Take several file locks in path order (TOOLS.md section 0, rule 4)."""
    with contextlib.ExitStack() as stack:
        for path in sorted({str(p) for p in paths}):
            stack.enter_context(common.file_lock(Path(path)))
        yield


def _find_chapter(book: dict, ch_id: str):
    ch_id = str(ch_id)
    for ch in book.get("chapters", []):
        if ch_id in (ch["id"], ch["slug"], f"{ch['id']}-{ch['slug']}"):
            return ch
    return None


def _chapter_keys(book: dict) -> dict:
    """service key -> the first chapter that has it."""
    keys = {}
    for ch in book.get("chapters", []):
        for key in ch.get("services", []):
            keys.setdefault(key, ch)
    return keys


def _dedupe(items) -> list:
    seen, out = set(), []
    for item in items:
        if item not in seen:
            seen.add(item)
            out.append(item)
    return out


# ---------------------------------------------------------------- Python API (TOOLS.md section 2)

def exam_guide():
    """The parsed exam guide (_build/registry/exam-guide.json), or None before `registry build`."""
    return common.read_json(_guide_path())


def services():
    """The parsed service lists (_build/registry/services.json), or None before `registry build`."""
    return common.read_json(_services_path())


def service_keys_in_scope() -> set:
    """Every registry service key that an in-scope entry maps to."""
    doc = services() or {}
    return {key for entry in doc.get("in_scope", []) for key in entry.get("keys", [])}


# ---------------------------------------------------------------- templates and ledger (read-only)

def _merge(base, over):
    if isinstance(base, dict) and isinstance(over, dict):
        out = dict(base)
        for key, value in over.items():
            out[key] = _merge(base[key], value) if key in base else copy.deepcopy(value)
        return out
    return copy.deepcopy(over)


def _template_key(ch: dict, spec: dict) -> str:
    override = (spec.get("chapter_overrides") or {}).get(ch["id"]) or {}
    return override.get("template") or ch.get("kind") or ch.get("tier")


def _template(ch: dict, spec: dict) -> dict:
    """The resolved template: lint.template(ch) when lint is there, else the same resolution rule."""
    try:
        from saalib import lint
        resolved = lint.template(ch["id"])
        if isinstance(resolved, dict) and resolved.get("key"):
            return resolved
    except (Exception, SystemExit):
        pass
    key = _template_key(ch, spec)
    override = dict((spec.get("chapter_overrides") or {}).get(ch["id"]) or {})
    override.pop("template", None)
    resolved = _merge((spec.get("templates") or {}).get(key) or {}, override)
    resolved["key"] = key
    return resolved


def _num(value) -> int:
    if isinstance(value, bool):
        return 0
    if isinstance(value, int):
        return value
    if isinstance(value, dict):
        return _num(value.get("max", 0))
    return 0


def _plan_counts(ch: dict, template: dict) -> dict:
    counts = template.get("counts") or {}
    questions = counts.get("questions") or {}
    cards = counts.get("cards") or {}
    tasks = counts.get("tasks") or {}
    card_total = _num(cards.get("core")) + _num(cards.get("extended"))
    card_total += _num(cards.get("extended_per_service")) * len(ch.get("services", []))
    return {
        "questions_write": _num(questions.get("write")),
        "questions_ship": _num(questions.get("shipped")),
        "speak": _num((counts.get("speak") or {}).get("count")),
        "cards": card_total,
        "tasks_max": sum(_num(tasks.get(kind)) for kind in ("look", "try", "lab")),
    }


def _ledger(ch_id: str) -> dict:
    return common.read_json(common.LEDGER / "chapters" / f"{ch_id}.json", {}) or {}


def _next_stage(ch: dict, ledger: dict, plan: dict):
    try:
        from saalib import ledger as ledger_mod
        fn = getattr(ledger_mod, "next_stage", None)
        if callable(fn):
            value = fn(ch["id"])
            if value is None or isinstance(value, str):
                return value
    except (Exception, SystemExit):
        pass
    skip = set()
    if plan["questions_ship"] == 0:
        skip |= {"questions", "verify-questions"}
    if plan["tasks_max"] == 0:
        skip.add("tasks")
    if plan["cards"] == 0:
        skip.add("cards")
    if plan["speak"] == 0:
        skip.add("speak")
    stages = ledger.get("stages") or {}
    for stage in STAGE_ORDER:
        status = (stages.get(stage) or {}).get("status")
        if status in ("pass", "na") or (status is None and stage in skip):
            continue
        return stage
    return None


# ---------------------------------------------------------------- exam guide parser (4.1 step 3)

def page_role(text: str) -> str:
    """Role from the first `# ` line: domain, in-scope, out-of-scope, or other."""
    first = next((line for line in text.splitlines() if line.startswith("# ")), "")
    if _RE_DOMAIN_H1.match(first):
        return "domain"
    if _RE_IN_SCOPE.match(first):
        return "in-scope"
    if _RE_OUT_SCOPE.match(first):
        return "out-of-scope"
    return "other"


def _parse_domain(lines, source_id, tasks, bullets) -> None:
    task = None
    kind = None
    started = False
    counters = {}
    seen_tasks = {t["id"] for t in tasks}
    for number, line in enumerate(lines, 1):
        if _RE_HEADING.match(line):
            kind = None
            match = _RE_TASK.match(line)
            if match:
                task = f"{match.group(1)}.{match.group(2)}"
                if task not in seen_tasks:
                    seen_tasks.add(task)
                    tasks.append({"id": task, "domain": int(match.group(1)), "title": match.group(3),
                                  "source_id": source_id, "line": number})
            elif line.startswith(("# ", "## ")):
                task = None
            continue
        label = line.strip().strip("*").strip()
        if label in ("Knowledge of:", "Skills in:"):
            kind = "knowledge" if label.startswith("K") else "skill"
            started = False
            continue
        if not kind or not task:
            continue
        if line.startswith(_MARKERS):
            started = True
            letter = "K" if kind == "knowledge" else "S"
            n = counters[(task, letter)] = counters.get((task, letter), 0) + 1
            bullets.append({"id": f"{task}.{letter}{n}", "task": task, "domain": int(task.split(".")[0]), "kind": kind,
                            "n": n, "text": line[2:].strip(), "source_id": source_id, "line": number})
        elif not line.strip():
            if started:
                kind = None
        elif not line.startswith((" ", "\t")):
            kind = None


def _parse_services(lines, source_id) -> list:
    raw = []
    category = None
    for number, line in enumerate(lines, 1):
        if _RE_HEADING.match(line):
            if line.startswith("## "):
                category = line[3:].strip()
            elif line.startswith("# "):
                category = None
            continue
        if category and line.startswith(_MARKERS):
            name = line[2:].strip()
            if name:
                raw.append({"official_name": name, "category": category, "source_id": source_id, "line": number})
    return raw


def parse_pages(pages) -> dict:
    """Parse saved exam guide pages. `pages`: [{"source_id", "url", "sha256", "text"}].

    Returns {"pages", "domains", "tasks", "bullets", "in_scope_raw", "out_of_scope_raw", "problems"}.
    """
    titles, weights = {}, {}
    tasks, bullets, in_raw, out_raw, rows = [], [], [], [], []
    for page in pages:
        lines = page["text"].splitlines()
        sid = page["source_id"]
        role = page_role(page["text"])
        has_weight = False
        for line in lines:
            for match in _RE_WEIGHT.finditer(line):
                has_weight = True
                weights.setdefault(int(match.group(1)), {"weight": int(match.group(3)), "title": match.group(2),
                                                         "source_id": sid})
        if role == "domain":
            first = next(line for line in lines if line.startswith("# "))
            match = _RE_DOMAIN_H1.match(first)
            titles.setdefault(int(match.group(1)), {"title": match.group(2), "source_id": sid})
            _parse_domain(lines, sid, tasks, bullets)
        elif role == "in-scope":
            in_raw += _parse_services(lines, sid)
        elif role == "out-of-scope":
            out_raw += _parse_services(lines, sid)
        elif has_weight:
            role = "overview"
        rows.append({"source_id": sid, "url": page["url"], "sha256": page["sha256"], "role": role})
    domains, problems = [], []
    for n in sorted(set(titles) | set(weights)):
        title = (titles.get(n) or weights.get(n))["title"]
        source = (titles.get(n) or weights.get(n))["source_id"]
        if n not in weights:
            problems.append(f"domain {n} has no weight")
            continue
        domains.append({"id": n, "title": title, "weight": weights[n]["weight"], "source_id": source})
    if len(domains) != 4:
        problems.append(f"expected exactly 4 domains with a weight, found {len(domains)}")
    total = sum(d["weight"] for d in domains)
    if total != 100:
        problems.append(f"the domain weights add up to {total}, not 100")
    return {"pages": rows, "domains": domains, "tasks": tasks, "bullets": bullets,
            "in_scope_raw": in_raw, "out_of_scope_raw": out_raw, "problems": problems}


# ---------------------------------------------------------------- service keys (4.1 step 4)

def short_name_of(official_name: str):
    match = _RE_SHORT.search(official_name)
    return match.group(1).strip() if match else None


def auto_slugs(official_name: str, short_name=None) -> list:
    """The automatic match candidates: the name without brand and parentheses, then the short name."""
    out = []
    for name in (_RE_PARENS.sub("", official_name), short_name or ""):
        slug = common.slugify(_RE_BRAND.sub("", name.strip()))
        if slug and slug not in out:
            out.append(slug)
    return out


def keys_for(official_name: str, short_name, book: dict, chapter_keys=None) -> list:
    chapter_keys = _chapter_keys(book) if chapter_keys is None else chapter_keys
    mapped = (book.get("service_map") or {}).get(official_name)
    if mapped is not None:
        return _dedupe(mapped)
    for slug in auto_slugs(official_name, short_name):
        if slug in chapter_keys:
            return [slug]
    return []


def _home(keys, chapter_keys):
    """(home chapter id, level) of the first key that a chapter has."""
    for key in keys[:1]:
        ch = chapter_keys.get(key)
        if ch:
            return ch["id"], (ch["tier"] if ch["tier"] != "mock" else None)
    return None, None


def _has_home(keys, chapter_keys) -> bool:
    return any(key in chapter_keys for key in keys)


def _entries(raw, book, in_scope: bool) -> list:
    chapter_keys = _chapter_keys(book)
    merged = {}
    for row in raw:
        entry = merged.get(row["official_name"])
        if entry:
            if row["category"] not in entry["categories"]:
                entry["categories"].append(row["category"])
            continue
        short = short_name_of(row["official_name"])
        merged[row["official_name"]] = {
            "id": common.slugify(row["official_name"]), "official_name": row["official_name"], "short_name": short,
            "categories": [row["category"]], "keys": [], "home_chapter": None, "level": None,
            "source_id": row["source_id"], "line": row["line"]}
    entries = list(merged.values())
    if in_scope:
        for entry in entries:
            _set_keys(entry, book, chapter_keys)
    return entries


def _set_keys(entry, book, chapter_keys) -> None:
    entry["keys"] = keys_for(entry["official_name"], entry.get("short_name"), book, chapter_keys)
    entry["home_chapter"], entry["level"] = _home(entry["keys"], chapter_keys)


def _unmapped(in_scope, chapter_keys) -> list:
    return [e["official_name"] for e in in_scope if not _has_home(e["keys"], chapter_keys)]


# ---------------------------------------------------------------- registry build

def _merge_book(seed, current, spec) -> dict:
    """4.1 step 1: seed-owned keys from the seed, tool-owned keys kept, defaults added."""
    if current is None:
        book = copy.deepcopy(seed)
    elif seed is None:
        book = copy.deepcopy(current)
    else:
        old = {ch["id"]: ch for ch in current.get("chapters", [])}
        chapters = []
        for seed_ch in seed["chapters"]:
            ch = {k: copy.deepcopy(v) for k, v in seed_ch.items()}
            for key, value in (old.get(seed_ch["id"]) or {}).items():
                if key not in SEED_KEYS and key not in seed_ch:
                    ch[key] = value
            chapters.append(ch)
        meta = dict(current.get("book") or {})
        meta.update(copy.deepcopy(seed.get("book") or {}))
        book = {"book": meta, "parts": copy.deepcopy(seed["parts"]), "chapters": chapters,
                "service_map": current.get("service_map") or {}}
    for ch in book["chapters"]:
        ch.setdefault("tasks", [])
        ch.setdefault("bullets", [])
        sources = ch.setdefault("sources", {})
        for name in SOURCE_LISTS:
            sources.setdefault(name, [])
    meta = book.setdefault("book", {})
    meta.setdefault("fact_namespaces", {"exam": "01"})
    if spec.get("version"):
        meta["style_version"] = str(spec["version"])
    meta.setdefault("exam_guide", dict(DEFAULT_GUIDE))
    book.setdefault("service_map", {})
    return book


def _snapshot(source_id: str):
    """(text, meta, sha256 of the .txt) of a snapshot, or (None, None, None)."""
    if not source_id or ".." in source_id.split("/"):
        return None, None, None
    base = common.CORPUS / "snap"
    txt = base / (source_id + ".txt")
    if not txt.exists():
        return None, None, None
    meta = common.read_json(base / (source_id + ".meta.json"), {}) or {}
    return txt.read_text(encoding="utf-8"), meta, common.sha256_file(txt)


def _fetch_code(exc) -> int:
    names = {cls.__name__ for cls in type(exc).__mro__}
    if "PolicyError" in names:
        return common.EXIT_POLICY
    if "TransientError" in names:
        return common.EXIT_TRANSIENT
    return common.EXIT_PRECONDITION


def _load_pages(index: dict, offline: bool):
    """Returns (pages, None) or (None, (exit code, message))."""
    corpus = _corpus()
    pages = []
    for page in index.get("pages", []):
        url, sid = page.get("url"), page.get("source_id")
        if not offline:
            if corpus is None:
                return None, (common.EXIT_PRECONDITION, "the corpus module is not available; use --offline")
            try:
                meta = corpus.fetch(url)
            except Exception as exc:
                return None, (_fetch_code(exc), f"cannot fetch {url}: {exc}")
            sid = meta.get("source_id") or sid
        if not sid and corpus is not None:
            try:
                sid = corpus.source_id_for(url)
            except Exception:
                sid = None
        text, meta, sha = _snapshot(sid)
        if text is None:
            return None, (common.EXIT_PRECONDITION, f"no snapshot for {url} (source_id {sid}); run `saa.py guide` first")
        pages.append({"source_id": sid, "url": meta.get("url") or url, "sha256": sha, "text": text})
    if not pages:
        return None, (common.EXIT_PRECONDITION, "the guide index lists no pages")
    return pages, None


def _schema_findings(obj, name, file) -> list:
    try:
        errors = schemas.validate(obj, name)
    except FileNotFoundError as exc:
        errors = [str(exc)]
    return [_finding("X01", err, file=file) for err in errors]


def build(offline: bool = False, accept_changes: bool = False):
    """Run `registry build`. Returns (exit code, result dict)."""
    spec = _spec()
    seed = common.read_json(_seed_path())
    current = common.read_json(_book_path())
    if seed is None and current is None:
        return common.EXIT_PRECONDITION, {"error": "no book.seed.json and no data/book.json"}
    book = _merge_book(seed, current, spec)
    guide_cfg = book["book"]["exam_guide"]
    index_path = common.CORPUS / "index" / f"{common.slugify(guide_cfg['guide_id'])}.json"
    index = common.read_json(index_path)
    if not index:
        return common.EXIT_PRECONDITION, {"error": f"missing {_book_rel(index_path)}; run `saa.py guide {guide_cfg['root']}`"}
    pages, problem = _load_pages(index, offline)
    if problem:
        return problem[0], {"error": problem[1]}
    parsed = parse_pages(pages)

    with _locks(_book_path(), _guide_path(), _services_path()):
        book = _merge_book(seed, common.read_json(_book_path()), spec)
        chapter_keys = _chapter_keys(book)
        in_scope = _entries(parsed["in_scope_raw"], book, True)
        out_scope = _entries(parsed["out_of_scope_raw"], book, False)
        unmapped = _unmapped(in_scope, chapter_keys)
        result = {"chapters": len(book["chapters"]), "domains": len(parsed["domains"]), "tasks": len(parsed["tasks"]),
                  "bullets": len(parsed["bullets"]), "in_scope": len(parsed["in_scope_raw"]),
                  "in_scope_unique": len(in_scope), "out_of_scope": len(out_scope), "unmapped": unmapped,
                  "changed_bullets": []}
        if parsed["problems"]:
            result["error"] = "; ".join(parsed["problems"])
            return common.EXIT_FAIL, result
        old = common.read_json(_guide_path())
        if old:
            new_text = {b["id"]: b["text"] for b in parsed["bullets"]}
            result["changed_bullets"] = [b["id"] for b in old.get("bullets", []) if new_text.get(b["id"]) != b["text"]]
            if result["changed_bullets"] and not accept_changes:
                result["error"] = "bullet text changed or id disappeared; nothing written (use --accept-changes)"
                return common.EXIT_FAIL, result
        now = common.now_iso()
        guide = {"exam": book["book"].get("exam", "SAA-C03"), "root": guide_cfg["root"], "built_at": now,
                 "pages": parsed["pages"], "domains": parsed["domains"], "tasks": parsed["tasks"],
                 "bullets": parsed["bullets"],
                 "counts": {"domains": len(parsed["domains"]), "tasks": len(parsed["tasks"]),
                            "bullets": len(parsed["bullets"])}}
        service_doc = {"exam": guide["exam"], "built_at": now, "in_scope": in_scope, "out_of_scope": out_scope,
                       "counts": {"in_scope": len(parsed["in_scope_raw"]), "in_scope_unique": len(in_scope),
                                  "out_of_scope": len(out_scope), "unmapped": len(unmapped)}}
        book["book"]["exam_guide_counts"] = {"domains": len(parsed["domains"]), "tasks": len(parsed["tasks"]),
                                             "bullets": len(parsed["bullets"]), "in_scope": len(parsed["in_scope_raw"]),
                                             "out_of_scope": len(out_scope)}
        book["book"]["built_at"] = now
        findings = (_schema_findings(guide, "exam-guide", "_build/registry/exam-guide.json")
                    + _schema_findings(service_doc, "services", "_build/registry/services.json")
                    + _schema_findings(book, "book", "data/book.json"))
        if findings:
            result["error"] = "schema errors; nothing written"
            result["errors"] = findings[:20]
            return common.EXIT_FAIL, result
        common.write_json(_guide_path(), guide)
        common.write_json(_services_path(), service_doc)
        common.write_json(_book_path(), book)
    return (common.EXIT_WARN if unmapped else common.EXIT_OK), result


def cmd_build(args) -> int:
    code, result = build(offline=args.offline, accept_changes=args.accept_changes)
    if "error" in result and len(result) == 1:
        if args.json:
            common.emit(result, args)
        return common.fail(result["error"], code)
    lines = [f"registry build: {'FAIL' if code == common.EXIT_FAIL else 'ok'} chapters={result['chapters']} "
             f"domains={result['domains']} tasks={result['tasks']} bullets={result['bullets']} "
             f"in_scope={result['in_scope']} unique={result['in_scope_unique']} out_of_scope={result['out_of_scope']} "
             f"unmapped={len(result['unmapped'])} changed_bullets={len(result['changed_bullets'])}"]
    if result.get("error"):
        lines.append("error: " + result["error"])
    lines += [_finding_text(f) for f in result.get("errors", [])]
    lines += [f"changed bullet: {b}" for b in result["changed_bullets"]]
    lines += [f"unmapped: {name}" for name in result["unmapped"]]
    _out(args, result, lines)
    return code


# ---------------------------------------------------------------- registry set

def _split(value) -> list:
    return [part.strip() for part in (value or "").split(",") if part.strip()]


def _host_ok(url: str) -> bool:
    try:
        return (urllib.parse.urlsplit(url).hostname or "").lower() in common.ALLOWED_HOSTS
    except ValueError:
        return False


def _input_file(name: str):
    """(object, None) or (None, (exit code, message)) for a --file argument."""
    path = Path(name)
    if not path.is_absolute():
        path = common.REPO / path
    if not common.inside_book(path):
        return None, (common.EXIT_POLICY, f"--file must be inside {common.REAL_BOOK}")
    if not path.exists():
        return None, (common.EXIT_PRECONDITION, f"no such file: {name}")
    try:
        obj = json.loads(path.read_text(encoding="utf-8"))
    except ValueError as exc:
        return None, (common.EXIT_FAIL, f"{name} is not valid JSON: {exc}")
    if not isinstance(obj, dict):
        return None, (common.EXIT_FAIL, f"{name} must hold one JSON object")
    return obj, None


def set_chapter(ch_id, patch=None, replace=(), by="unknown"):
    """Apply a patch to one chapter of data/book.json. Returns (exit code, result dict)."""
    patch = copy.deepcopy(patch or {})
    replace = set(replace or ())
    for key in patch:
        if key in SEED_KEYS:
            return common.EXIT_FAIL, {"error": f"`{key}` is owned by the seed; change book.seed.json and run registry build"}
        if key not in PATCH_KEYS:
            return common.EXIT_FAIL, {"error": f"unknown patch key `{key}`"}
    sources = patch.get("sources") or {}
    if not isinstance(sources, dict) or any(k not in SOURCE_LISTS or not isinstance(v, list) for k, v in sources.items()):
        return common.EXIT_FAIL, {"error": f"`sources` takes the lists {', '.join(SOURCE_LISTS)}"}
    for key in ("tasks", "bullets", "cards"):
        if not isinstance(patch.get(key, []), list):
            return common.EXIT_FAIL, {"error": f"`{key}` must be a list"}
    if "notes" in patch and (not isinstance(patch["notes"], str) or len(patch["notes"]) > NOTES_MAX_CHARS):
        return common.EXIT_FAIL, {"error": f"`notes` must be one string of at most {NOTES_MAX_CHARS} characters"}
    service_map = patch.get("service_map") or {}
    if not isinstance(service_map, dict) or any(not isinstance(v, list) for v in service_map.values()):
        return common.EXIT_FAIL, {"error": "`service_map` maps an official name to a list of keys"}
    for name in replace:
        if name not in ("bullets", "tasks", "cards") and not (name.startswith("sources.") and name[8:] in SOURCE_LISTS):
            return common.EXIT_FAIL, {"error": f"--replace takes sources.<list>, bullets, tasks or cards, not `{name}`"}
    for name in URL_LISTS:
        for url in sources.get(name, []):
            if not isinstance(url, str) or not _host_ok(url):
                return common.EXIT_POLICY, {"error": f"host of {url!r} is not in the allow-list"}
            if not url.startswith("https://"):
                return common.EXIT_FAIL, {"error": f"{url!r} is not an https URL"}

    with _locks(_book_path(), _services_path()):
        book = common.read_json(_book_path())
        if book is None:
            return common.EXIT_PRECONDITION, {"error": "no data/book.json; run registry build first"}
        ch = _find_chapter(book, ch_id)
        if ch is None:
            return common.EXIT_PRECONDITION, {"error": f"unknown chapter {ch_id!r}"}
        chapter_keys = _chapter_keys(book)
        guide = exam_guide()
        if (patch.get("bullets") or patch.get("tasks")) and guide is None:
            return common.EXIT_PRECONDITION, {"error": "no exam-guide.json; run registry build first"}
        bullet_task = {b["id"]: b["task"] for b in (guide or {}).get("bullets", [])}
        task_ids = {t["id"] for t in (guide or {}).get("tasks", [])}
        for bullet in patch.get("bullets", []):
            if bullet not in bullet_task:
                return common.EXIT_FAIL, {"error": f"bullet {bullet!r} is not in exam-guide.json"}
        for task in patch.get("tasks", []):
            if task not in task_ids:
                return common.EXIT_FAIL, {"error": f"task {task!r} is not in exam-guide.json"}
        for name, keys in service_map.items():
            for key in keys:
                if key not in chapter_keys:
                    return common.EXIT_FAIL, {"error": f"mapped key {key!r} ({name}) is a service of no chapter"}
        for key in patch.get("cards", []):
            if key not in ch.get("services", []):
                return common.EXIT_FAIL, {"error": f"cards key {key!r} is not a service of chapter {ch['id']}"}

        added = {}

        def merge(label, target, key, new):
            old = [] if label in replace else list(target.get(key, []))
            result = _dedupe(old + list(new))
            count = len([x for x in result if x not in old])
            if count or label in replace:
                added[label] = count
            target[key] = result

        ch_sources = ch.setdefault("sources", {})
        for name in SOURCE_LISTS:
            ch_sources.setdefault(name, [])
            label = f"sources.{name}"
            if name in sources or label in replace:
                merge(label, ch_sources, name, sources.get(name, []))
        if "bullets" in patch or "bullets" in replace:
            merge("bullets", ch, "bullets", patch.get("bullets", []))
        ch.setdefault("bullets", [])
        bullet_tasks = _dedupe(bullet_task[b] for b in ch["bullets"] if b in bullet_task)
        if "tasks" in replace:
            ch["tasks"] = []
        before = list(ch.get("tasks", []))
        ch["tasks"] = _dedupe(before + list(patch.get("tasks", [])) + bullet_tasks)
        new_tasks = len([t for t in ch["tasks"] if t not in before])
        if new_tasks or "tasks" in replace:
            added["tasks"] = new_tasks
        if "cards" in patch:
            ch["cards"] = _dedupe(patch["cards"])
            added["cards"] = len(ch["cards"])
        if "notes" in patch:                # one string; it replaces the old note, and an empty string removes it
            note = " ".join(patch["notes"].split())
            if note != ch.get("notes", ""):
                added["notes"] = 1
            if note:
                ch["notes"] = note
            else:
                ch.pop("notes", None)
        map_changed = 0
        if service_map:
            current_map = book.setdefault("service_map", {})
            for name, keys in service_map.items():
                keys = _dedupe(keys)
                if not keys:
                    if name in current_map:
                        del current_map[name]
                        map_changed += 1
                elif current_map.get(name) != keys:
                    current_map[name] = keys
                    map_changed += 1
            if map_changed:
                added["service_map"] = map_changed

        findings = _schema_findings(book, "book", "data/book.json")
        if findings:
            return common.EXIT_FAIL, {"error": "the patch breaks book.schema.json; nothing written", "errors": findings[:20]}
        common.write_json(_book_path(), book)
        if map_changed:
            doc = common.read_json(_services_path())
            if doc:
                for entry in doc.get("in_scope", []):
                    _set_keys(entry, book, chapter_keys)
                doc.setdefault("counts", {})["unmapped"] = len(_unmapped(doc.get("in_scope", []), chapter_keys))
                common.write_json(_services_path(), doc)
        return common.EXIT_OK, {"chapter": ch["id"], "added": added, "tasks": ch["tasks"]}


def cmd_set(args) -> int:
    patch = {}
    if args.file:
        patch, problem = _input_file(args.file)
        if problem:
            return common.fail(problem[1], problem[0])
    if args.bullets:
        patch["bullets"] = list(patch.get("bullets", [])) + _split(args.bullets)
    if args.cards is not None:
        patch["cards"] = _split(args.cards)
    for item in args.map or []:
        if "=" not in item:
            return common.fail(f"--map takes \"Official name=key1,key2\", not {item!r}")
        name, keys = item.split("=", 1)
        patch.setdefault("service_map", {})[name.strip()] = _split(keys)
    replace = [name for group in (args.replace or []) for name in group]
    code, result = set_chapter(args.chapter, patch, replace, by=args.by)
    if "error" in result:
        if args.json:
            common.emit(result, args)
        return common.fail(result["error"], code)
    added = " ".join(f"{k}=+{v}" for k, v in result["added"].items()) or "nothing new"
    _out(args, result, [f"registry set {result['chapter']}: {added}; tasks={','.join(result['tasks'])}"])
    return code


# ---------------------------------------------------------------- registry check

def _corpus_urls() -> dict:
    """url -> meta for every snapshot meta in the corpus (TOOLS.md section 0, rule 11)."""
    found = {}
    base = common.CORPUS / "snap"
    if base.is_dir():
        for path in sorted(base.rglob("*.meta.json")):
            try:
                meta = common.read_json(path) or {}
            except ValueError:
                continue
            if meta.get("url"):
                found.setdefault(meta["url"], meta)
    return found


def _meta_for(url: str, by_url: dict):
    corpus = _corpus()
    if corpus is not None:
        try:
            meta = corpus.load_meta(corpus.source_id_for(url))
            if meta is not None:
                return meta
        except Exception:
            pass
    return by_url.get(url)


def _page_path(url: str) -> str:
    path = urllib.parse.urlsplit(url or "").path
    for ext in (".html", ".htm", ".md"):
        if path.endswith(ext):
            return path[:-len(ext)]
    return path.rstrip("/")


def _guide_index(root: str):
    """The index that `saa.py guide ROOT` made, or None.

    A guide root (sources.guides) is not a page: it has no snapshot. It is "in the corpus" when its
    index exists under corpus/index/ (the default guide id, or any index whose `root` is this URL).
    """
    want = (root or "").rstrip("/")
    corpus = _corpus()
    if corpus is not None:
        try:
            index = corpus.load_index(corpus.guide_id_for(root))
        except Exception:
            index = None
        if isinstance(index, dict) and (index.get("root") or "").rstrip("/") == want:
            return index
    base = common.CORPUS / "index"
    if base.is_dir():
        for path in sorted(base.glob("*.json")):
            try:
                index = common.read_json(path)
            except ValueError:
                continue
            if isinstance(index, dict) and (index.get("root") or "").rstrip("/") == want:
                return index
    return None


def check(urls: bool = False, fetch: bool = False) -> dict:
    """`registry check`: {"ok", "errors", "warnings", "counts"} or {"error"} when book.json is missing."""
    book = common.read_json(_book_path())
    if book is None:
        return {"error": "no data/book.json; run registry build first"}
    spec = _spec()
    errors, warnings = [], []
    book_file, guide_file, serv_file = "data/book.json", "_build/registry/exam-guide.json", "_build/registry/services.json"

    def err(code, msg, file=book_file, item=None):
        errors.append(_finding(code, msg, file=file, item=item))

    def warn(code, msg, file=book_file, item=None):
        warnings.append(_finding(code, msg, file=file, item=item))

    # R01 schemas
    guide, service_doc = exam_guide(), services()
    for obj, name, file in ((book, "book", book_file), (guide, "exam-guide", guide_file), (service_doc, "services", serv_file)):
        if obj is None:
            err("R01", "file is missing; run registry build", file=file)
            continue
        for finding in _schema_findings(obj, name, file):
            err("R01", finding["msg"], file=file)
    chapters = [ch for ch in book.get("chapters", []) if isinstance(ch, dict) and "id" in ch and "slug" in ch]
    guide = guide if isinstance(guide, dict) else {}
    service_doc = service_doc if isinstance(service_doc, dict) else {}

    # R02 chapters
    parts = {p.get("id") for p in book.get("parts", []) if isinstance(p, dict)}
    templates = spec.get("templates") or {}
    overrides = spec.get("chapter_overrides") or {}
    seen = {"id": {}, "slug": {}, "service key": {}}
    for ch in chapters:
        cid = ch["id"]
        for kind, values in (("id", [cid]), ("slug", [ch["slug"]]), ("service key", ch.get("services", []))):
            for value in values:
                if value in seen[kind]:
                    err("R02", f"{kind} `{value}` is used twice (chapters {seen[kind][value]} and {cid})", item=cid)
                else:
                    seen[kind][value] = cid
        if ch.get("part") not in parts:
            err("R02", f"part `{ch.get('part')}` does not exist", item=cid)
        key = _template_key(ch, spec)
        if key not in templates:
            err("R02", f"template `{key}` is not in SPEC.json", item=cid)
        if ch.get("tier") in ("front", "synthesis") and cid not in overrides:
            err("R02", f"a {ch.get('tier')} chapter needs a chapter_overrides entry in SPEC.json", item=cid)
        for card in ch.get("cards", []):
            if card not in ch.get("services", []):
                err("R02", f"cards key `{card}` is not a service of the chapter", item=cid)
    chapter_keys = _chapter_keys({"chapters": chapters})

    # R03 bullets and tasks
    assigned_bullets = {b for ch in chapters for b in ch.get("bullets", [])}
    assigned_tasks = {t for ch in chapters for t in ch.get("tasks", [])}
    unassigned = [b["id"] for b in guide.get("bullets", []) if b.get("id") not in assigned_bullets]
    for bullet in unassigned:
        err("R03", "bullet is in the bullets of no chapter", item=bullet)
    for task in guide.get("tasks", []):
        if task.get("id") not in assigned_tasks:
            err("R03", "task statement is in the tasks of no chapter", item=task.get("id"))

    # R04, R05, R11 services (keys are recomputed from the current book)
    mapped_keys, unmapped = set(), 0
    for entry in service_doc.get("in_scope", []):
        keys = keys_for(entry.get("official_name", ""), entry.get("short_name"), book, chapter_keys)
        mapped_keys |= set(keys)
        if not _has_home(keys, chapter_keys):
            unmapped += 1
            err("R04", f"in-scope entry `{entry.get('official_name')}` has no key with a home chapter",
                file=serv_file, item=entry.get("id"))
    for entry in service_doc.get("out_of_scope", []):
        for slug in auto_slugs(entry.get("official_name", ""), entry.get("short_name")):
            if slug in chapter_keys:
                err("R05", f"service key `{slug}` matches the out-of-scope entry `{entry.get('official_name')}`",
                    item=chapter_keys[slug]["id"])
    if service_doc:
        for key, ch in chapter_keys.items():
            if key not in mapped_keys:
                warn("R11", f"service key `{key}` maps to no in-scope entry", item=ch["id"])

    # R06, R16 sources
    by_url = _corpus_urls() if urls else {}
    corpus = _corpus()
    for ch in chapters:
        for name in URL_LISTS:
            for url in (ch.get("sources") or {}).get(name, []):
                if not _host_ok(url):
                    err("R06", f"sources.{name}: host of {url} is not allowed", item=ch["id"])
                    continue
                if not urls:
                    continue
                if name == "guides":            # a guide root has an index, not a snapshot
                    index = _guide_index(url)
                    if index is None and fetch and corpus is not None:
                        try:
                            corpus.build_guide(url)
                        except Exception as exc:
                            err("R06", f"sources.guides: cannot index {url}: {exc}", item=ch["id"])
                            continue
                        index = _guide_index(url)
                    if index is None:
                        err("R06", f"sources.guides: {url} has no guide index; run `saa.py guide {url}`", item=ch["id"])
                    continue
                meta = _meta_for(url, by_url)
                if meta is None and fetch:
                    if corpus is None:
                        err("R06", f"sources.{name}: cannot fetch {url}: no corpus module", item=ch["id"])
                        continue
                    try:
                        meta = corpus.fetch(url)
                    except Exception as exc:
                        err("R06", f"sources.{name}: cannot fetch {url}: {exc}", item=ch["id"])
                        continue
                if meta is None:
                    err("R06", f"sources.{name}: {url} is not in the corpus", item=ch["id"])
                elif meta.get("final_url") and _page_path(meta["final_url"]) != _page_path(meta.get("url") or url):
                    warn("R16", f"sources.{name}: {url} was redirected to {meta['final_url']}", item=ch["id"])

    # R07 fact namespaces
    ids = {ch["id"] for ch in chapters}
    for name, home in ((book.get("book") or {}).get("fact_namespaces") or {}).items():
        if home not in ids:
            err("R07", f"fact namespace `{name}` points to `{home}`, which is not a chapter id")
        if name in chapter_keys:
            err("R07", f"fact namespace `{name}` equals a service key")

    # R12 sources of deep and medium chapters
    for ch in chapters:
        sources = ch.get("sources") or {}
        if ch.get("tier") in ("deep", "medium") and not sources.get("guides") and not sources.get("pages"):
            warn("R12", f"{ch.get('tier')} chapter has no sources.guides and no sources.pages", item=ch["id"])

    return {"ok": not errors, "errors": errors, "warnings": warnings,
            "counts": {"chapters": len(chapters), "bullets_unassigned": len(unassigned), "services_unmapped": unmapped}}


def cmd_check(args) -> int:
    result = check(urls=args.urls or args.fetch, fetch=args.fetch)
    if "error" in result:
        if args.json:
            common.emit(result, args)
        return common.fail(result["error"], common.EXIT_PRECONDITION)
    counts = result["counts"]
    lines = [f"registry check: {'ok' if result['ok'] else 'FAIL'} errors={len(result['errors'])} "
             f"warnings={len(result['warnings'])} chapters={counts['chapters']} "
             f"bullets_unassigned={counts['bullets_unassigned']} services_unmapped={counts['services_unmapped']}"]
    lines += [_finding_text(f) for f in result["errors"]] + [_finding_text(f) for f in result["warnings"]]
    _out(args, result, lines)
    if result["errors"]:
        return common.EXIT_FAIL
    return common.EXIT_WARN if result["warnings"] else common.EXIT_OK


# ---------------------------------------------------------------- registry show, wave-args

def cmd_show(args) -> int:
    book = common.load_book()
    ch = _find_chapter(book, args.chapter)
    if ch is None:
        return common.fail(f"unknown chapter {args.chapter!r}", common.EXIT_PRECONDITION)
    texts = {b["id"]: b["text"] for b in (exam_guide() or {}).get("bullets", [])}
    bullets = [{"id": b, "text": texts.get(b)} for b in ch.get("bullets", [])]
    mine = set(ch.get("services", []))
    entries = [{"official_name": e["official_name"], "keys": e["keys"], "categories": e["categories"]}
               for e in (services() or {}).get("in_scope", []) if mine & set(e.get("keys", []))]
    result = {"chapter": ch, "bullets": bullets, "services": entries}
    sources = ch.get("sources") or {}
    lines = [f"{ch['id']} {ch['slug']} \"{ch['title']}\" tier={ch['tier']}"
             + (f" kind={ch['kind']}" if ch.get("kind") else "") + (" xl" if ch.get("xl") else "")
             + f" wave={ch['wave']} part={ch['part']}",
             "services: " + (", ".join(ch.get("services", [])) or "none"),
             "tasks: " + (", ".join(ch.get("tasks", [])) or "none")]
    if ch.get("cards"):
        lines.append("cards: " + ", ".join(ch["cards"]))
    if ch.get("notes"):
        note = ch["notes"]
        lines.append("notes: " + (note if len(note) <= 300 else note[:297] + "..."))
    lines += [f"sources.{name}: {len(sources.get(name, []))}" for name in SOURCE_LISTS if sources.get(name)]
    lines += [f"bullet {b['id']}: {b['text'] or '(not in exam-guide.json)'}" for b in bullets]
    lines += [f"in scope: {e['official_name']} -> {','.join(e['keys'])}" for e in entries]
    _out(args, result, lines)
    return common.EXIT_OK


def wave_args(wave: str):
    """The object of `registry wave-args`, or None for an unknown wave."""
    wave = str(wave).strip()
    wave = wave if wave.upper().startswith("W") else "W" + wave
    wave = wave.upper()
    book = common.load_book()
    spec = _spec()
    chapters = [ch for ch in book["chapters"] if ch.get("wave") == wave]
    if not chapters:
        return None
    out, skipped = [], []
    for ch in chapters:
        ledger = _ledger(ch["id"])
        status = ledger.get("status") or "planned"
        if status == "ready" and not ledger.get("stale"):
            skipped.append({"id": ch["id"], "reason": "ready"})
            continue
        template = _template(ch, spec)
        key = template.get("key")
        plan = _plan_counts(ch, template)
        out.append({"id": ch["id"], "slug": ch["slug"], "dir": f"{ch['id']}-{ch['slug']}", "title": ch["title"],
                    "tier": ch["tier"], "template": key, "xl": bool(ch.get("xl")), "services": ch.get("services", []),
                    "tasks": ch.get("tasks", []), "bullets": len(ch.get("bullets", [])),
                    "mine_lenses": {"deep": 5, "medium": 3}.get(key, 2), "counts": plan,
                    "status": status, "next_stage": _next_stage(ch, ledger, plan)})
    return {"wave": wave, "chapters": out, "skipped": skipped}


def cmd_wave_args(args) -> int:
    result = wave_args(args.wave)
    if result is None:
        return common.fail(f"unknown wave {args.wave!r}", common.EXIT_PRECONDITION)
    common.emit(json.dumps(result, ensure_ascii=False, separators=(",", ":")), args)
    return common.EXIT_OK


# ---------------------------------------------------------------- coverage

def _items(path: Path) -> list:
    try:
        doc = common.read_json(path)
    except ValueError:
        return []
    if isinstance(doc, dict):
        doc = doc.get("items", [])
    return [item for item in doc or [] if isinstance(item, dict)]


def _all_facts() -> dict:
    facts = {}
    if common.FACTS_DIR.is_dir():
        for path in sorted(common.FACTS_DIR.glob("*.jsonl")):
            try:
                rows = common.read_jsonl(path)
            except ValueError:
                continue
            for row in rows:
                if isinstance(row, dict) and row.get("id"):
                    facts[row["id"]] = row
    return facts


def coverage(release: bool = False):
    """Write coverage.json and coverage.md. Returns (exit code, report dict) or (3, {"error"})."""
    book = common.read_json(_book_path())
    guide, service_doc = exam_guide(), services()
    if book is None or guide is None or service_doc is None:
        return common.EXIT_PRECONDITION, {"error": "book.json, exam-guide.json and services.json are needed; run registry build"}
    chapters = book["chapters"]
    status = {ch["id"]: (_ledger(ch["id"]).get("status") or "planned") for ch in chapters}
    facts = _all_facts()
    questions, cards, by_id = [], [], {}
    for ch in chapters:
        folder = common.DATA / f"{ch['id']}-{ch['slug']}"
        for item in _items(folder / "questions.json"):
            questions.append(item)
            by_id.setdefault(item.get("id"), item)
        cards += _items(folder / "cards.json")
    live = [q for q in questions if q.get("status") == "ready" and q.get("pool") in ("chapter", "drill")]
    ready_cards = [c for c in cards if c.get("status") == "ready"]
    mocks = {}
    for ch in chapters:
        if ch.get("tier") != "mock":
            continue
        try:
            manifest = common.read_json(common.DATA / f"{ch['id']}-{ch['slug']}" / "mock.json") or {}
        except ValueError:
            manifest = {}
        mocks[ch["id"]] = [by_id[q] for q in manifest.get("questions", []) if q in by_id]
    mock_items = [q for items in mocks.values() for q in items]

    def card_services(card):
        if card.get("services"):
            return set(card["services"])
        return {facts[f]["service"] for f in card.get("facts") or [] if f in facts and facts[f].get("service")}

    errors, warnings = [], []

    def report(blocking, code, msg, item):
        (errors if blocking and release else warnings).append(_finding(code, msg, item=item))

    bullet_rows = []
    for bullet in guide["bullets"]:
        bid = bullet["id"]
        homes = [ch["id"] for ch in chapters if bid in ch.get("bullets", [])]
        row = {"id": bid, "chapters": homes, "ready_chapters": sum(1 for c in homes if status[c] == "ready"),
               "questions": sum(1 for q in live if bid in (q.get("bullets") or [])),
               "mock_questions": sum(1 for q in mock_items if bid in (q.get("bullets") or []))}
        bullet_rows.append(row)
        if row["ready_chapters"] == 0 or row["questions"] == 0:
            report(True, "V01", f"bullet has {row['ready_chapters']} ready chapters and {row['questions']} questions", bid)
        elif row["questions"] < 2:
            report(False, "V11", f"bullet has {row['questions']} question", bid)
    service_rows = []
    for entry in service_doc["in_scope"]:
        keys = set(entry.get("keys", []))
        row = {"id": entry["id"], "keys": entry.get("keys", []), "home_chapter": entry.get("home_chapter"),
               "level": entry.get("level"),
               "facts": sum(1 for f in facts.values() if f.get("status") == "verified" and f.get("service") in keys),
               "cards": sum(1 for c in ready_cards if keys & card_services(c)),
               "questions": sum(1 for q in live if keys & set(q.get("services") or []))}
        service_rows.append(row)
        if not row["home_chapter"]:
            report(True, "V02", "in-scope service has no home chapter", row["id"])
        if row["level"] == "deep":
            if row["facts"] == 0 or row["questions"] == 0:
                report(True, "V03", f"deep-level service has {row['facts']} facts and {row['questions']} questions", row["id"])
            elif row["questions"] < 5:
                report(False, "V12", f"deep-level service has {row['questions']} questions", row["id"])
        if row["cards"] == 0:
            report(False, "V13", "service has 0 cards", row["id"])
    task_rows = []
    for task in guide["tasks"]:
        tid = task["id"]
        row = {"id": tid, "questions": sum(1 for q in live if q.get("task") == tid),
               "mock": {mock: sum(1 for q in items if q.get("task") == tid) for mock, items in mocks.items()}}
        task_rows.append(row)
        for mock, n in row["mock"].items():
            if n == 0:
                report(True, "V04", f"task statement is absent from mock {mock}", tid)

    doc = {"bullets": bullet_rows, "services": service_rows, "tasks": task_rows, "errors": errors, "warnings": warnings}
    common.write_json(common.REPORTS / "coverage.json", doc)
    md = ["# Coverage", "",
          f"Made {common.now_iso()}{' (release rules)' if release else ''}. "
          f"{len(bullet_rows)} bullets, {len(service_rows)} in-scope services, {len(task_rows)} task statements. "
          f"{len(errors)} errors, {len(warnings)} warnings.", "",
          "## Bullets", "", "| Bullet | Chapters | Ready chapters | Questions | Mock questions |", "|---|---|---|---|---|"]
    md += [f"| {r['id']} | {', '.join(r['chapters']) or '-'} | {r['ready_chapters']} | {r['questions']} | {r['mock_questions']} |"
           for r in bullet_rows]
    md += ["", "## Services", "", "| Service | Keys | Home | Level | Facts | Cards | Questions |", "|---|---|---|---|---|---|---|"]
    md += [f"| {r['id']} | {', '.join(r['keys']) or '-'} | {r['home_chapter'] or '-'} | {r['level'] or '-'} | {r['facts']} "
           f"| {r['cards']} | {r['questions']} |" for r in service_rows]
    md += ["", "## Task statements", "", "| Task | Questions | Mocks |", "|---|---|---|"]
    md += [f"| {r['id']} | {r['questions']} | {', '.join(f'{k}: {v}' for k, v in r['mock'].items()) or '-'} |" for r in task_rows]
    md += ["", "## Findings", ""]
    md += [f"- error {_finding_text(f)}" for f in errors] + [f"- warning {_finding_text(f)}" for f in warnings]
    common.ensure_dir(common.REPORTS)
    (common.REPORTS / "coverage.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    code = common.EXIT_FAIL if errors else (common.EXIT_WARN if warnings else common.EXIT_OK)
    return code, doc


def cmd_coverage(args) -> int:
    code, doc = coverage(release=args.release)
    if "error" in doc:
        if args.json:
            common.emit(doc, args)
        return common.fail(doc["error"], code)
    summary = {"ok": not doc["errors"], "report": _book_rel(common.REPORTS / "coverage.json"),
               "counts": {"bullets": len(doc["bullets"]), "services": len(doc["services"]), "tasks": len(doc["tasks"]),
                          "errors": len(doc["errors"]), "warnings": len(doc["warnings"])},
               "errors": doc["errors"][:20], "warnings": doc["warnings"][:20]}
    lines = [f"coverage: {'ok' if summary['ok'] else 'FAIL'} bullets={len(doc['bullets'])} services={len(doc['services'])} "
             f"tasks={len(doc['tasks'])} errors={len(doc['errors'])} warnings={len(doc['warnings'])} "
             f"report={summary['report']}"]
    lines += [_finding_text(f) for f in doc["errors"]] + [_finding_text(f) for f in doc["warnings"]]
    _out(args, summary, lines)
    return code


# ---------------------------------------------------------------- command line

def register(subparsers) -> None:
    reg = subparsers.add_parser("registry", help="the chapter registry and the parsed exam guide")
    sub = reg.add_subparsers(dest="registry_cmd")
    reg.set_defaults(func=lambda args: (reg.print_help(), common.EXIT_PRECONDITION)[1])

    p = sub.add_parser("build", help="build data/book.json, exam-guide.json and services.json")
    p.add_argument("--offline", action="store_true", help="read the saved snapshots only; fetch nothing")
    p.add_argument("--accept-changes", action="store_true", help="accept changed or removed bullet ids")
    common.add_common_args(p)
    p.set_defaults(func=cmd_build)

    p = sub.add_parser("set", help="add sources, bullets, tasks, cards, a note or a service map entry to a chapter")
    p.add_argument("chapter")
    p.add_argument("--file", help="a JSON patch inside aws-saa-book/ (keys: sources, tasks, bullets, cards, service_map, notes)")
    p.add_argument("--bullets", help="bullet ids, comma separated")
    p.add_argument("--cards", help="recognise-only service keys of the chapter, comma separated (replaces the list)")
    p.add_argument("--map", action="append", help='"Official name=key1,key2" (repeatable; no key removes the entry)')
    p.add_argument("--replace", action="append", nargs="+", metavar="KEY",
                   help="replace instead of merge: sources.<list>, bullets, tasks")
    p.add_argument("--by", default=os.environ.get("SAA_AGENT") or "unknown", help="who makes the write")
    common.add_common_args(p)
    p.set_defaults(func=cmd_set)

    p = sub.add_parser("check", help="check the registry files (R01 to R16)")
    p.add_argument("--urls", action="store_true", help="also check that every source URL is in the corpus")
    p.add_argument("--fetch", action="store_true", help="with --urls: fetch missing URLs first")
    common.add_common_args(p)
    p.set_defaults(func=cmd_check)

    p = sub.add_parser("show", help="print one chapter entry with its bullets and in-scope services")
    p.add_argument("chapter")
    common.add_common_args(p)
    p.set_defaults(func=cmd_show)

    p = sub.add_parser("wave-args", help="one compact object with the chapters of a wave, for a workflow")
    p.add_argument("wave")
    common.add_common_args(p)
    p.set_defaults(func=cmd_wave_args)

    p = subparsers.add_parser("coverage", help="exam guide coverage by chapters, facts, questions and cards")
    p.add_argument("--release", action="store_true", help="apply the blocking release rules (V01 to V04)")
    common.add_common_args(p)
    p.set_defaults(func=cmd_coverage)
