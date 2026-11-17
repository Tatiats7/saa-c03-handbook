"""Ledger: `stage`, `gate`, `status`, `report`, `selftest` (TOOLS.md section 3). Standard library only.

State on disk (all under common.LEDGER):
  chapters/<id>.json        one ledger per chapter (ledger-chapter.schema.json)
  gates/<id>.<gate>.json    the last record of each gate (gate.schema.json)
  events.jsonl              append-only log

Other modules call  ledger.mark_stale(ch, reason, stages=None, item_stages=None).

Gates of other modules (facts, lint, qbank, lab, diagram) are called through their Python
functions. A module or function that is missing gives "check unavailable" (code X03, exit 3):
nothing passes, and no attempt of the stage is used.
"""
from __future__ import annotations

import contextlib
import copy
import hashlib
import importlib
import io
import json
import os
import re
import sys
import unittest
from pathlib import Path

from saalib import common, schemas

# name, prerequisites, gates run by `stage end` (TOOLS.md 3.1)
STAGES = [
    ("plan", [], ["plan"]),
    ("mine", ["plan"], ["facts-mech"]),
    ("register", ["mine"], ["facts-mech"]),
    ("verify-facts", ["register"], ["facts-final"]),
    ("brief", ["verify-facts"], ["brief"]),
    ("prose", ["brief"], ["lint"]),
    ("questions", ["brief"], ["questions"]),
    ("tasks", ["brief"], ["tasks"]),
    ("cards", ["brief"], ["cards"]),
    ("speak", ["brief"], ["speak"]),
    ("diagrams", ["brief"], ["diagrams"]),
    ("edit", ["prose", "questions", "tasks", "cards", "speak", "diagrams"], ["lint", "sync"]),
    ("review", ["edit", "verify-questions"], ["findings"]),
    ("fix", ["review"], ["findings-closed", "lint", "sync"]),
    ("verify-questions", ["questions"], ["questions-verified"]),
    ("finalize", ["fix", "verify-questions"],
     ["facts-final", "lint", "sync", "questions-verified", "cards", "speak", "tasks", "diagrams", "findings-closed", "counts"]),
]
STAGE_NAMES = [s[0] for s in STAGES]
PREREQS = {s[0]: s[1] for s in STAGES}
STAGE_GATES = {s[0]: s[2] for s in STAGES}
# the order in which the stages really run (verify-questions before review); used for next_stage
RUN_ORDER = ["plan", "mine", "register", "verify-facts", "brief", "prose", "questions", "tasks", "cards", "speak",
             "diagrams", "verify-questions", "edit", "review", "fix", "finalize"]
# a gate that is skipped when its item stage is not applicable
GATE_STAGE = {"questions": "questions", "questions-verified": "verify-questions", "cards": "cards",
              "speak": "speak", "tasks": "tasks"}
FRONT_STATUS = {"prose": "draft", "fix": "reviewed", "finalize": "ready"}
OWN_GATES = {"plan": "gate_plan", "brief": "gate_brief", "findings": "gate_findings",
             "findings-closed": "gate_findings_closed", "diagrams": "gate_diagrams", "counts": "gate_counts"}
EXTERNAL_GATES = {
    "facts-mech": ("facts", "gate_mech"), "facts-final": ("facts", "gate_final"),
    "lint": ("lint", "gate_lint"), "sync": ("lint", "gate_sync"),
    "questions": ("qbank", "gate_questions"), "questions-verified": ("qbank", "gate_questions_verified"),
    "cards": ("qbank", "gate_cards"), "speak": ("qbank", "gate_speak"), "tasks": ("lab", "gate_tasks"),
}
GATE_NAMES = list(OWN_GATES) + list(EXTERNAL_GATES)
MAX_ATTEMPTS = 3
SELFTEST_REQUIRED = ["ledger", "registry", "facts", "lint", "qbank", "lab", "corpus", "feeds", "diagram", "contract"]
LIVE_STATUSES = ("drafted", "reviewed", "ready")


class Precondition(Exception):
    """Exit 3: something the command needs is missing."""


class Unavailable(Exception):
    """A check of another module cannot run because the module or function is missing."""


# ---------------------------------------------------------------- small helpers

def _module(name: str):
    """saalib.<name>, or None when it does not exist (or does not load) yet."""
    try:
        return importlib.import_module(f"saalib.{name}")
    except Exception:
        return None


def _finding(code, msg, file=None, line=None, item=None) -> dict:
    return {"code": code, "file": file, "line": line, "item": item, "msg": msg}


def _fmt(f: dict) -> str:
    if f.get("file"):
        where = f["file"] + (f":{f['line']}" if f.get("line") else "") + ": "
    elif f.get("item"):
        where = f"{f['item']}: "
    else:
        where = ""
    return f"{where}{f.get('code', '?')} {f.get('msg', '')}"


def _rel(path) -> str:
    try:
        return Path(path).resolve().relative_to(Path(common.BOOK).resolve()).as_posix()
    except ValueError:
        return str(path)


def _inputs(paths) -> list:
    seen = {}
    for path in paths:
        path = Path(path)
        if path.is_file():
            seen[_rel(path)] = common.sha256_file(path)
    return [{"path": p, "sha256": seen[p]} for p in sorted(seen)]


def _result(gate, ch_id, errors, warnings, counts=None, inputs=()) -> dict:
    return {"gate": gate, "chapter": ch_id, "ok": not errors, "exit": 1 if errors else (2 if warnings else 0),
            "errors": errors, "warnings": warnings, "counts": counts or {}, "inputs": _inputs(inputs)}


def _read(path):
    """(object, None) or (None, reason)."""
    path = Path(path)
    if not path.is_file():
        return None, "does not exist"
    try:
        return common.read_json(path), None
    except ValueError as exc:
        return None, f"is not valid JSON ({exc})"


def _spec() -> dict:
    return common.read_json(common.STYLE_DIR / "SPEC.json") or {}


def _spec_version() -> str:
    return str(_spec().get("version", "unknown"))


def _tool_version() -> str:
    for name in ("saa", "__main__"):
        version = getattr(sys.modules.get(name), "VERSION", None)
        if isinstance(version, str):
            return version
    try:
        import saa
        return str(saa.VERSION)
    except Exception:
        return "unknown"


def _dir_name(ch: dict) -> str:
    return f"{ch['id']}-{ch['slug']}"


def _work_dir(ch: dict) -> Path:
    return common.BUILD / "work" / _dir_name(ch)


def _merge(base, over):
    if isinstance(base, dict) and isinstance(over, dict):
        out = dict(base)
        for key, value in over.items():
            out[key] = _merge(base[key], value) if key in base else copy.deepcopy(value)
        return out
    return copy.deepcopy(over)


def _template(ch: dict) -> dict:
    """The resolved template: lint.template(ch) when lint exists, else the same rule (SPEC resolution.template)."""
    lint = _module("lint")
    if lint is not None and hasattr(lint, "template"):
        try:
            tpl = lint.template(ch["id"])
            if isinstance(tpl, dict):
                return tpl
        except Exception:
            pass
    spec = _spec()
    key = ch.get("kind") or ch.get("tier")
    override = dict((spec.get("chapter_overrides") or {}).get(ch["id"]) or {})
    key = override.pop("template", None) or key
    tpl = _merge(copy.deepcopy((spec.get("templates") or {}).get(key) or {}), override)
    tpl["key"] = key
    return tpl


