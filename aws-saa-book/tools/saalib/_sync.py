"""Generators behind `sync` (TOOLS-items.md 6.2). Loaded by saalib/lint.py; no subcommand of its own.

Every output is deterministic: no timestamps, items in file order, `\n` line ends, one blank line between blocks.
"""
from __future__ import annotations

import os
import re
from pathlib import Path

from saalib import common

KINDS = ("do", "say", "quiz", "sources", "tasks", "plan", "facts", "glossary", "exam-english", "sheet")
_SCHEMAS = {"questions": "question", "cards": "card", "speak": "speak", "tasks": "task"}
_RE_FACT_LINK = re.compile(r"\]\(\.\./facts/([a-z0-9-]+)\.md#([a-z0-9-]+)\)")


def _lint():
    from saalib import lint
    return lint


def _dirname(entry) -> str:
    return f"{entry['id']}-{entry['slug']}"


def _doc(entry, kind):
    return common.read_json(common.DATA / _dirname(entry) / f"{kind}.json")


def _items(entry, kind) -> list:
    return [i for i in (_doc(entry, kind) or {}).get("items", []) if isinstance(i, dict)]


def _join(blocks) -> str:
    return "\n\n".join(b.rstrip("\n") for b in blocks if b is not None and b != "") + "\n"


def _marker(sp) -> str:
    return sp["generated_regions"]["generated_file_first_line"]


def _end(text: str) -> str:
    text = text.strip()
    return text if text.endswith((".", "?", "!")) else text + "."


def _review(entry, section, cache) -> str:
    """`**Review.**` link for an item's section: <file>#<anchor>, or ../<NN-slug>/<file>#<anchor>."""
    if not section:
        return ""
    target, _, sid = section.partition("#")
    parts = target.split("/")
    other = None
    if len(parts) == 2:
        try:
            other = common.chapter(parts[0])
        except SystemExit:
            return section
        name = parts[1]
    else:
        name = parts[0]
    owner = other or entry
    key = owner["id"]
    if key not in cache:
        cache[key] = _lint().sections(owner)
    row = cache[key].get(name, {}).get(sid)
    if not row or not row.get("anchor"):
        return section
    prefix = f"../{_dirname(owner)}/" if other and other["id"] != entry["id"] else ""
    return f"[{row['heading']}]({prefix}{name}#{row['anchor']})"


# ---------------------------------------------------------------- 5-quiz.md

def _shippable(sp, q) -> bool:
    need = sp.get("questions", {}).get("ship_requires", {})
    return q.get("status") == need.get("status", "ready") and \
        (q.get("verification") or {}).get("status") in need.get("verification_status", ["pass", "edited-pass"])


def _question(entry, q, n, cache) -> str:
    correct = [o for o in q.get("options", []) if o.get("correct")]
    wrong = [o for o in q.get("options", []) if not o.get("correct")]
    blocks = [f"<!-- quiz:start id={q['id']} -->\n### Question {n}", q.get("stem", ""),
              "\n".join(f"- {o['text']}" for o in q.get("options", [])), "<details>\n<summary>Answer</summary>"]
    if len(correct) == 1:
        blocks.append(f"**Answer.** {correct[0]['text']}")
    else:
        blocks += ["**Answer.**", "\n".join(f"- {o['text']}" for o in correct)]
    if q.get("keywords"):
        blocks.append("**Deciding phrases.** " + ", ".join(f'"{k}"' for k in q["keywords"]))
    worked = q.get("worked") or {}
    if worked.get("steps"):
        blocks += ["**Think aloud.**", "\n".join(f"{i}. {s}" for i, s in enumerate(worked["steps"], 1))]
    blocks.append(f"**Why.** {q.get('explanation', '')}")
    if q.get("type") == "multi":
        blocks.append("\n".join(f"- {o.get('why', '')}" for o in correct))
    if wrong:
        rows = []
        for o in wrong:
            words = o["text"].split()
            head = " ".join(words[:8]) + (" ..." if len(words) > 8 else "")
            rows.append(f'- "{head}": {o.get("why", "")}')
        blocks += ["**Why not.**", "\n".join(rows)]
    if q.get("twin"):
        blocks.append(f"**Twin.** {q['twin']}")
    if q.get("takeaway"):
        blocks.append(f"**Takeaway.** {q['takeaway']}")
    review = _review(entry, q.get("section"), cache)
    if review:
        blocks.append(f"**Review.** {review}")
    blocks.append("</details>\n<!-- quiz:end -->")
    return _join(blocks).rstrip("\n")


