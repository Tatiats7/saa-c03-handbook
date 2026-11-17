"""Spec file to checked scene to SVG file. The one place that knows which kinds exist."""
from __future__ import annotations

import importlib
import os
import pkgutil
from pathlib import Path

from .. import common
from . import arch
from . import icons as icons_mod
from . import layout_grid
from . import lint
from . import schema
from . import shapes
from . import svg

# kind -> build_scene(spec) -> scene
KINDS = {"arch": arch.build_scene}
# kind -> its module. A kind module may also define (all optional):
#   lint_spec(spec, icons) -> issues        limit checks; a code starting with "ref-" stops before layout
#   lint_scene(scene, spec) -> (issues, stats)   replaces lint.lint_scene (compare, raw)
#   caption(spec) -> dict                   replaces the default caption
#   WANTS_BASE_DIR = True                   lint_spec and build_scene then also get base_dir (raw)
MODULES = {}
_discovered = False


def register_kind(name: str, build_scene) -> None:
    KINDS[name] = build_scene


def _discover() -> None:
    """Load optional kind modules: any saalib/diagram/layout_<x>.py that defines KIND and build_scene."""
    global _discovered
    if _discovered:
        return
    _discovered = True
    here = Path(__file__).resolve().parent
    for mod in sorted(pkgutil.iter_modules([str(here)]), key=lambda m: m.name):
        if not mod.name.startswith("layout_") or mod.name == "layout_grid":
            continue
        try:
            module = importlib.import_module(f"{__package__}.{mod.name}")
        except Exception:      # a broken optional kind must not take the others down
            continue
        if hasattr(module, "KIND") and hasattr(module, "build_scene"):
            KINDS.setdefault(module.KIND, module.build_scene)
            MODULES.setdefault(module.KIND, module)


def all_ids() -> list:
    if not common.DIAGRAM_SRC.is_dir():
        return []
    return sorted(p.stem for p in common.DIAGRAM_SRC.glob("*.json"))


def spec_path(diagram_id: str) -> Path:
    return common.DIAGRAM_SRC / f"{diagram_id}.json"


def svg_path(diagram_id: str) -> Path:
    return common.DIAGRAM_SVG / f"{diagram_id}.svg"


def check_spec(spec, expect_id: str = None, icons: dict = None, base_dir: Path = None) -> dict:
    """Validate, lay out and lint one spec. Never raises on a bad spec.

    base_dir: the folder of the spec file (the raw kind reads its SVG from there)."""
    _discover()
    ident = spec.get("id", expect_id or "?") if isinstance(spec, dict) else (expect_id or "?")
    result = {"id": ident, "issues": [], "stats": None, "scene": None, "spec": spec}
    errors = schema.validate(spec)
    if errors:
        result["issues"] = [{"level": "error", "code": "schema", "msg": e} for e in errors]
        return result
    if expect_id is not None and spec["id"] != expect_id:
        result["issues"].append({"level": "error", "code": "id-mismatch",
                                 "msg": f"\"id\" is {spec['id']!r} but the file is named {expect_id}.json"})
    kind = spec["kind"]
    if kind not in KINDS:
        result["issues"].append({"level": "error", "code": "kind-unsupported", "msg": f"kind {kind!r} is not supported yet"})
        return result
    if icons is None:
        icons = icons_mod.load()
    module = MODULES.get(kind)
    extra = (base_dir or common.DIAGRAM_SRC,) if getattr(module, "WANTS_BASE_DIR", False) else ()
    if kind == "arch":
        result["issues"] += lint.lint_spec(spec, icons)
    elif hasattr(module, "lint_spec"):
        result["issues"] += module.lint_spec(spec, icons, *extra)
    result["issues"] += shapes.number_issues(spec, module.label_texts(spec, *extra) if hasattr(module, "label_texts") else ())
    if lint.has_fatal(result["issues"]):
        return result
    try:
        scene = KINDS[kind](spec, *extra)
    except layout_grid.LayoutError as exc:
        result["issues"].append({"level": "error", "code": "layout", "msg": str(exc)})
        return result
    if hasattr(module, "lint_scene"):
        issues, stats = module.lint_scene(scene, spec)
    else:
        issues, stats = lint.lint_scene(scene, spec.get("size", "m"))
    result["issues"] += issues
    result["stats"] = stats
    result["scene"] = scene
    return result