def _numbers(value):
    if isinstance(value, bool):
        return
    if isinstance(value, (int, float)):
        yield value
    elif isinstance(value, dict):
        for sub in value.values():
            yield from _numbers(sub)


def _applies(stage: str, tpl: dict) -> bool:
    counts = tpl.get("counts") or {}
    if stage in ("questions", "verify-questions"):
        return bool((counts.get("questions") or {}).get("shipped", 0))
    if stage == "tasks":
        return any(isinstance(v, dict) and v.get("max", 0) for v in (counts.get("tasks") or {}).values())
    if stage == "cards":
        return any(n for n in _numbers(counts.get("cards") or {}))
    if stage == "speak":
        return bool((counts.get("speak") or {}).get("count", 0))
    return True


def _gate_applies(gate: str, tpl: dict) -> bool:
    return gate not in GATE_STAGE or _applies(GATE_STAGE[gate], tpl)


def _hand_files(ch: dict, tpl: dict = None) -> list:
    tpl = tpl if tpl is not None else _template(ch)
    folder = common.BOOK / _dir_name(ch)
    names = [f.get("name") for f in tpl.get("files") or [] if isinstance(f, dict) and f.get("source") == "hand"]
    if names:
        return [folder / n for n in names if n and (folder / n).is_file()]
    out = []
    if folder.is_dir():
        for path in sorted(folder.glob("*.md")):
            first = path.read_text(encoding="utf-8").split("\n", 1)[0]
            if "generated by saa.py" not in first:
                out.append(path)
    return out


def _fact_rows() -> list:
    rows = []
    if common.FACTS_DIR.is_dir():
        for path in sorted(common.FACTS_DIR.glob("*.jsonl")):
            for row in common.read_jsonl(path):
                row["_file"] = path
                rows.append(row)
    return rows


def _items(ch: dict, kind: str) -> list:
    doc = common.read_json(common.DATA / _dir_name(ch) / f"{kind}.json")
    if isinstance(doc, dict):
        doc = doc.get("items")
    return [i for i in doc or [] if isinstance(i, dict)]


def _open_requests(ch_id: str) -> list:
    rows = common.read_jsonl(common.BUILD / "facts" / "requests.jsonl")
    return [r for r in rows if str(r.get("chapter")) == ch_id and r.get("status") == "open"]


# ---------------------------------------------------------------- ledger file

def _ledger_path(ch_id: str) -> Path:
    return common.LEDGER / "chapters" / f"{ch_id}.json"


def _gate_path(ch_id: str, gate: str) -> Path:
    return common.LEDGER / "gates" / f"{ch_id}.{gate}.json"


def _blank_stage() -> dict:
    return {"status": "fail", "attempts": 0, "pass_seq": 0, "inputs_hash": None, "started": None, "ended": None,
            "run": None, "gates": [], "counts": {}, "reason": None, "note": None}


def _load(ch: dict) -> dict:
    led = common.read_json(_ledger_path(ch["id"]))
    if led is None:
        led = {"chapter": ch["id"], "slug": ch["slug"], "status": "planned", "blocked": None, "rev": 0,
               "style_version": _spec_version(), "stages": {}, "warnings": [], "stale": [], "updated": common.now_iso()}
    led.setdefault("blocked", None)
    led.setdefault("stale", [])
    led.setdefault("warnings", [])
    return led


def _status_of(led: dict) -> str:
    if led.get("blocked"):
        return "blocked"
    for stage, status in (("finalize", "ready"), ("fix", "reviewed"), ("edit", "drafted"), ("verify-facts", "facts-verified")):
        if (led["stages"].get(stage) or {}).get("status") == "pass":
            return status
    return "planned"


def _event(ch_id, stage, event, detail, run=None) -> None:
    common.append_jsonl(common.LEDGER / "events.jsonl",
                        {"ts": common.now_iso(), "chapter": ch_id, "stage": stage, "event": event, "detail": detail, "run": run})


def _save(led: dict, run=None) -> None:
    """Recompute the chapter status, validate and write. Call inside file_lock(_ledger_path)."""
    before = led.get("status")
    led["status"] = _status_of(led)
    led["updated"] = common.now_iso()
    errors = schemas.validate(led, "ledger-chapter")
    if errors:
        raise RuntimeError("X01 ledger file would be invalid: " + "; ".join(errors[:3]))
    common.write_json(_ledger_path(led["chapter"]), led)
    if before != led["status"]:
        _event(led["chapter"], None, "status", f"{before} -> {led['status']}", run)


def _dependents(stages) -> list:
    """Every stage that depends, directly or not, on one of `stages` (table order)."""
    hit = set(stages)
    changed = True
    while changed:
        changed = False
        for name in STAGE_NAMES:
            if name not in hit and any(p in hit for p in PREREQS[name]):
                hit.add(name)
                changed = True
    return [n for n in STAGE_NAMES if n in hit and n not in stages]


def _set_stale(led: dict, names, reason: str, run=None) -> list:
    done = []
    for name in names:
        st = led["stages"].get(name)
        if st and st.get("status") == "pass":
            st["status"] = "stale"
            st["reason"] = reason
            done.append(name)
            _event(led["chapter"], name, "stale", reason, run)
    return done


def _eff_status(led: dict, stage: str, tpl: dict):
    if not _applies(stage, tpl):
        return "na"
    status = (led["stages"].get(stage) or {}).get("status")
    return None if status == "na" else status


def _inputs_hash(ch: dict, stage: str, led: dict) -> str:
    prereqs = {p: (led["stages"].get(p) or {}).get("pass_seq", 0) for p in PREREQS[stage]}
    blob = json.dumps({"stage": stage, "style": _spec_version(), "entry": ch, "prereqs": prereqs}, sort_keys=True)
    return hashlib.sha256(blob.encode("utf-8")).hexdigest()


def mark_stale(ch, reason, stages=None, item_stages=None) -> dict:
    """Set passed stages to `stale` and note the reason (TOOLS.md section 2).

    Default stages: `edit` and every later stage. `item_stages` (questions, cards, speak, tasks) are added.
    Stages that depend on a marked stage are marked too. Only a stage with status `pass` changes."""
    entry = common.chapter(ch)
    names = list(stages) if stages is not None else STAGE_NAMES[STAGE_NAMES.index("edit"):]
    names += [s for s in item_stages or [] if s not in names]
    unknown = [n for n in names if n not in STAGE_NAMES]
    if unknown:
        raise ValueError(f"unknown stage {unknown[0]!r}")
    names += _dependents(names)
    path = _ledger_path(entry["id"])
    with common.file_lock(path):
        if not path.exists():
            return {"chapter": entry["id"], "stale": [], "reason": reason}
        led = _load(entry)
        done = _set_stale(led, [n for n in STAGE_NAMES if n in names], reason)
        if reason not in led["stale"]:
            led["stale"].append(reason)
        if not done:
            _event(entry["id"], None, "stale", reason)
        _save(led)
    return {"chapter": entry["id"], "stale": done, "reason": reason}


# ---------------------------------------------------------------- gates owned by the ledger

def _meta_urls() -> set:
    urls = set()
    snap = common.CORPUS / "snap"
    if snap.is_dir():
        for path in snap.rglob("*.meta.json"):
            try:
                url = (common.read_json(path) or {}).get("url")
            except ValueError:
                continue
            if url:
                urls.add(url)
    return urls