def gen_quiz(entry, sp) -> str:
    items = [q for q in _items(entry, "questions") if _shippable(sp, q) and q.get("pool") != "drill"]
    blocks, cache, n = [_marker(sp) + f"\n# {entry['title']}: questions"], {}, 0
    mock = common.read_json(common.DATA / _dirname(entry) / "mock.json")
    groups = []
    if isinstance(mock, dict) and mock.get("questions"):
        by_id = {q["id"]: q for q in items}
        groups.append(("Questions", [by_id[i] for i in mock["questions"] if i in by_id]))
    else:
        worked = [q for q in items if q.get("worked")]
        rest = [q for q in items if not q.get("worked")]
        groups = [("Worked examples", worked), ("Core", [q for q in rest if q.get("layer") == "core"]),
                  ("Extended", [q for q in rest if q.get("layer") != "core"])]
    for title, group in groups:
        if not group:
            continue
        blocks.append(f"## {title}")
        for q in group:
            n += 1
            blocks.append(_question(entry, q, n, cache))
    if n == 0:
        blocks.append("Nothing here yet.")
    return _join(blocks)


# ---------------------------------------------------------------- 4-say.md

def _speak(item, n) -> str:
    blocks = [f"<!-- speak:start id={item['id']} -->\n### Prompt {n}", f"**A customer asks.** {item.get('prompt', '')}",
              "<details>\n<summary>Answer</summary>", f"**In 10 seconds.** {item.get('ten_second', '')}", "**In 60 seconds.**"]
    blocks += list(item.get("sixty_second", []))
    blocks.append("**Skeleton.** " + " / ".join(item.get("skeleton", [])))
    must = [k for k in item.get("key_points", []) if k.get("kind") == "must"]
    if must:
        blocks += ["**Must say.**", "\n".join(f"- {k['point']}" for k in must)]
    if item.get("must_not_say"):
        blocks += ["**Do not say.**", "\n".join(f"- \"{x['error']}\". Say: {x['correct']}" for x in item["must_not_say"])]
    if item.get("follow_ups"):
        blocks += ["**Follow-up questions.**", "\n".join(f"- {x['question']} {x['answer']}" for x in item["follow_ups"])]
    blocks.append("</details>\n<!-- speak:end -->")
    return _join(blocks).rstrip("\n")


def gen_say(entry, sp, fs) -> str:
    items = [i for i in _items(entry, "speak") if i.get("status") == "ready"]
    if any("pack" in str(src) for src in fs.get("from", [])):
        for other in common.chapters():
            if other["id"] != entry["id"]:
                items += [i for i in _items(other, "speak") if i.get("status") == "ready" and i.get("pack")]
    blocks = [_marker(sp) + f"\n# {entry['title']}: say it"]
    blocks += [_speak(item, n) for n, item in enumerate(items, 1)]
    if not items:
        blocks.append("Nothing here yet.")
    return _join(blocks)


# ---------------------------------------------------------------- tasks: 3-do.md and task regions

def _fence(command, indent="") -> str:
    return f"{indent}```bash\n{indent}{command}\n{indent}```"


