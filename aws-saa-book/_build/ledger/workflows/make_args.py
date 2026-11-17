#!/usr/bin/env python3
"""Build the args for one run of saa-chapter-factory.v4-light.js from the ledger.

Run from the repository root:
  python3 aws-saa-book/_build/ledger/workflows/make_args.py 11 24
  python3 aws-saa-book/_build/ledger/workflows/make_args.py 38 39 --facts
  python3 aws-saa-book/_build/ledger/workflows/make_args.py 35 --skip-lenses 35=faq --note 35="text"

It writes aws-saa-book/_build/tmp/run-<ids>.json and prints the same JSON. Pass that JSON object (not a string)
as the Workflow tool's `args`, with scriptPath = <repo root>/aws-saa-book/_build/ledger/workflows/saa-chapter-factory.v4-light.js.
Each chapter gets `passed` (the stages the ledger has passed), `next_stage`, and an orchestrator note with the
standard rules plus a resume line for stages that were begun and never finished. Stdlib only.
"""
import argparse, json, subprocess, sys
from pathlib import Path

TOOL = [sys.executable, "aws-saa-book/tools/saa.py"]
TMP = Path("aws-saa-book/_build/tmp")
WRITE_RULES = ("Twin pairs: write one more twin pair than the template needs so that one rejection does not block shipping. "
               "The brief's terms are added to the glossary by a terms agent right after the brief: list every term the chapter "
               "defines in bold in brief.json so that no writer needs a needs-term marker. Fetch only pages that are not yet in the "
               "corpus; never refresh a cached page (a refresh changes the snapshots that verified facts quote).")
FACT_RULES = ("Miners run on Sonnet: follow mine-plan.json exactly, add facts in files of 10 to 25, keep every quote verbatim, and make "
              "sure the quote carries every clause, scope, condition and exception of the claim on its own: when the condition stands "
              "in the next sentence, include that sentence in the quote; otherwise narrow the claim. Entail votes run on Opus; currency "
              "and derive on Sonnet. Fetch only pages that are not yet in the corpus; never refresh a cached page.")


def run(args):
    out = subprocess.run(TOOL + args, capture_output=True, text=True)
    return out.stdout


def all_chapters():
    TMP.mkdir(parents=True, exist_ok=True)
    found = {}
    for n in range(1, 30):
        path = TMP / f"wave-args-W{n}.json"
        res = subprocess.run(TOOL + ["registry", "wave-args", f"W{n}", "--out", str(path.resolve())], capture_output=True, text=True)
        if res.returncode not in (0, 2) or not path.exists():
            if n > 13:
                break
            continue
        for ch in json.loads(path.read_text()).get("chapters", []):
            found[ch["id"]] = dict(ch, wave=f"W{n}")
    return found


def stage_info(cid):
    try:
        d = json.loads(run(["stage", "show", cid]))
    except json.JSONDecodeError:
        return [], [], []
    stages = d.get("stages", d)
    passed = [k for k, v in stages.items() if isinstance(v, dict) and v.get("status") == "pass"]
    unfinished = [f"{k} (status {v.get('status')}, attempt {v.get('attempts', v.get('attempt', '?'))})"
                  for k, v in stages.items() if isinstance(v, dict) and v.get("status") in ("running", "fail")]
    return passed, unfinished, d.get("stale", [])


def kv_list(items):
    out = {}
    for item in items or []:
        cid, _, val = item.partition("=")
        out[cid] = val
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("ids", nargs="+", help="chapter ids, for example 24 25")
    ap.add_argument("--facts", action="store_true", help="facts run: stop after verify-facts")
    ap.add_argument("--note", action="append", help="ID=text added to that chapter's orchestrator note")
    ap.add_argument("--skip-lenses", action="append", help="ID=lens1,lens2 mining lenses already finished")
    ap.add_argument("--skip-writers", action="append", help="ID=fast,deep,... writers whose files are complete")
    a = ap.parse_args()
    chapters = all_chapters()
    notes, lenses, writers = kv_list(a.note), kv_list(a.skip_lenses), kv_list(a.skip_writers)
    picked, waves = [], []
    for cid in a.ids:
        if cid not in chapters:
            sys.exit(f"chapter {cid} is in no wave (registry wave-args); check the id")
        ch = dict(chapters[cid])
        passed, unfinished, stale = stage_info(cid)
        ch["passed"] = passed
        parts = [FACT_RULES if a.facts else WRITE_RULES]
        if unfinished:
            parts.insert(0, "Resume: these stages were begun before and did not finish: " + "; ".join(unfinished)
                         + ". Begin each again and continue from any partial files rather than starting over.")
        if stale:
            parts.insert(0, "Stale stages to redo: " + "; ".join(stale[:6]) + ".")
        if cid in notes:
            parts.insert(0, notes[cid])
        ch["orchestrator_note"] = " ".join(parts)
        if cid in lenses:
            ch["skip_lenses"] = [x for x in lenses[cid].split(",") if x]
        if cid in writers:
            ch["skip_writers"] = [x for x in writers[cid].split(",") if x]
        if not a.facts and "prose" not in passed:
            done = []
            for f in ("1-fast.md", "2-deep.md"):
                fp = Path("aws-saa-book") / ch["dir"] / f
                if fp.exists() and len(fp.read_text().split()) > 500:
                    done.append(f)
            if done and cid not in writers:
                print(f"# {cid}: {', '.join(done)} already written. If `python3 aws-saa-book/tools/saa.py lint {cid} --draft` shows no "
                      f"errors in them (a missing SVG is fine), re-run with --skip-writers {cid}=fast,deep so they are not rewritten.",
                      file=sys.stderr)
        if not a.facts and "questions" not in passed and cid not in writers:
            qn = run(["q", "list", "--chapter", cid]).split("\n", 1)[0]
            if qn and not qn.startswith("q list: 0"):
                print(f"# {cid}: {qn.strip()} already exist; add questions to --skip-writers if they are complete.", file=sys.stderr)
        picked.append(ch)
        waves.append(ch.pop("wave"))
    result = {"wave": "+".join(sorted(set(waves))), "chapters": picked, "skipped": [], "only": a.ids}
    if a.facts:
        result["through"] = "verify-facts"
    path = TMP / f"run-{'-'.join(a.ids)}.json"
    path.write_text(json.dumps(result, indent=1))
    print(json.dumps(result, separators=(",", ":")))
    for ch in picked:
        print(f"# {ch['id']} {ch['slug']}: next={ch.get('next_stage')} passed={len(ch['passed'])} stages", file=sys.stderr)
    print(f"# written {path}", file=sys.stderr)


if __name__ == "__main__":
    main()