def gate_plan(ch_id, quick=False, **options) -> dict:
    ch = common.chapter(ch_id)
    path = _work_dir(ch) / "brief.v0.json"
    name = _rel(path)
    errors, warnings = [], []
    inputs = [path, common.DATA / "book.json"]
    doc, why = _read(path)
    if why or not isinstance(doc, dict):
        return _result("plan", ch["id"], [_finding("B01", f"brief.v0.json {why or 'is not an object'}", name)], [], {}, inputs)
    for key, kind in (("chapter", str), ("sources_fetched", int), ("fetch_failures", list), ("demand", list)):
        if not isinstance(doc.get(key), kind):
            errors.append(_finding("B01", f"brief.v0.json has no valid `{key}`", name))
    demand = [d for d in doc.get("demand") or [] if isinstance(d, dict)] if isinstance(doc.get("demand"), list) else []
    for i, item in enumerate(doc.get("demand") if isinstance(doc.get("demand"), list) else []):
        missing = [k for k in ("id", "bullet", "question", "status", "facts") if not isinstance(item, dict) or k not in item]
        if missing:
            errors.append(_finding("B01", f"demand item {i} lacks {', '.join(missing)}", name))
    have = {d.get("bullet") for d in demand}
    for bullet in ch.get("bullets") or []:
        if bullet not in have:
            errors.append(_finding("B02", f"bullet {bullet} has no demand item", name))
    failures = set()
    for row in doc.get("fetch_failures") if isinstance(doc.get("fetch_failures"), list) else []:
        failures.add(row.get("url") if isinstance(row, dict) else row)
    corpus = _module("corpus")
    metas = None
    urls = []
    for key in ("pages", "faq", "history", "quotas", "pricing"):
        urls += (ch.get("sources") or {}).get(key) or []
    for url in urls:
        if url in failures:
            continue
        found = False
        if corpus is not None:
            try:
                found = corpus.load_meta(corpus.source_id_for(url)) is not None
            except Exception:
                found = False
        if not found:
            metas = _meta_urls() if metas is None else metas
            found = url in metas
        if not found:
            errors.append(_finding("B03", f"source {url} is not in the corpus and not in fetch_failures", name))
    counts = {"demand_items": len(demand), "sources": len(urls), "fetch_failures": len(failures)}
    return _result("plan", ch["id"], errors, warnings, counts, inputs)


def _displays(fact: dict) -> list:
    out = []
    for value in fact.get("values") or []:
        text = common.normalize_text(str(value.get("display", ""))) if isinstance(value, dict) else ""
        if text and text not in out:
            out.append(text)
    return out


def gate_brief(ch_id, quick=False, **options) -> dict:
    ch = common.chapter(ch_id)
    tpl = _template(ch)
    path = _work_dir(ch) / "brief.json"
    name = _rel(path)
    terms_path = common.DATA / "terms.json"
    errors, warnings = [], []
    inputs = [path, common.DATA / "book.json", terms_path]
    doc, why = _read(path)
    if why or not isinstance(doc, dict):
        return _result("brief", ch["id"], [_finding("B01", f"brief.json {why or 'is not an object'}", name)], [], {}, inputs)
    shape = {"sections": ("file", "section", "heading", "bullets", "facts"), "traps": ("id", "belief", "truth", "facts"),
             "question_slots": ("bullet", "concept", "difficulty", "type", "layer", "exam_english"),
             "terms": (), "tasks": (), "diagrams": ("id", "kind", "claim", "alt", "say")}
    if not isinstance(doc.get("chapter"), str):
        errors.append(_finding("B01", "brief.json has no valid `chapter`", name))
    for key, fields in shape.items():
        rows = doc.get(key)
        if not isinstance(rows, list):
            errors.append(_finding("B01", f"brief.json has no list `{key}`", name))
            doc[key] = []
            continue
        for i, row in enumerate(rows):
            missing = [f for f in fields if not isinstance(row, dict) or f not in row]
            if fields and missing:
                errors.append(_finding("B01", f"{key}[{i}] lacks {', '.join(missing)}", name))
    sections = [s for s in doc["sections"] if isinstance(s, dict)]
    traps = [t for t in doc["traps"] if isinstance(t, dict)]
    slots = [s for s in doc["question_slots"] if isinstance(s, dict)]
    in_sections = {b for s in sections for b in (s.get("bullets") if isinstance(s.get("bullets"), list) else [])}
    in_slots = {s.get("bullet") for s in slots}
    need_slot = _applies("questions", tpl)
    for bullet in ch.get("bullets") or []:
        if bullet not in in_sections:
            errors.append(_finding("B02", f"bullet {bullet} maps to no section", name))
        if need_slot and bullet not in in_slots:
            errors.append(_finding("B02", f"bullet {bullet} maps to no question slot", name))
    named = []
    for row in sections + traps:
        for fact_id in row.get("facts") if isinstance(row.get("facts"), list) else []:
            if fact_id not in named:
                named.append(fact_id)
    canon = {row.get("id"): row for row in _fact_rows()}
    for fact_id in named:
        fact = canon.get(fact_id)
        if fact is None:
            errors.append(_finding("B04", "fact is not in the canon", name, item=str(fact_id)))
            continue
        inputs.append(fact["_file"])
        if fact.get("status") != "verified":
            errors.append(_finding("B04", f"fact has status {fact.get('status')}, not verified", name, item=fact_id))
        elif (fact.get("hard") and fact.get("kind") in ("behavior", "capability", "restriction", "default")
              and len(_displays(fact)) < 2):
            warnings.append(_finding("B12", "hard fact has fewer than two displays", name, item=fact_id))
    terms_doc = common.read_json(terms_path) if terms_path.is_file() else {}
    known = set()
    for term in (terms_doc or {}).get("terms") or []:
        known.update(str(term.get(k)) for k in ("id", "term") if term.get(k))
    for term in doc["terms"]:
        if str(term) not in known:
            errors.append(_finding("B11", f"term {term!r} is not in data/terms.json", name))
    counts = {"sections": len(sections), "traps": len(traps), "question_slots": len(slots), "facts": len(named),
              "terms": len(doc["terms"]), "diagrams": len(doc["diagrams"])}
    return _result("brief", ch["id"], errors, warnings, counts, inputs)


def _lenses(tpl: dict) -> list:
    return ["claims", "reader"] + (["exam"] if tpl.get("key") in ("deep", "medium", "pattern") else [])


def _load_findings(ch: dict, tpl: dict):
    """(rows as (lens, file name, finding), errors B05, input paths)."""
    rows, errors, inputs = [], [], []
    for lens in _lenses(tpl):
        path = _work_dir(ch) / "findings" / f"{lens}.json"
        inputs.append(path)
        doc, why = _read(path)
        if not why and not (isinstance(doc, dict) and isinstance(doc.get("findings"), list)):
            why = "has no `findings` list"
        if why:
            errors.append(_finding("B05", f"findings file of lens {lens} {why}", _rel(path)))
            continue
        rows += [(lens, _rel(path), f) for f in doc["findings"]]
    return rows, errors, inputs