def task_body(task, sp) -> str:
    kind = task.get("type", "try")
    look = kind == "look"
    blocks = [kind.capitalize(), f"**It kills the belief.** {task.get('kills', '')}"]
    cost = f"> **Cost:** {_end(task.get('cost', ''))}"
    if not look:
        cost += f" If you forget the cleanup: {_end(task.get('cost_if_forgotten', ''))}"
    blocks.append(cost)
    if task.get("permissions"):
        blocks.append("**Permissions.** " + ", ".join(f"`{p}`" for p in task["permissions"]))
    if task.get("read_only_alternative"):
        blocks.append(f"**No permission to create resources?** {task['read_only_alternative']}")
    if kind == "lab" and task.get("template"):
        blocks.append(f"**Template.** `{task['template']}`")
    steps = []
    for n, step in enumerate(task.get("steps", []), 1):
        parts = []
        if step.get("break_it") and step.get("predict"):
            parts.append(f"**Predict.** {step['predict']}")
        parts.append(step.get("text", ""))
        command = step.get("command")
        if command:
            cap = step.get("capture")
            if cap:
                command = f"{cap['name']}=$({command} --query {cap['query']} --output text)"
            parts.append(_fence(command, "   "))
        if step.get("expect"):
            parts.append(f"Expect: {step['expect']}")
        if step.get("break_it") and step.get("explain"):
            parts.append(f"**Why.** {step['explain']}")
        lines = []
        for k, part in enumerate(parts):
            if part.startswith("   ```"):
                lines.append(part)
            else:
                lines.append((f"{n}. " if k == 0 else "   ") + part)
        steps.append("\n\n".join(lines))
    blocks.append("\n\n".join(steps))
    if not look:
        if task.get("cleanup"):
            blocks.append("> **Clean up:** Run these steps in this order.")
            rows = []
            for n, step in enumerate(task["cleanup"], 1):
                row = f"{n}. {step.get('text', '')}"
                if step.get("command"):
                    row += "\n\n" + _fence(step["command"], "   ")
                rows.append(row)
            blocks.append("\n\n".join(rows))
        verify = task.get("verify")
        if verify:
            blocks += ["**Verify.**", _fence(verify["command"]), f"Expect: {verify['expect']}"]
        if task.get("still_costs"):
            blocks += ["**Still costs money if left.**", "\n".join(f"- {x}" for x in task["still_costs"])]
        blocks.append(f"> **Careful:** {sp['tasks']['stop_rule']}")
    blocks.append(f"**Label.** {task.get('label', sp['tasks']['label'])}. Checked {task.get('checked', '')}.")
    return _join(blocks).rstrip("\n")


def gen_do(entry, sp) -> str:
    tasks = [t for t in _items(entry, "tasks") if t.get("status") == "ready"]
    blocks = [_marker(sp) + f"\n# {entry['title']}: do it"]
    for t in tasks:
        blocks.append(f"## {t['title']} ({t['minutes']} min)")
        blocks.append(f"<!-- task:start id={t['id']} -->")
        blocks.append(task_body(t, sp))
        blocks.append("<!-- task:end -->")
    if not tasks:
        blocks.append("Nothing here yet.")
    return _join(blocks)


# ---------------------------------------------------------------- regions in hand files

def _plan_table(plan_id) -> str:
    data = common.read_json(common.DATA / "plan.json") or {}
    plan = next((p for p in data.get("plans", []) if p.get("id") == plan_id), None)
    if plan is None:
        return None
    rows = ["<!-- table: plan -->", "| Day | Minutes | Work |", "|---|---|---|"]
    for day in plan.get("days", []):
        number = int(re.sub(r"\D", "", day["id"]) or 0)
        rows.append(f"| Day {number} | {day.get('minutes', 0)} | " + "; ".join(t["text"] for t in day.get("tasks", [])) + " |")
    return "\n".join(rows)


def _ee_table(group_id, kind="exam-english") -> str:
    data = common.read_json(common.DATA / "exam-english.json") or {}
    group = next((g for g in data.get("groups", []) if g.get("id") == group_id), None)
    if group is None:
        return None
    rows = [f"<!-- table: {kind} -->", "| Word | Meaning | It signals |", "|---|---|---|"]
    rows += [f"| {w['word']} | {w['meaning']} | {w['signals']} |" for w in group.get("items", [])]
    return "\n".join(rows)


def fill_regions(entry, sp, text: str, only) -> str:
    """Rewrite the generated regions of one hand file; the text outside the regions is never changed."""
    tasks = {t["id"]: t for t in _items(entry, "tasks")}
    lines, out, i = text.split("\n"), [], 0
    wanted = {"task": "tasks", "plan": "plan", "exam-english": "exam-english"}
    while i < len(lines):
        m = re.match(r"^<!--\s*(task|plan|exam-english):start\b(.*?)-->$", lines[i].strip())
        if not m:
            out.append(lines[i])
            i += 1
            continue
        kind = m.group(1)
        j = i + 1
        while j < len(lines) and not re.match(r"^<!--\s*" + kind + r":end\s*-->$", lines[j].strip()):
            j += 1
        if j >= len(lines) or (only is not None and wanted[kind] not in only):
            out.append(lines[i])
            i += 1
            continue
        attrs = dict(p.split("=", 1) for p in m.group(2).split() if "=" in p)
        body = None
        if kind == "task":
            task = tasks.get(attrs.get("id"))
            body = task_body(task, sp) if task and task.get("status") == "ready" else ""
        elif kind == "plan":
            body = _plan_table(attrs.get("id"))
        else:
            body = _ee_table(attrs.get("group"))
        if body is None:        # unknown key: leave the region as it is
            out += lines[i:j + 1]
        else:
            out.append(lines[i])
            if body:
                out += ["", body, ""]
            out.append(lines[j])
        i = j + 1
    return "\n".join(out)


