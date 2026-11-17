#!/usr/bin/env python3
"""saa.py: the single command-line tool behind the SAA-C03 Handbook build.

Run from the repo root as:  python3 aws-saa-book/tools/saa.py <subcommand> [options]

This file is only a dispatcher. Each subcommand lives in a module under
aws-saa-book/tools/saalib/ that exposes  register(subparsers)  and sets
func=<callable(args) -> int>  on its parsers. Exit codes: 0 pass, 1 blocking
failure, 2 warnings only, 3 precondition missing or stale, 4 policy refusal,
5 transient (safe to retry).
"""
import argparse
import importlib
import os
import pkgutil
import sys
from pathlib import Path

TOOLS = Path(__file__).resolve().parent
REAL_BOOK = TOOLS.parent
VERSION = "0.1.1"

sys.path.insert(0, str(TOOLS))


def _pre_scan_book_dir(argv):
    """`--book-dir DIR` must take effect before any module computes its paths.

    DIR is a sandbox copy of the book layout and has to live inside the real book folder
    (normally under aws-saa-book/_build/tmp/). Used by tests and by gate-breaking experiments.
    """
    argv = list(argv)
    for i, arg in enumerate(argv):
        value = None
        if arg == "--book-dir" and i + 1 < len(argv):
            value, cut = argv[i + 1], 2
        elif arg.startswith("--book-dir="):
            value, cut = arg.split("=", 1)[1], 1
        if value is not None:
            path = Path(value)
            if not path.is_absolute():
                path = REAL_BOOK.parent / path
            path = path.resolve()
            try:
                path.relative_to(REAL_BOOK.resolve())
            except ValueError:
                print(f"refused: --book-dir must be inside {REAL_BOOK}", file=sys.stderr)
                raise SystemExit(4)
            os.environ["SAA_BOOK_DIR"] = str(path)
            del argv[i:i + cut]
            break
    return argv


def main(argv=None):
    argv = _pre_scan_book_dir(sys.argv[1:] if argv is None else argv)
    book = os.environ.get("SAA_BOOK_DIR") or str(REAL_BOOK)
    parser = argparse.ArgumentParser(prog="saa.py", description=__doc__.splitlines()[0],
                                     epilog="Global option: --book-dir DIR runs against a sandbox copy inside aws-saa-book/.")
    parser.add_argument("--version", action="version", version=f"saa.py {VERSION}")
    sub = parser.add_subparsers(dest="cmd")

    ping = sub.add_parser("ping", help="check that the tool runs (used by the permission canary)")
    ping.set_defaults(func=lambda a: (print(f"saa.py {VERSION} ok; book={book}"), 0)[1])

    libdir = TOOLS / "saalib"
    failed = []
    if libdir.is_dir():
        for mod in sorted(pkgutil.iter_modules([str(libdir)]), key=lambda m: m.name):
            if mod.name.startswith("_"):
                continue
            try:
                module = importlib.import_module(f"saalib.{mod.name}")
                if hasattr(module, "register"):
                    module.register(sub)
            except Exception as exc:  # a broken module must not take the whole tool down
                failed.append((mod.name, repr(exc)))

    args = parser.parse_args(argv)
    if failed and getattr(args, "cmd", None) not in ("ping",):
        for name, err in failed:
            print(f"warning: module saalib.{name} failed to load: {err}", file=sys.stderr)
    if not getattr(args, "func", None):
        parser.print_help()
        return 3
    return int(args.func(args) or 0)


if __name__ == "__main__":
    sys.exit(main())