def gate_findings(ch_id, quick=False, **options) -> dict:
    ch = common.chapter(ch_id)
    rows, errors, inputs = _load_findings(ch, _template(ch))
    counts = {"findings": len(rows), "blocking": 0, "open": 0}
    for lens, name, row in rows:
        ident = str(row.get("id")) if isinstance(row, dict) and row.get("id") else None
        if not isinstance(row, dict):
            errors.append(_finding("B06", "a finding is not an object", name))
            continue
        missing = [k for k in ("file", "type", "evidence") if not row.get(k)]
        if missing:
            errors.append(_finding("B06", f"finding lacks {', '.join(missing)}", name, item=ident))
        if row.get("severity") not in ("blocking", "should", "note"):
            errors.append(_finding("B06", f"finding has severity {row.get('severity')!r}", name, item=ident))
        if row.get("status") not in ("open", "fixed", "removed", "rejected"):
            errors.append(_finding("B06", f"finding has status {row.get('status')!r}", name, item=ident))
        counts["blocking"] += row.get("severity") == "blocking"
        counts["open"] += row.get("status") == "open"
    return _result("findings", ch["id"], errors, [], counts, inputs)


def gate_findings_closed(ch_id, quick=False, **options) -> dict:
    ch = common.chapter(ch_id)
    rows, errors, inputs = _load_findings(ch, _template(ch))
    counts = {"findings": len(rows), "blocking_open": 0}
    for lens, name, row in rows:
        if not isinstance(row, dict):
            errors.append(_finding("B06", "a finding is not an object", name))
            continue
        # an unreadable severity or status counts as blocking and open: the gate must not pass on a typo
        blocking = row.get("severity") not in ("should", "note")
        is_open = row.get("status") not in ("fixed", "removed", "rejected")
        if blocking and is_open:
            counts["blocking_open"] += 1
            errors.append(_finding("B07", f"blocking finding is open ({lens})", name, item=str(row.get("id") or "?")))
    return _result("findings-closed", ch["id"], errors, [], counts, inputs)


_RE_EMBED = re.compile(r"\]\(\.\./diagrams/svg/([^)\s]+?)\.svg\)")


def gate_diagrams(ch_id, quick=False, **options) -> dict:
    ch = common.chapter(ch_id)
    pipeline = _module("diagram.pipeline")
    if pipeline is None or not hasattr(pipeline, "check_id"):
        raise Unavailable("saalib.diagram.pipeline.check_id")
    errors, warnings, ids = [], [], []
    inputs = []
    for path in _hand_files(ch):
        inputs.append(path)
        for number, line in enumerate(path.read_text(encoding="utf-8").split("\n"), 1):
            for ident in _RE_EMBED.findall(line):
                if ident not in [i for i, _, _ in ids]:
                    ids.append((ident, _rel(path), number))
    for ident, name, number in ids:
        spec, svg = pipeline.spec_path(ident), pipeline.svg_path(ident)
        inputs += [spec, svg]
        if not Path(svg).is_file():
            errors.append(_finding("D02", f"diagram {ident} has no SVG file", name, number))
        if not Path(spec).is_file():
            errors.append(_finding("D01", f"diagram {ident} has no spec in diagrams/src", name, number))
            continue
        for issue in pipeline.check_id(ident).get("issues") or []:
            text = f"diagram {ident}: {issue.get('code')} {issue.get('msg')}"
            if issue.get("level") == "error":
                errors.append(_finding("D03", text, name, number))
            else:
                warnings.append(_finding("D03", text, name, number))
        # gate-break 61: the SVG that the reader sees is the output of the spec that was linted
        if Path(svg).is_file() and hasattr(pipeline, "stale_files"):
            for stale in pipeline.stale_files(ident):
                errors.append(_finding("D04", f"diagram {ident}: {Path(stale).name} is not the output of its spec; "
                                              f"run `diagram build {ident}`", name, number))
    return _result("diagrams", ch["id"], errors, warnings, {"diagrams": len(ids)}, inputs)


def gate_counts(ch_id, quick=False, **options) -> dict:
    ch = common.chapter(ch_id)
    tpl = _template(ch)
    errors, warnings, counts = [], [], {}
    paths, extra = [], {}
    ship = [("verify-questions", "qbank", "gate_questions_verified", {}), ("cards", "qbank", "gate_cards", {"ship": True}),
            ("speak", "qbank", "gate_speak", {"ship": True}), ("tasks", "lab", "gate_tasks", {"ship": True})]
    for stage, mod_name, fn_name, kwargs in ship:
        if not _applies(stage, tpl):
            continue
        fn = getattr(_module(mod_name), fn_name, None)
        if fn is None:
            raise Unavailable(f"saalib.{mod_name}.{fn_name}")
        res = fn(ch["id"], **kwargs)
        errors += list(res.get("errors") or [])
        warnings += list(res.get("warnings") or [])
        if not res.get("ok", False) and not res.get("errors"):
            errors.append(_finding("X01", f"{fn_name} is not ok and names no error"))
        for item in res.get("inputs") or []:
            extra[item["path"]] = item["sha256"]
        counts[fn_name] = len(res.get("errors") or [])
    hand = _hand_files(ch, tpl)
    for path in hand:
        paths.append(path)
        lines = path.read_text(encoding="utf-8").split("\n")
        ok = False
        if lines and lines[0].strip() == "---":
            for line in lines[1:]:
                if line.strip() == "---":
                    break
                if re.match(r"status:\s*\S", line):
                    ok = True
                    break
        if not ok:
            errors.append(_finding("B08", "hand file has no front matter `status` line", _rel(path)))
    requests_path = common.BUILD / "facts" / "requests.jsonl"
    paths += [requests_path, common.STYLE_DIR / "SPEC.json"]
    for row in _open_requests(ch["id"]):
        errors.append(_finding("B09", f"open fact request: {row.get('question', '')}"[:200], item=row.get("id")))
    led = common.read_json(_ledger_path(ch["id"])) or {}
    redo = [n for n, st in (led.get("stages") or {}).items() if n != "finalize" and st.get("status") == "stale"]
    if led.get("stale") and redo:
        errors.append(_finding("B10", f"chapter is stale ({led['stale'][0]}); stages to run again: {', '.join(redo)}"))
    counts.update({"hand_files": len(hand), "open_requests": len(_open_requests(ch["id"])), "stale": len(led.get("stale") or [])})
    result = _result("counts", ch["id"], errors, warnings, counts, paths)
    have = {i["path"] for i in result["inputs"]}
    result["inputs"] += [{"path": p, "sha256": s} for p, s in sorted(extra.items()) if p not in have]
    return result


# ---------------------------------------------------------------- running gates, records

def _bad_record(gate, ch_id, code, msg, exit_code=1) -> dict:
    return {"gate": gate, "chapter": ch_id, "ok": False, "exit": exit_code, "errors": [_finding(code, msg)],
            "warnings": [], "counts": {}, "inputs": []}