# ---------------------------------------------------------------- sources.md, glossary.md, exam-english.md, sheet.md

def _facts() -> dict:
    return _lint()._load_facts()


def _used_facts(entry, sp) -> list:
    ids = []
    folder = common.BOOK / _dirname(entry)
    for fs in _lint().template(entry)["files"]:
        path = folder / fs["name"]
        if fs.get("source") == "hand" and path.exists():
            ids += [m[1] for m in _RE_FACT_LINK.findall(path.read_text(encoding="utf-8"))]
    for kind in ("questions", "cards", "speak", "tasks"):
        for item in _items(entry, kind):
            if item.get("status") in ("rejected", "retired"):
                continue
            ids += list(item.get("facts") or []) + list(item.get("cost_facts") or [])
    return sorted(set(ids))


def gen_sources(entry, sp) -> str:
    facts, pages = _facts(), {}
    for fid in _used_facts(entry, sp):
        fact = facts.get(fid)
        if not fact or fact.get("status") in ("rejected",):
            continue
        for ev in fact.get("evidence", []):
            if not ev.get("url"):
                continue
            page = pages.setdefault(ev["url"], {"title": ev.get("title") or ev["url"], "checked": "", "facts": {}})
            page["checked"] = max(page["checked"], str(fact.get("retrieved") or ""))
            page["facts"][fid] = fact.get("service")
    blocks = [_marker(sp) + f"\n# {entry['title']}: sources"]
    rows = []
    for url, page in sorted(pages.items(), key=lambda kv: (kv[1]["title"].lower(), kv[0])):
        links = ", ".join(f"[{fid}](../facts/{service}.md#{fid})" for fid, service in sorted(page["facts"].items()))
        rows.append(f"- [{page['title']}]({url}). Checked {page['checked']}. Facts: {links}")
    blocks.append("\n".join(rows) if rows else "Nothing here yet.")
    return _join(blocks)


def gen_glossary(sp):
    """Returns (text, errors). A term whose anchor differs from its id is an error (exit 1)."""
    lint = _lint()
    terms = (common.read_json(common.DATA / "terms.json") or {}).get("terms", [])
    blocks, errors = [_marker(sp) + "\n# Glossary"], []
    for t in sorted(terms, key=lambda t: (t["term"].lower(), t["id"])):
        if lint.anchor(t["term"]) != t["id"]:
            errors.append(f"term `{t['term']}`: its anchor `{lint.anchor(t['term'])}` differs from the id `{t['id']}`")
        blocks.append(f"### {t['term']}")
        if t.get("respelling"):
            blocks.append(f"**Say it.** {t['respelling']}")
        blocks.append(t.get("meaning", ""))
        if t.get("collocations"):
            blocks.append("**Words that go with it.** " + "; ".join(t["collocations"]))
        if t.get("do_not_confuse"):
            blocks.append("**Do not confuse with.** " + ", ".join(t["do_not_confuse"]))
    if not terms:
        blocks.append("Nothing here yet.")
    return _join(blocks), errors


def gen_exam_english(entry, sp) -> str:
    data = common.read_json(common.DATA / "exam-english.json") or {}
    blocks = [_marker(sp) + f"\n# {entry['title']}: exam English"]
    for group in data.get("groups", []):
        blocks += [f"## {group['title']}", _ee_table(group["id"], "plain")]
    if not data.get("groups"):
        blocks.append("Nothing here yet.")
    return _join(blocks)