def check_file(path: Path, expect_id: str = None) -> dict:
    path = Path(path)
    if not path.is_file():
        return {"id": expect_id or path.stem, "stats": None, "scene": None, "spec": None,
                "issues": [{"level": "error", "code": "missing", "msg": f"{common.rel(path)} does not exist"}]}
    try:
        spec = common.read_json(path)
    except ValueError as exc:
        return {"id": expect_id or path.stem, "stats": None, "scene": None, "spec": None,
                "issues": [{"level": "error", "code": "json", "msg": f"{common.rel(path)}: {exc}"}]}
    return check_spec(spec, expect_id, base_dir=path.parent)


def check_id(diagram_id: str) -> dict:
    return check_file(spec_path(diagram_id), diagram_id)


def _write(out: Path, text: str) -> None:
    common.ensure_dir(out.parent)
    tmp = out.with_name(out.name + f".tmp{os.getpid()}")
    tmp.write_text(text, encoding="utf-8")
    os.replace(tmp, out)


def panel_path(diagram_id: str, number: int) -> Path:
    """File of one panel of a compare diagram: diagrams/svg/<id>.p<number>.svg."""
    return common.DIAGRAM_SVG / f"{diagram_id}.p{number}.svg"


def build_one(diagram_id: str) -> dict:
    """Check and, when there is no error, write diagrams/svg/<id>.svg.

    A compare diagram also gets one file per panel, diagrams/svg/<id>.p1.svg and so on."""
    result = check_id(diagram_id)
    if result["scene"] is None or any(i["level"] == "error" for i in result["issues"]):
        return result
    files = rendered(diagram_id, result)
    out = svg_path(diagram_id)
    result["svg"] = out
    result["panels"] = []
    for path, text in files.items():
        _write(path, text)
        if path != out:
            result["panels"].append(path)
    return result


def rendered(diagram_id: str, result: dict) -> dict:
    """{path: SVG text} that `diagram build` writes for a checked spec (the result of check_id)."""
    icons = icons_mod.load()
    scene, spec = result["scene"], result["spec"]
    files = {svg_path(diagram_id): svg.render_standalone(scene, spec, icons)}
    for number, panel in enumerate(scene.get("panels") or [], 1):
        sub_spec = {"title": f"{spec['title']}: {panel['label']}", "alt": panel.get("alt") or spec["alt"]}
        files[panel_path(diagram_id, number)] = svg.render_standalone(panel["scene"], sub_spec, icons)
    return files


def stale_files(diagram_id: str) -> list:
    """The SVG files of a diagram that are missing or are not the output of its spec (gate-break 61: an SVG drawn
    by hand, or left from an older spec). Empty when the spec has errors; the lint reports those."""
    result = check_id(diagram_id)
    if result["scene"] is None or any(i["level"] == "error" for i in result["issues"]):
        return []
    out = []
    for path, text in rendered(diagram_id, result).items():
        if not path.is_file() or path.read_text(encoding="utf-8") != text:
            out.append(path)
    return out


def caption(spec: dict) -> dict:
    """What goes under the figure: title, claim, and the numbered steps as a list."""
    _discover()
    module = MODULES.get(spec.get("kind"))
    if hasattr(module, "caption"):
        return module.caption(spec)
    steps = {}
    for edge in spec.get("edges", []):
        if edge.get("step") is not None and edge.get("say"):
            steps.setdefault(edge["step"], edge["say"])
    return {"title": spec.get("title", ""), "claim": spec.get("claim", ""), "alt": spec.get("alt", ""),
            "steps": [(n, steps[n]) for n in sorted(steps)]}