def run_gate(ch_id, gate, run=None, **options) -> dict:
    """Run one gate and return its full record (with ts, run, tool_version). Never raises for a bad gate.

    A record with exit 3 and code X03 means "check unavailable"; it is never written to disk."""
    ch = common.chapter(ch_id)
    if gate not in GATE_NAMES:
        raise Precondition(f"unknown gate {gate!r}")
    try:
        if gate in OWN_GATES:
            fn = globals()[OWN_GATES[gate]]
        else:
            mod_name, fn_name = EXTERNAL_GATES[gate]
            fn = getattr(_module(mod_name), fn_name, None)
            if fn is None:
                raise Unavailable(f"saalib.{mod_name}.{fn_name}")
        res = fn(ch["id"], **options)
        if not isinstance(res, dict):
            raise TypeError(f"gate function returned {type(res).__name__}, not a dict")
        errors = list(res.get("errors") or [])
        warnings = list(res.get("warnings") or [])
        if res.get("ok") is not True and not errors:
            errors.append(_finding("X01", "the gate function says not ok and names no error"))
        record = {"gate": gate, "chapter": ch["id"], "ok": not errors, "exit": 1 if errors else (2 if warnings else 0),
                  "errors": errors, "warnings": warnings, "counts": res.get("counts") or {}, "inputs": res.get("inputs") or []}
        if res.get("gate") != gate or res.get("chapter") != ch["id"]:
            record = _bad_record(gate, ch["id"], "X01", f"gate function answered for {res.get('gate')!r} {res.get('chapter')!r}")
    except Unavailable as exc:
        record = _bad_record(gate, ch["id"], "X03", f"check unavailable: {exc} is missing", 3)
    except (Exception, SystemExit) as exc:
        record = _bad_record(gate, ch["id"], "X02", f"gate function failed: {type(exc).__name__}: {exc}"[:300])
    record.update({"ts": common.now_iso(), "run": run, "tool_version": _tool_version()})
    problems = schemas.validate(record, "gate")
    if problems:
        bad = _bad_record(gate, ch["id"], "X01", "gate result is not valid: " + "; ".join(problems[:3])[:300])
        bad.update({"ts": record["ts"], "run": run, "tool_version": record["tool_version"]})
        record = bad
    return record


def _unavailable(record: dict) -> bool:
    return record.get("exit") == 3


def _write_record(record: dict) -> str:
    path = _gate_path(record["chapter"], record["gate"])
    with common.file_lock(path):
        common.write_json(path, record)
    return _rel(path)


def _record_stale(record: dict) -> bool:
    for item in record.get("inputs") or []:
        path = common.BOOK / item["path"]
        if not path.is_file() or common.sha256_file(path) != item["sha256"]:
            return True
    return False


def _run_gates(ch: dict, gates, run=None, draft_lint=False):
    """Run every gate (all of them), write the records. Returns (records, summaries, errors, code)."""
    records, summaries, errors = [], [], []
    for gate in gates:
        options = {"draft": True} if (gate == "lint" and draft_lint) else {}
        record = run_gate(ch["id"], gate, run=run, **options)
        records.append(record)
        where = None if _unavailable(record) else _write_record(record)
        summaries.append({"gate": gate, "ok": record["ok"], "errors": len(record["errors"]),
                          "warnings": len(record["warnings"]), "record": where})
        if not _unavailable(record):
            errors += record["errors"]
    missing = [r for r in records if _unavailable(r)]
    if errors:
        code = common.EXIT_FAIL
    elif missing:
        code = common.EXIT_PRECONDITION
        errors = [e for r in missing for e in r["errors"]]
    elif any(r["warnings"] for r in records):
        code = common.EXIT_WARN
    else:
        code = common.EXIT_OK
    return records, summaries, errors, code


def _finalize_gates(tpl: dict) -> list:
    return [g for g in STAGE_GATES["finalize"] if _gate_applies(g, tpl)]


def _front_status(ch: dict) -> dict:
    """The `status:` value of the front matter of every hand file, by relative path (what `stage end` puts back
    when the gates of a prose, fix or finalize stage fail)."""
    out = {}
    for path in _hand_files(ch):
        lines = path.read_text(encoding="utf-8").split("\n")
        if not lines or lines[0].strip() != "---":
            continue
        for line in lines[1:]:
            if line.strip() == "---":
                break
            if line.startswith("status:"):
                out[_rel(path)] = line[len("status:"):].strip()
                break
    return out


def _write_front_status(ch: dict, value) -> list:
    """Rewrite the one `status:` line of the front matter of every hand file. `value` is one status for every
    file, or a dict of relative path to status (the previous values of `_front_status`). Returns the files changed."""
    changed = []
    for path in _hand_files(ch):
        want = value.get(_rel(path)) if isinstance(value, dict) else value
        if want is None:
            continue
        lines = path.read_text(encoding="utf-8").split("\n")
        if not lines or lines[0].strip() != "---":
            continue
        for i in range(1, len(lines)):
            if lines[i].strip() == "---":
                break
            if lines[i].startswith("status:"):
                if lines[i] != f"status: {want}":
                    lines[i] = f"status: {want}"
                    tmp = path.with_name(path.name + f".tmp{os.getpid()}")
                    tmp.write_text("\n".join(lines), encoding="utf-8")
                    os.replace(tmp, path)
                    changed.append(_rel(path))
                break
    return changed


# ---------------------------------------------------------------- stage begin / end / reset

def _check_stage(stage: str) -> None:
    if stage not in STAGE_NAMES:
        raise Precondition(f"unknown stage {stage!r} (stages: {', '.join(STAGE_NAMES)})")


def stage_begin(ch_id, stage, run=None):
    """Returns (exit code, result). TOOLS.md 3.2."""
    ch = common.chapter(ch_id)
    _check_stage(stage)
    tpl = _template(ch)
    path = _ledger_path(ch["id"])
    with common.file_lock(path):
        led = _load(ch)
        st = led["stages"].get(stage)
        status = st.get("status") if st else None
        attempt = st.get("attempts", 0) if st else 0
        write = False
        blocked_on = next((p for p in PREREQS[stage] if _eff_status(led, p, tpl) not in ("pass", "na")), None)
        if not _applies(stage, tpl):
            decision, reason = "SKIP", "not-applicable"
            if status != "na":
                new = _blank_stage()
                new.update({"status": "na", "pass_seq": (st or {}).get("pass_seq", 0), "reason": "not-applicable"})
                led["stages"][stage] = new
                write = True
            attempt = 0
        elif blocked_on:
            decision, reason = "BLOCKED", f"prereq:{blocked_on}"
        else:
            current = _inputs_hash(ch, stage, led)
            if status == "pass" and st.get("inputs_hash") == current:
                decision, reason = "SKIP", "already-passed"
            elif status != "pass" and attempt >= MAX_ATTEMPTS:
                decision, reason = "BLOCKED", "attempts"
                if not led.get("blocked"):
                    led["blocked"] = {"stage": stage, "reason": (st.get("reason") or "three attempts failed")[:300],
                                      "since": common.now_iso()}
                    _event(ch["id"], stage, "block", led["blocked"]["reason"], run)
                    write = True
            else:
                decision = "GO"
                reason = ("first" if status in (None, "na") else "retry" if status in ("fail", "running")
                          else "stale" if status == "stale" else "inputs-changed")
                attempt = 1 if status in ("pass", "stale", "na", None) else attempt + 1
                new = _blank_stage()
                new.update(st or {})
                new.update({"status": "running", "attempts": attempt, "inputs_hash": current, "started": common.now_iso(),
                            "ended": None, "run": run, "reason": None})
                led["stages"][stage] = new
                led["style_version"] = _spec_version()
                write = True
        _event(ch["id"], stage, "begin", f"{decision} attempt {attempt} {reason}", run)
        if write:
            _save(led, run)
    code = common.EXIT_PRECONDITION if decision == "BLOCKED" else common.EXIT_OK
    return code, {"decision": decision, "chapter": ch["id"], "stage": stage, "attempt": attempt, "reason": reason}