def gen_sheet(entry, sp, fs) -> str:
    lint = _lint()
    source = " ".join(str(x) for x in fs.get("from", []))
    blocks = [_marker(sp) + f"\n# {entry['title']}: sheet"]
    changed_rows = []
    for other in common.chapters():
        if other["id"] == entry["id"] or not (common.BOOK / _dirname(other)).is_dir():
            continue
        try:
            docs = lint._hand_docs(other)
        except SystemExit:
            continue
        part = []
        for doc in docs.values():
            for b in doc.blocks:
                kind = b.extra.get("tkind") if b.kind == "table" else None
                if "signals" in source and kind == "signals":
                    part.append("<!-- table: signals -->\n" + "\n".join(x.strip() for x in b.lines))
                elif "signals" in source and b.kind == "list" and any(m["block"] is b and m["kind"] == "trap" for m in doc.markers):
                    part.append("\n".join("- " + re.sub(r"\s*<!--.*?-->", "", it["text"]).strip() for it in b.extra["items"]))
                elif "numbers" in source and kind == "numbers":
                    part.append("<!-- table: numbers -->\n" + "\n".join(x.strip() for x in b.lines))
                elif "Changed" in source and b.kind == "quote" and b.extra["content"][0].startswith("**Changed recently:**"):
                    m = re.search(r"\((20[0-9]{2}-[0-9]{2}(?:-[0-9]{2})?)\)", b.extra["content"][0])
                    changed_rows.append((m.group(1) if m else "", other["id"], "\n".join(x.strip() for x in b.lines)))
        if part:
            blocks += [f"## {other['title']}"] + part
    if "Changed" in source:
        for _, _, text in sorted(changed_rows, key=lambda r: (r[0], r[1]), reverse=True):
            blocks.append(text)
        rows = []
        for fid, fact in sorted(_facts().items()):
            ch = fact.get("changed")
            if ch and fact.get("status") == "verified":
                rows.append((str(ch.get("date", "")), f"- {ch.get('date', '')}: {fact.get('claim', '')} [{fid}](../facts/{fact.get('service')}.md#{fid})"))
        if rows:
            blocks += ["## Facts that changed", "\n".join(r[1] for r in sorted(rows, reverse=True))]
    if len(blocks) == 1:
        blocks.append("Nothing here yet.")
    return _join(blocks)


# ---------------------------------------------------------------- driver

def _outputs(entry, sp, only, with_facts, result) -> dict:
    """relative path -> new text, for one chapter."""
    lint = _lint()
    tpl, dirname, out = lint.template(entry), _dirname(entry), {}
    for kind, name in _SCHEMAS.items():
        doc = _doc(entry, kind)
        if doc is None:
            continue
        try:
            from saalib import schemas
            errors = schemas.validate(doc, name)
        except FileNotFoundError:
            errors = []
        for err in errors[:5]:
            result["invalid"].append((f"data/{dirname}/{kind}.json", err))
    if result["invalid"]:
        return out
    want = lambda kind: only is None or kind in only
    for fs in tpl["files"]:
        name, rel = fs["name"], f"{dirname}/{fs['name']}"
        if fs.get("source") == "generated":
            kind = lint.GEN_KINDS.get(name)
            if kind is None or not want(kind):
                continue
            if kind == "do":
                if not fs.get("required") and _doc(entry, "tasks") is None:
                    continue
                out[rel] = gen_do(entry, sp)
            elif kind == "say":
                out[rel] = gen_say(entry, sp, fs)
            elif kind == "quiz":
                out[rel] = gen_quiz(entry, sp)
            elif kind == "sources":
                out[rel] = gen_sources(entry, sp)
            elif kind == "exam-english":
                out[rel] = gen_exam_english(entry, sp)
            elif kind == "sheet":
                out[rel] = gen_sheet(entry, sp, fs)
        elif fs.get("source") == "hand":
            path = common.BOOK / rel
            if path.exists():
                result["files"].append(rel)
                text = path.read_text(encoding="utf-8")
                if re.search(r"<!--\s*(task|plan|exam-english):start\b", text):
                    out[rel] = fill_regions(entry, sp, text, only)
    if with_facts:
        # gate-break H14: the sheets of the chapter's services and of every service that a hand file links
        services = set(entry.get("services", []))
        for rel in result["files"]:
            if rel.startswith(dirname + "/"):
                services.update(re.findall(r"\]\(\.\./facts/([a-z0-9-]+)\.md#", (common.BOOK / rel).read_text(encoding="utf-8")))
        _fact_sheets(services, out, result)
    return out


def _fact_sheets(services, out, result):
    try:
        from saalib import facts as facts_mod
        render = facts_mod.render_sheet
    except Exception:
        result["skipped"].append("facts (saalib.facts.render_sheet is not available)")
        return
    have = {f.get("service") for f in _facts().values() if f.get("status") in ("verified", "superseded")}
    for service in sorted(set(services) & have):
        text = render(service)
        if isinstance(text, str) and text:
            out[f"facts/{service}.md"] = text if text.endswith("\n") else text + "\n"


