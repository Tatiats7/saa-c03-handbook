"""The diagram system: a declarative JSON spec rendered by our own grid renderer to SVG.

    python3 aws-saa-book/tools/saa.py diagram build <id> | --all
    python3 aws-saa-book/tools/saa.py diagram lint <id> | --all | --file <spec.json>
    python3 aws-saa-book/tools/saa.py diagram preview <id>
    python3 aws-saa-book/tools/saa.py diagram shot <id>
    python3 aws-saa-book/tools/saa.py diagram shot --file <page.html|image.svg> --out <png> [--width W --height H --dark --full]
    python3 aws-saa-book/tools/saa.py diagram sheet
    python3 aws-saa-book/tools/saa.py diagram icons [--from <unzipped package>] [--zip-url URL] [--list]
    python3 aws-saa-book/tools/saa.py diagram css | sprite

Author guide: aws-saa-book/_build/style/TOOLS-diagram.md
"""
from __future__ import annotations

from pathlib import Path

from .. import common


def _ids(args) -> list:
    from . import pipeline
    if getattr(args, "all", False):
        return pipeline.all_ids()
    return [args.id] if getattr(args, "id", None) else []


def _report(results: list, args, verb: str) -> int:
    worst = common.EXIT_OK
    payload = []
    lines = []
    for res in results:
        errors = [i for i in res["issues"] if i["level"] == "error"]
        warns = [i for i in res["issues"] if i["level"] == "warn"]
        status = "FAIL" if errors else ("WARN" if warns else "ok")
        if errors:
            worst = common.EXIT_FAIL
        elif warns and worst == common.EXIT_OK:
            worst = common.EXIT_WARN
        extra = ""
        if res.get("stats"):
            s = res["stats"]
            extra = f"  {s['width']}x{s['height']}  nodes {s['nodes']}  edges {s['edges']}  crossings {s['crossings']}"
        out = f"  -> {common.rel(res['svg'])}" if res.get("svg") else ""
        lines.append(f"{status:4} {res['id']}{extra}{out}")
        for issue in res["issues"]:
            lines.append(f"     {issue['level']:5} {issue['code']}: {issue['msg']}")
        payload.append({"id": res["id"], "status": status, "issues": res["issues"], "stats": res.get("stats"),
                        "svg": common.rel(res["svg"]) if res.get("svg") else None})
    if not results:
        lines.append(f"nothing to {verb}")
    common.emit(payload if getattr(args, "json", False) else "\n".join(lines), args)
    return worst


def cmd_build(args) -> int:
    from . import pipeline
    ids = _ids(args)
    if not ids:
        return common.fail("give a diagram id or --all", common.EXIT_PRECONDITION)
    return _report([pipeline.build_one(i) for i in ids], args, "build")


def cmd_lint(args) -> int:
    from . import pipeline
    if getattr(args, "file", None):
        path = Path(args.file)
        if not path.is_absolute():
            path = common.REPO / path
        return _report([pipeline.check_file(path)], args, "lint")
    ids = _ids(args)
    if not ids:
        return common.fail("give a diagram id, --all or --file", common.EXIT_PRECONDITION)
    return _report([pipeline.check_id(i) for i in ids], args, "lint")


def cmd_preview(args) -> int:
    from . import preview
    try:
        page, _size = preview.write_preview(args.id)
    except preview.PreviewError as exc:
        return common.fail(str(exc), exc.code)
    common.emit(f"wrote {common.rel(page)}", args)
    return common.EXIT_OK


def cmd_shot(args) -> int:
    from . import preview
    try:
        if args.file:
            if not args.out:
                return common.fail("--file needs --out <png>", common.EXIT_PRECONDITION)
            png = preview.shot_file(args.file, args.out, args.width, args.height, args.dark, args.full, args.scale)
        elif args.id:
            png = preview.shot_diagram(args.id, args.out, args.scale)
        else:
            return common.fail("give a diagram id or --file", common.EXIT_PRECONDITION)
    except preview.PreviewError as exc:
        return common.fail(str(exc), exc.code)
    print(f"wrote {common.rel(png)}")
    return common.EXIT_OK


def cmd_sheet(args) -> int:
    from . import preview
    try:
        png, count = preview.sheet(args.out, args.scale)
    except preview.PreviewError as exc:
        return common.fail(str(exc), exc.code)
    print(f"wrote {common.rel(png)} ({count} diagrams)")
    return common.EXIT_OK