def _block_if_spent(led: dict, stage: str, st: dict, run) -> None:
    if st["attempts"] >= MAX_ATTEMPTS and not led.get("blocked"):
        led["blocked"] = {"stage": stage, "reason": (st.get("reason") or "failed")[:300], "since": common.now_iso()}
        _event(led["chapter"], stage, "block", led["blocked"]["reason"], run)


def stage_end(ch_id, stage, counts=None, note=None, fail=None, run=None):
    """Returns (exit code, result). TOOLS.md 3.3."""
    ch = common.chapter(ch_id)
    _check_stage(stage)
    tpl = _template(ch)
    path = _ledger_path(ch["id"])

    def running(led):
        st = led["stages"].get(stage)
        if not st or st.get("status") != "running":
            raise Precondition(f"stage {stage} of chapter {ch['id']} is not running "
                               f"(status {st.get('status') if st else 'none'}); run `stage begin` first")
        return st

    with common.file_lock(path):
        led = _load(ch)
        st = running(led)
        run = run or st.get("run")
        if fail:
            st.update({"status": "fail", "reason": str(fail)[:300], "ended": common.now_iso(), "note": note})
            _block_if_spent(led, stage, st, run)
            _event(ch["id"], stage, "end", f"FAIL {fail}"[:300], run)
            _save(led, run)
            return common.EXIT_FAIL, {"result": "FAIL", "chapter": ch["id"], "stage": stage, "status": led["status"],
                                      "gates": [], "errors": [_finding("B00", str(fail)[:300] or "failed")]}

    # the gates run without the ledger lock: a gate can call mark_stale
    previous = {}
    if stage in FRONT_STATUS:
        previous = _front_status(ch)
        _write_front_status(ch, FRONT_STATUS[stage])
    gates = [g for g in STAGE_GATES[stage] if stage != "finalize" or _gate_applies(g, tpl)]
    records, summaries, errors, code = _run_gates(ch, gates, run=run, draft_lint=(stage == "prose"))
    if previous and code in (common.EXIT_FAIL, common.EXIT_PRECONDITION):
        _write_front_status(ch, previous)       # the gates did not pass: the hand files keep their previous status

    with common.file_lock(path):
        led = _load(ch)
        st = running(led)
        st["gates"] = gates
        if code == common.EXIT_PRECONDITION:
            # a check is missing: nothing passes and no attempt is used
            st["attempts"] = max(0, st["attempts"] - 1)
            st["reason"] = _fmt(errors[0])[:300]
            result = "UNAVAILABLE"
        elif code == common.EXIT_FAIL:
            st.update({"status": "fail", "reason": _fmt(errors[0])[:300], "ended": common.now_iso(), "note": note})
            _block_if_spent(led, stage, st, run)
            result = "FAIL"
        else:
            st.update({"status": "pass", "attempts": 0, "pass_seq": st.get("pass_seq", 0) + 1, "ended": common.now_iso(),
                       "counts": counts or {}, "reason": None, "note": note})
            for record in records:
                prefix = f"{record['gate']}: "
                led["warnings"] = [w for w in led["warnings"] if not w.startswith(prefix)]
                led["warnings"] += [f"{prefix}{w.get('code')} {w.get('msg')}" for w in record["warnings"]]
            _set_stale(led, _dependents([stage]), f"prerequisite {stage} passed again", run)
            if stage == "finalize":
                led["rev"] = led.get("rev", 0) + 1
                led["style_version"] = _spec_version()
                led["stale"] = []
            result = "PASS"
        detail = result if result == "PASS" else f"{result} {errors[0].get('code')}"
        _event(ch["id"], stage, "end", detail, run)
        _save(led, run)
    return code, {"result": result, "chapter": ch["id"], "stage": stage, "status": led["status"],
                  "gates": summaries, "errors": errors[:20]}


def stage_reset(ch_id, stage, reason, by="unknown"):
    """`stage` is a stage name or None for all. Returns (exit code, result)."""
    ch = common.chapter(ch_id)
    if stage is not None:
        _check_stage(stage)
    path = _ledger_path(ch["id"])
    with common.file_lock(path):
        if not path.exists():
            raise Precondition(f"chapter {ch['id']} has no ledger file")
        led = _load(ch)
        names = [stage] if stage else [n for n in STAGE_NAMES if n in led["stages"]]
        done = []
        for name in names:
            st = led["stages"].get(name)
            if not st:
                continue
            st["attempts"] = 0
            done.append(name)
            _event(ch["id"], name, "reset", f"{reason} (by {by})")
        text = f"reset: {reason}"
        _set_stale(led, [n for n in STAGE_NAMES if n in names or n in _dependents(names)], text)
        if led.get("blocked") and (stage is None or led["blocked"].get("stage") == stage):
            led["blocked"] = None
        _save(led)
    return common.EXIT_OK, {"chapter": ch["id"], "reset": done, "status": led["status"], "reason": reason}


# ---------------------------------------------------------------- gate command

def gate_chapter(ch_id, gate=None, run=None):
    ch = common.chapter(ch_id)
    if gate is not None and gate not in GATE_NAMES:
        raise Precondition(f"unknown gate {gate!r} (gates: {', '.join(GATE_NAMES)})")
    gates = [gate] if gate else _finalize_gates(_template(ch))
    records, summaries, errors, code = _run_gates(ch, gates, run=run)
    result = {common.EXIT_FAIL: "FAIL", common.EXIT_PRECONDITION: "UNAVAILABLE"}.get(code, "PASS")
    return code, {"result": result, "chapter": ch["id"], "gates": summaries, "errors": errors[:20]}


def gate_all(quick=False, run=None):
    rows = []
    for ch in common.chapters():
        led = common.read_json(_ledger_path(ch["id"]))
        if not led or led.get("status") not in LIVE_STATUSES:
            continue
        tpl = _template(ch)
        stale, failed, missing, unavailable = [], [], [], []
        for gate in _finalize_gates(tpl):
            if quick and gate != "sync":
                record = common.read_json(_gate_path(ch["id"], gate))
                if record is None:
                    missing.append(gate)
                elif _record_stale(record):
                    stale.append(gate)
                elif not record.get("ok"):
                    failed.append(gate)
                continue
            record = run_gate(ch["id"], gate, run=run)
            if _unavailable(record):
                unavailable.append(gate)
                continue
            _write_record(record)
            if not record["ok"]:
                failed.append(gate)
        result = "fail" if failed else "stale" if stale else "no-record" if (missing or unavailable) else "ok"
        rows.append({"id": ch["id"], "status": led["status"], "result": result, "stale_gates": stale,
                     "failed_gates": failed, "missing_gates": missing, "unavailable_gates": unavailable})
    results = {r["result"] for r in rows}
    code = (common.EXIT_FAIL if "fail" in results
            else common.EXIT_PRECONDITION if results & {"stale", "no-record"} else common.EXIT_OK)
    return code, {"chapters": rows}


# ---------------------------------------------------------------- status, report

def _wave_name(text) -> str:
    text = str(text).strip()
    return text.upper() if text[:1] in "wW" else f"W{text}"


def _next_stage(led: dict, tpl: dict):
    for name in RUN_ORDER:
        if _eff_status(led, name, tpl) not in ("pass", "na"):
            return name
    return None