def _write(path: Path, text: str) -> None:
    common.ensure_dir(path.parent)
    with common.file_lock(path):
        tmp = path.with_name(path.name + f".tmp{os.getpid()}")
        tmp.write_text(text, encoding="utf-8", newline="\n")
        os.replace(tmp, path)


def run(entry=None, check=False, only=None, all_chapters=False) -> dict:
    """Build every output in memory; compare (check) or write. Returns the result of one run."""
    lint = _lint()
    sp = lint.spec()
    result = {"checked": 0, "stale": [], "missing": [], "written": [], "unchanged": 0, "invalid": [], "skipped": [],
              "files": [], "errors": []}
    out = {}
    if all_chapters:
        for e in common.chapters():
            if (common.BOOK / _dirname(e)).is_dir() or (common.DATA / _dirname(e)).is_dir():
                out.update(_outputs(e, sp, only, False, result))
        if only is None or "facts" in only:
            _fact_sheets({f.get("service") for f in _facts().values()}, out, result)
        if only is None or "glossary" in only:
            text, errors = gen_glossary(sp)
            result["errors"] += errors
            out["glossary.md"] = text
    else:
        out.update(_outputs(entry, sp, only, only is None or "facts" in only, result))
        if only is not None and "glossary" in only:
            text, errors = gen_glossary(sp)
            result["errors"] += errors
            out["glossary.md"] = text
    if result["invalid"] or result["errors"]:
        return result
    if all_chapters and (only is None or "facts" in only) and common.FACTSHEETS.is_dir():
        # gate-break H14: a sheet that no verified fact produces was written by hand (or its facts are gone)
        for path in sorted(common.FACTSHEETS.glob("*.md")):
            rel = f"facts/{path.name}"
            if rel not in out:
                result["checked"] += 1
                if check:
                    result["stale"].append(rel)
                else:
                    result["skipped"].append(f"{rel} is produced by no verified fact: delete the file")
    for rel in sorted(out):
        path = common.BOOK / rel
        result["checked"] += 1
        old = path.read_bytes() if path.exists() else None
        new = out[rel].encode("utf-8")
        if old == new:
            result["unchanged"] += 1
        elif check:
            result["missing" if old is None else "stale"].append(rel)
        else:
            _write(path, out[rel])
            result["written"].append(rel)
    return result


def cmd(args) -> int:
    only = None
    if args.only:
        only = [k for part in args.only for k in part.split(",") if k]
        bad = [k for k in only if k not in KINDS]
        if bad:
            return common.fail(f"unknown sync kind {', '.join(bad)}; kinds: {', '.join(KINDS)}", common.EXIT_PRECONDITION)
    if not args.all and not args.chapter:
        return common.fail("sync needs a chapter or --all", common.EXIT_PRECONDITION)
    result = run(None if args.all else common.chapter(args.chapter), check=args.check, only=only, all_chapters=args.all)
    if result["invalid"]:
        findings = [{"code": "X01", "file": f, "line": None, "item": None, "msg": msg} for f, msg in result["invalid"]]
        common.emit({"ok": False, "errors": findings} if args.json else
                    "sync: data files are not valid\n" + "\n".join(f"{f['file']}: X01 {f['msg']}" for f in findings[:40]), args)
        return common.EXIT_PRECONDITION
    if result["errors"]:
        common.emit({"ok": False, "errors": result["errors"]} if args.json else "sync: FAIL\n" + "\n".join(result["errors"][:40]), args)
        return common.EXIT_FAIL
    if args.check:
        public = {"checked": result["checked"], "stale": result["stale"], "missing": result["missing"]}
        bad = result["stale"] or result["missing"]
        text = f"sync --check: {'STALE' if bad else 'ok'} checked={result['checked']} stale={len(result['stale'])} missing={len(result['missing'])}"
        text = "\n".join([text] + [f"stale: {x}" for x in result["stale"]][:20] + [f"missing: {x}" for x in result["missing"]][:20])
        common.emit(public if args.json else text, args)
        return common.EXIT_FAIL if bad else common.EXIT_OK
    public = {"written": result["written"], "unchanged": result["unchanged"]}
    if result["skipped"]:
        public["skipped"] = result["skipped"]
    text = "\n".join([f"sync: written={len(result['written'])} unchanged={result['unchanged']}"] + result["written"][:40])
    common.emit(public if args.json else text, args)
    return common.EXIT_OK