def cmd_icons(args) -> int:
    from . import icons
    if args.list:
        data = icons.load()
        common.emit("\n".join(f"{name:36} {entry.get('kind', ''):9} {entry.get('file', '')}" for name, entry in sorted(data.items()))
                    or "icons.json is empty; run: diagram icons", args)
        return common.EXIT_OK
    if args.find:
        root = icons.unpack_dir() / "unpacked"
        if not root.is_dir():
            return common.fail("no unpacked package; run: diagram icons", common.EXIT_PRECONDITION)
        terms = [t.lower() for t in args.find.split(",")]
        hits = sorted({"/".join(p.relative_to(root).parts[1:]) for p in root.rglob("*.svg")
                       if "__MACOSX" not in str(p) and ("_48" in p.name or "_32" in p.name and "Group" in str(p))
                       and any(t in p.name.lower() for t in terms)})
        common.emit("\n".join(hits) or "no match", args)
        return common.EXIT_OK
    try:
        if args.from_dir:
            root = Path(args.from_dir)
            if not root.is_absolute():
                root = common.REPO / root
            if not root.is_dir():
                return common.fail(f"{root} is not a folder", common.EXIT_PRECONDITION)
            meta = common.read_json(icons.unpack_dir() / "package.json", {}) or {}
        else:
            meta = icons.download(args.zip_url)
            root = icons.unpack_dir() / "unpacked"
    except PermissionError as exc:
        return common.fail(str(exc), common.EXIT_POLICY)
    except OSError as exc:
        return common.fail(f"download failed: {exc}", common.EXIT_TRANSIENT)
    except RuntimeError as exc:
        return common.fail(str(exc), common.EXIT_PRECONDITION)
    if args.usage:
        meta["usage_statement"] = args.usage
        common.write_json(icons.unpack_dir() / "package.json", meta)
    result = icons.build(root, meta)
    common.write_json(icons.icons_json_path(), result)
    icons.sprite_path().write_text(icons.sprite(result["icons"]), encoding="utf-8")
    icons.write_notice(meta, result)
    missing = result["meta"]["missing"]
    common.emit(f"icons: {result['meta']['count']} written to {common.rel(icons.icons_json_path())}; "
                f"release {result['meta']['release']}; missing {len(missing)}"
                + (": " + ", ".join(missing) if missing else ""), args)
    return common.EXIT_WARN if missing else common.EXIT_OK


def cmd_css(args) -> int:
    from . import svg
    common.emit(svg.inline_css(), args)
    return common.EXIT_OK


def cmd_sprite(args) -> int:
    from . import icons
    common.emit(icons.sprite(icons.load()), args)
    return common.EXIT_OK


def register(subparsers) -> None:
    parser = subparsers.add_parser("diagram", help="build, lint and preview diagrams (JSON spec to SVG)")
    actions = parser.add_subparsers(dest="action")
    parser.set_defaults(func=lambda a: (parser.print_help(), common.EXIT_PRECONDITION)[1])

    p = actions.add_parser("build", help="validate, lint and render diagrams/src/<id>.json to diagrams/svg/<id>.svg")
    p.add_argument("id", nargs="?")
    p.add_argument("--all", action="store_true")
    common.add_common_args(p)
    p.set_defaults(func=cmd_build)

    p = actions.add_parser("lint", help="validate and lint without writing the SVG")
    p.add_argument("id", nargs="?")
    p.add_argument("--all", action="store_true")
    p.add_argument("--file", help="lint a spec file anywhere inside the book")
    common.add_common_args(p)
    p.set_defaults(func=cmd_lint)

    p = actions.add_parser("preview", help="write the four-panel preview page (desktop and 368 px, light and dark)")
    p.add_argument("id")
    common.add_common_args(p)
    p.set_defaults(func=cmd_preview)

    p = actions.add_parser("shot", help="screenshot a diagram preview, or any .html or .svg file, with headless Chrome")
    p.add_argument("id", nargs="?")
    p.add_argument("--file", help="an .html or .svg file inside the book")
    p.add_argument("--out", help="PNG path inside the book")
    p.add_argument("--width", type=int, default=1280)
    p.add_argument("--height", type=int, default=900)
    p.add_argument("--dark", action="store_true", help="dark colour scheme (also sets data-theme=dark on the root)")
    p.add_argument("--full", action="store_true", help="measure the page and capture its full height")
    p.add_argument("--scale", type=float, default=2.0, help="device scale factor (default 2)")
    p.set_defaults(func=cmd_shot)

    p = actions.add_parser("sheet", help="one contact-sheet PNG of all built diagrams")
    p.add_argument("--out", help="PNG path inside the book")
    p.add_argument("--scale", type=float, default=1.0)
    p.set_defaults(func=cmd_sheet)

    p = actions.add_parser("icons", help="download the AWS Architecture Icons once and build diagrams/icons.json")
    p.add_argument("--from", dest="from_dir", help="use an already unzipped package folder")
    p.add_argument("--zip-url", help="package URL on d1.awsstatic.com (default: found on the AWS icons page)")
    p.add_argument("--usage", help="AWS usage statement to record in ICONS-NOTICE.md when it cannot be captured")
    p.add_argument("--list", action="store_true", help="list the icon names in icons.json")
    p.add_argument("--find", help="search the unpacked package for file names containing any of these comma-separated terms")
    common.add_common_args(p)
    p.set_defaults(func=cmd_icons)

    p = actions.add_parser("css", help="print the stylesheet for inline diagrams (classes bound to --dg-* tokens)")
    common.add_common_args(p)
    p.set_defaults(func=cmd_css)

    p = actions.add_parser("sprite", help="print the icon sprite (<symbol id=ic-NAME>) for the web shell")
    common.add_common_args(p)
    p.set_defaults(func=cmd_sprite)