def chapter_rows(wave=None) -> list:
    facts = {}
    for row in _fact_rows():
        if row.get("status") in ("rejected", "superseded"):
            continue
        tally = facts.setdefault(str(row.get("home_chapter")), {"verified": 0, "total": 0})
        tally["total"] += 1
        tally["verified"] += row.get("status") == "verified"
    rows = []
    for ch in common.chapters():
        if wave and _wave_name(ch.get("wave", "")) != wave:
            continue
        tpl = _template(ch)
        led = _load(ch)
        if not _ledger_path(ch["id"]).exists():
            led["status"] = "planned"
        target = (tpl.get("counts") or {}).get("questions", {}).get("shipped", 0)
        ready = sum(1 for q in _items(ch, "questions") if q.get("status") == "ready")
        rows.append({"id": ch["id"], "slug": ch["slug"], "tier": ch.get("tier"), "wave": ch.get("wave"),
                     "status": led["status"], "next_stage": _next_stage(led, tpl), "blocked": led.get("blocked"),
                     "facts": facts.get(ch["id"], {"verified": 0, "total": 0}),
                     "questions": {"ready": ready, "target": target},
                     "warnings": len(led.get("warnings") or []), "stale": len(led.get("stale") or [])})
    return rows


def status_report(wave=None) -> dict:
    rows = chapter_rows(_wave_name(wave) if wave else None)
    totals = {}
    for row in rows:
        totals[row["status"]] = totals.get(row["status"], 0) + 1
    return {"totals": totals, "chapters": rows}


def _status_line(row: dict) -> str:
    return (f"{row['id']} {row['slug']} {row['tier']} {row['wave']} {row['status']} next={row['next_stage'] or '-'} "
            f"facts={row['facts']['verified']}/{row['facts']['total']} "
            f"q={row['questions']['ready']}/{row['questions']['target']} warn={row['warnings']} stale={row['stale']}")


def wave_report(wave) -> dict:
    wave = _wave_name(wave)
    rows = chapter_rows(wave)
    if not rows:
        raise Precondition(f"unknown wave {wave!r}")
    by_id = {c["id"]: c for c in common.chapters()}
    counts = {"facts": sum(r["facts"]["verified"] for r in rows)}
    for kind in ("questions", "cards", "speak", "tasks"):
        counts[kind] = sum(1 for r in rows for i in _items(by_id[r["id"]], kind) if i.get("status") == "ready")
    path = common.REPORTS / f"wave-{wave}.json"
    report = {
        "wave": wave,
        "ready": [r["id"] for r in rows if r["status"] == "ready"],
        "blocked": [{"id": r["id"], "stage": (r["blocked"] or {}).get("stage"), "reason": (r["blocked"] or {}).get("reason")}
                    for r in rows if r["status"] == "blocked"],
        "in_progress": [{"id": r["id"], "status": r["status"], "next_stage": r["next_stage"]}
                        for r in rows if r["status"] not in ("ready", "blocked")],
        "counts": counts,
        "warnings": sum(r["warnings"] for r in rows),
        "open_requests": sum(len(_open_requests(r["id"])) for r in rows),
        "report": _rel(path),
    }
    with common.file_lock(path):
        common.write_json(path, report)
    return report


# ---------------------------------------------------------------- selftest

def _walk(suite):
    for test in suite:
        if isinstance(test, unittest.TestSuite):
            yield from _walk(test)
        else:
            yield test


def _test_module(test) -> str:
    name = type(test).__module__
    if name.startswith("unittest"):            # a test file that did not import
        name = getattr(test, "_testMethodName", name)
    stem = name.split(".")[-1]
    stem = stem[5:] if stem.startswith("test_") else stem
    for known in sorted(SELFTEST_REQUIRED, key=len, reverse=True):
        if stem == known or stem.startswith(known + "_"):
            return known
    return stem


def selftest(tests_dir=None, pattern="test_*.py", required=None):
    """Run the unit tests in-process (as tests/run.py does) and report per module. Returns (exit code, result)."""
    tests_dir = Path(tests_dir or common.TESTS)
    required = SELFTEST_REQUIRED if required is None else required
    added = [p for p in (str(common.TOOLS), str(tests_dir)) if p not in sys.path]
    for p in added:
        sys.path.insert(0, p)
    try:
        suite = unittest.TestLoader().discover(str(tests_dir), pattern=pattern, top_level_dir=str(tests_dir))
        modules = {}
        for test in _walk(suite):
            row = modules.setdefault(_test_module(test), {"tests": 0, "failures": 0, "errors": 0, "must_fail": 0})
            row["tests"] += 1
            row["must_fail"] += getattr(test, "_testMethodName", "").startswith("test_must_fail_")
        sink = io.StringIO()
        with contextlib.redirect_stdout(sink), contextlib.redirect_stderr(sink):
            outcome = unittest.TextTestRunner(stream=io.StringIO(), verbosity=0).run(suite)
    finally:
        for p in added:
            if p in sys.path:
                sys.path.remove(p)
    failed = []
    for kind, pairs in (("failures", outcome.failures), ("errors", outcome.errors)):
        for test, _ in pairs:
            key = _test_module(test)
            if key in modules:
                modules[key][kind] += 1
            failed.append(test.id() if hasattr(test, "id") else str(test))
    must_fail = {name: row["must_fail"] for name, row in sorted(modules.items())}
    for name in required:
        must_fail.setdefault(name, 0)
    missing = [name for name in required if not must_fail.get(name)]
    result = {"tests": outcome.testsRun, "failures": len(outcome.failures), "errors": len(outcome.errors),
              "must_fail": must_fail, "modules": dict(sorted(modules.items())),
              "missing_must_fail": missing, "failed": failed[:20]}
    ok = outcome.wasSuccessful() and outcome.testsRun > 0 and not missing
    return (common.EXIT_OK if ok else common.EXIT_FAIL), result


# ---------------------------------------------------------------- command functions

def _guard(fn):
    def wrapped(args):
        try:
            return fn(args)
        except Precondition as exc:
            return common.fail(str(exc), common.EXIT_PRECONDITION)
    return wrapped


def _text(args, summary: str, lines=()) -> None:
    lines = list(lines)
    if len(lines) > 40 and not getattr(args, "out", None):
        lines = lines[:39] + [f"... ({len(lines) - 39} more; use --json or --out FILE)"]
    common.emit("\n".join([summary] + lines), args)


def _parse_counts(pairs) -> dict:
    out = {}
    for pair in pairs or []:
        if "=" not in pair:
            raise Precondition(f"--counts needs k=v, got {pair!r}")
        key, value = pair.split("=", 1)
        try:
            out[key] = int(value)
        except ValueError:
            out[key] = value
    return out


def _gate_bits(summaries) -> str:
    return ",".join(f"{g['gate']}:{'ok' if g['ok'] else 'no record' if g['record'] is None else 'FAIL'}"
                    f"({g['errors']}e/{g['warnings']}w)" for g in summaries)


@_guard
def cmd_stage(args) -> int:
    action = getattr(args, "action", None)
    if action == "begin":
        code, res = stage_begin(args.chapter, args.stage, run=args.run)
        if args.json:
            common.emit(res, args)
        else:
            common.emit(f"{res['decision']} {res['chapter']} {res['stage']} attempt={res['attempt']} reason={res['reason']}", args)
        return code
    if action == "end":
        code, res = stage_end(args.chapter, args.stage, counts=_parse_counts(args.counts), note=args.note,
                              fail=args.fail, run=args.run)
        if args.json:
            common.emit(res, args)
        else:
            _text(args, f"{res['result']} {res['chapter']} {res['stage']} status={res['status']} gates={_gate_bits(res['gates'])}",
                  [_fmt(f) for f in res["errors"]])
        return code
    if action == "reset":
        if bool(args.stage) == bool(args.all):
            raise Precondition("stage reset needs a stage name or --all (not both)")
        code, res = stage_reset(args.chapter, None if args.all else args.stage, args.reason,
                                by=args.by or os.environ.get("SAA_AGENT") or "unknown")
        common.emit(res if args.json else f"RESET {res['chapter']} {','.join(res['reset']) or '-'} status={res['status']}", args)
        return code
    if action == "show":
        ch = common.chapter(args.chapter)
        if not _ledger_path(ch["id"]).exists():
            raise Precondition(f"chapter {ch['id']} has no ledger file (status planned)")
        common.emit(_load(ch), args)
        return common.EXIT_OK
    raise Precondition("stage needs one of: begin, end, reset, show")


@_guard
def cmd_gate(args) -> int:
    if args.all:
        code, res = gate_all(quick=args.quick, run=args.run)
        if args.json:
            common.emit(res, args)
        else:
            tally = {}
            for row in res["chapters"]:
                tally[row["result"]] = tally.get(row["result"], 0) + 1
            rank = {"fail": 0, "stale": 1, "no-record": 2, "ok": 3}
            lines = [f"{r['id']} {r['status']} {r['result']}"
                     + "".join(f" {k.split('_')[0]}={','.join(r[k])}" for k in
                               ("failed_gates", "stale_gates", "missing_gates", "unavailable_gates") if r[k])
                     for r in sorted(res["chapters"], key=lambda r: (rank[r["result"]], r["id"]))]
            _text(args, f"gate --all{' --quick' if args.quick else ''}: {len(res['chapters'])} chapters "
                  + " ".join(f"{k}={v}" for k, v in sorted(tally.items())), lines)
        return code
    if not args.chapter:
        raise Precondition("gate needs a chapter or --all")
    code, res = gate_chapter(args.chapter, gate=args.gate, run=args.run)
    if args.json:
        common.emit(res, args)
    else:
        _text(args, f"{res['result']} {res['chapter']} gates={_gate_bits(res['gates'])}", [_fmt(f) for f in res["errors"]])
    return code


@_guard
def cmd_status(args) -> int:
    res = status_report(args.wave)
    if args.json:
        common.emit(res, args)
        return common.EXIT_OK
    rank = {"blocked": 0, "planned": 3, "ready": 2}
    rows = sorted(res["chapters"], key=lambda r: (rank.get(r["status"], 1), r["id"]))
    _text(args, f"{len(rows)} chapters: " + " ".join(f"{k}={v}" for k, v in sorted(res["totals"].items())),
          [_status_line(r) for r in rows])
    return common.EXIT_OK


@_guard
def cmd_report(args) -> int:
    if getattr(args, "what", None) != "wave":
        raise Precondition("report needs: wave W")
    res = wave_report(args.wave)
    if args.json:
        common.emit(res, args)
        return common.EXIT_OK
    lines = [f"ready: {', '.join(res['ready']) or '-'}"]
    lines += [f"blocked: {b['id']} {b['stage']} {b['reason']}" for b in res["blocked"]]
    lines += [f"in progress: {p['id']} {p['status']} next={p['next_stage'] or '-'}" for p in res["in_progress"]]
    lines.append("counts: " + " ".join(f"{k}={v}" for k, v in res["counts"].items()))
    lines.append(f"warnings={res['warnings']} open_requests={res['open_requests']}")
    lines.append(f"report: {res['report']}")
    if len(lines) > 49:
        lines = lines[:48] + [f"... ({len(lines) - 48} more lines in the report file)"]
    common.emit("\n".join([f"wave {res['wave']}: {len(res['ready'])} ready, {len(res['blocked'])} blocked, "
                           f"{len(res['in_progress'])} in progress"] + lines), args)
    return common.EXIT_OK


@_guard
def cmd_selftest(args) -> int:
    code, res = selftest(pattern=f"test_{args.module}*.py" if args.module else "test_*.py",
                         required=[] if args.module else None)
    if args.json:
        common.emit(res, args)
        return code
    lines = [f"{name}: tests={row['tests']} failures={row['failures']} errors={row['errors']} must_fail={row['must_fail']}"
             for name, row in res["modules"].items()]
    lines = [f"no must-fail test: {name}" for name in res["missing_must_fail"]] + [f"failed: {t}" for t in res["failed"]] + lines
    _text(args, f"selftest {'ok' if code == 0 else 'FAILED'}: tests={res['tests']} failures={res['failures']} "
          f"errors={res['errors']} modules without a must-fail test={len(res['missing_must_fail'])}", lines)
    return code


def register(subparsers) -> None:
    stage = subparsers.add_parser("stage", help="begin, end, reset or show a pipeline stage of a chapter")
    stage.set_defaults(func=cmd_stage)
    actions = stage.add_subparsers(dest="action")
    begin = actions.add_parser("begin", help="GO, SKIP or BLOCKED for one stage")
    begin.add_argument("chapter")
    begin.add_argument("stage")
    end = actions.add_parser("end", help="run the gates of a running stage and record pass or fail")
    end.add_argument("chapter")
    end.add_argument("stage")
    end.add_argument("--counts", nargs="*", default=[], metavar="K=V")
    end.add_argument("--note")
    end.add_argument("--fail", metavar="REASON", help="record a failure without running gates")
    reset = actions.add_parser("reset", help="orchestrator only: attempts to 0, pass to stale, blocked cleared")
    reset.add_argument("chapter")
    reset.add_argument("stage", nargs="?")
    reset.add_argument("--all", action="store_true")
    reset.add_argument("--reason", required=True)
    show = actions.add_parser("show", help="print the ledger file of a chapter")
    show.add_argument("chapter")
    for parser in (begin, end, reset, show):
        parser.add_argument("--run", help="workflow run id")
        parser.add_argument("--by", help="who runs this (default: SAA_AGENT)")
        common.add_common_args(parser)
        parser.set_defaults(func=cmd_stage)

    gate = subparsers.add_parser("gate", help="run the finalize gates of a chapter (or one gate), or check all chapters")
    gate.add_argument("chapter", nargs="?")
    gate.add_argument("--gate", help="one gate name")
    gate.add_argument("--all", action="store_true", help="every chapter that is drafted, reviewed or ready")
    gate.add_argument("--quick", action="store_true", help="with --all: compare stored records with file hashes; run only sync")
    gate.add_argument("--run", help="workflow run id")
    common.add_common_args(gate)
    gate.set_defaults(func=cmd_gate)

    status = subparsers.add_parser("status", help="one line per chapter")
    status.add_argument("--wave")
    common.add_common_args(status)
    status.set_defaults(func=cmd_status)

    report = subparsers.add_parser("report", help="report wave W: write _build/reports/wave-<W>.json")
    report.set_defaults(func=cmd_report)
    what = report.add_subparsers(dest="what")
    wave = what.add_parser("wave")
    wave.add_argument("wave")
    common.add_common_args(wave)
    wave.set_defaults(func=cmd_report)

    self_test = subparsers.add_parser("selftest", help="run the unit tests and count the must-fail tests per module")
    self_test.add_argument("module", nargs="?", help="only tests/test_<module>*.py")
    common.add_common_args(self_test)
    self_test.set_defaults(func=cmd_selftest)
