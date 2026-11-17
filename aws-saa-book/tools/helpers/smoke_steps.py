"""The steps of the W0 smoke test. Run through smoke.py (python3 aws-saa-book/tools/helpers/smoke.py run).

Every step is one `saa.py --book-dir <sandbox>` command with an expected exit code. Steps marked MUST FAIL
feed the tool one bad input and require a refusal.

Honest limits of this test: the facts, the votes and the solver answers are written by one agent (this
script and its input files), so the votes and the blind solve prove the mechanics, not independence.
"""
from __future__ import annotations

import json
import shutil

from saalib import common


def run(S) -> None:
    book, inp = S.BOOK, S.INPUTS
    tmp = book / "_build" / "tmp"
    f = lambda name: common.rel(inp / name)                      # noqa: E731
    t = lambda name: common.rel(tmp / name)                      # noqa: E731
    deep = book / "99-sample" / "2-deep.md"

    # ---- 1. corpus
    S.step("MUST FAIL: fetch from a host outside the allow-list", "fetch", "https://example.com/", expect=(4,))
    S.step("the tables of the quotas page", "tables", S.QUOTA_SID, "--index", "2", keep=8)
    S.step("search the snapshots", "search", "scales up to 100 Gbps", "--scope", "snap", keep=4)

    # ---- 2. facts
    S.step_json("add three facts with verbatim quotes", "facts", "add", "--file", f("facts-add.json"), "--by", "smoke-miner")
    S.step_json("adopt one fact from a table row (table 2, row 2 of the quotas page)", "facts", "adopt",
                "--source", S.QUOTA_SID, "--table", "2", "--row", "2", "--file", f("fact-adopt.json"), "--by", "smoke-miner")
    code, res = S.step_json("MUST FAIL: a fact whose number (45 Gbps) is not in its quote", "facts", "add",
                            "--file", f("fact-bad.json"), "--by", "smoke-miner", expect=(1,), keep=8)
    S.check("the bad fact is rejected with M5", bool(res) and "M5" in json.dumps(res["rejected"]))
    code, res = S.step_json("mechanical verification of the vpc facts", "facts", "verify", "--service", "vpc")
    S.check("4 facts checked, 4 ok", bool(res) and res.get("checked") == 4 and res.get("ok") == 4)
    code, res = S.step_json("make an entail batch", "facts", "batch", "--chapter", "99", "--lens", "entail")
    batch = (res or {}).get("batches", ["99-entail-001"])[0]
    S.step("write the verifier packet", "facts", "packet", batch, "--out", t("packet-entail.json"))
    packet = common.read_json(tmp / "packet-entail.json") or {}
    S.check("the packet holds no author, status or votes",
            not any(k in fact for fact in packet.get("facts", []) for k in ("author", "status", "votes")) and len(packet.get("facts", [])) == 4)
    S.step_json("MUST FAIL: the author votes on the author's own facts", "facts", "vote", "--file", f("votes.json"),
                "--by", "smoke-miner", expect=(1,), keep=6)
    S.step_json("record four entail votes by another label", "facts", "vote", "--file", f("votes.json"), "--by", "smoke-verifier", keep=6)
    code, res = S.step_json("finalize", "facts", "finalize", "--service", "vpc")
    S.check("4 facts verified", bool(res) and len(res.get("verified", [])) == 4)
    S.step("render the fact sheet facts/vpc.md", "facts", "render", "--service", "vpc")
    sheet = (book / "facts" / "vpc.md").read_text(encoding="utf-8") if (book / "facts" / "vpc.md").exists() else ""
    S.check("the fact sheet has one anchor per fact and the exact AWS sentence",
            sheet.count("\n### vpc-natgw-") == 4 and "automatically scales up to 100 Gbps." in sheet)
    S.step("writer cards with ready-made links", "facts", "card", "--service", "vpc", keep=10)

    # ---- 3. chapter text, sync, lint
    block = (inp / "chapter-insert.md").read_text(encoding="utf-8").rstrip("\n")
    text = deep.read_text(encoding="utf-8")
    deep.write_text(text.replace("> **Try it:**", block, 1), encoding="utf-8")
    S.say("\n(edited 99-sample/2-deep.md: one Go deeper block with five links to the four vpc facts)")
    S.step("sync the generated files", "sync", "99", keep=8)
    S.step("lint the chapter (draft status; warnings allowed, no error)", "lint", "99", expect=(0, 2), keep=8)
    good, bad = "[up to 100 Gbps](../facts/vpc.md#vpc-natgw-bandwidth)", "[up to 45 Gbps](../facts/vpc.md#vpc-natgw-bandwidth)"
    text = deep.read_text(encoding="utf-8")
    deep.write_text(text.replace(good, bad, 1), encoding="utf-8")
    code, out, err = S.step("MUST FAIL: lint with the wrong number `up to 45 Gbps` in one link text", "lint", "99", expect=(1,), keep=4)
    S.check("lint reports L303 for the wrong number", "L303" in out and "45 Gbps" in out)
    deep.write_text(text, encoding="utf-8")
    S.step("lint again after the number is restored", "lint", "99", expect=(0, 2), keep=3)

    # ---- 4. questions: add, lint, blind packs, adjudicate
    code, res = S.step_json("add two questions", "q", "add", "--chapter", "99", "--file", f("questions.json"), "--by", "smoke-writer")
    new_ids = (res or {}).get("added", [])
    S.check("two questions stored", len(new_ids) == 2)
    S.step("lint the questions of the chapter", "q", "lint", "99", expect=(0, 2), keep=6)
    key = {opt["text"]: opt["correct"] for q in common.read_json(inp / "questions.json") for opt in q["options"]}
    cite = {
        "Create a NAT gateway in each": ["vpc-natgw-az-scope"],
        "Keep the one NAT gateway": ["vpc-natgw-az-scope"],
        "Create two more NAT gateways": [{"source_id": S.NAT_SID, "quote": "Each NAT gateway is created in a specific Availability Zone"}],
        "Attach a security group": ["vpc-natgw-no-security-group"],
        "Replace the NAT gateway": ["vpc-natgw-bandwidth"],
        "Keep the NAT gateway,": [{"source_id": S.NAT_SID, "quote": "automatically scales up to 100 Gbps"}],
        "Associate a larger security group": ["vpc-natgw-no-security-group"],
        "Request a higher quota": ["vpc-natgw-per-az-quota"],
    }
    answer_files, orders = [], {}
    for lens in ("closed", "open", "ambiguity"):
        S.step(f"blind pack, lens {lens}", "q", "pack", "--chapter", "99", "--lens", lens, "--ids", *new_ids, "--out", t(f"pack-{lens}.json"), keep=2)
        pack = common.read_json(tmp / f"pack-{lens}.json") or {"items": []}
        leaked = [k for item in pack["items"] for k in item if k not in ("id", "type", "select", "stem", "options")]
        leaked += [k for item in pack["items"] for opt in item["options"] for k in opt if k not in ("label", "text")]
        S.check(f"the {lens} pack holds only id, type, select, stem and options", not leaked and len(pack["items"]) == 2)
        answers = []
        for item in pack["items"]:
            orders.setdefault(item["id"], []).append([opt["text"] for opt in item["options"]])
            row = {"id": item["id"], "answer": [opt["label"] for opt in item["options"] if key[opt["text"]]],
                   "flag": None, "stem_only": None, "citations": None, "case": None}
            if lens == "closed":
                row["stem_only"] = "Stated before the options were read."
            if lens == "open":
                row["citations"] = {opt["label"]: next(v for k, v in cite.items() if opt["text"].startswith(k)) for opt in item["options"]}
            if lens == "ambiguity":
                wrong = next(opt for opt in item["options"] if not key[opt["text"]])
                row["case"] = {"label": wrong["label"], "text": "The strongest case for this option still breaks a fact of the canon."}
            answers.append(row)
        path = tmp / f"answers-{lens}.json"
        common.write_json(path, {"pack": pack.get("pack"), "lens": lens, "solver": f"smoke-solver-{lens}", "answers": answers})
        answer_files.append(common.rel(path))
    S.check("the lenses do not all get the same option order", any(len({tuple(o) for o in v}) > 1 for v in orders.values()))
    code, res = S.step_json("adjudicate the three answer files", "q", "adjudicate", "--chapter", "99", "--answers", *answer_files,
                            expect=(0, 1))
    S.check("both questions pass the blind solve", bool(res) and sorted(res.get("pass", [])) == sorted(new_ids))
    S.step("list the questions", "q", "list", "--chapter", "99", keep=8)

    # ---- 5. a task
    S.step_json("add one small Look task", "tasks", "add", "--chapter", "99", "--file", f("task.json"), "--by", "smoke-writer")
    S.step("lint the tasks of the chapter (warnings allowed)", "tasks", "lint", "99", expect=(0, 2), keep=8)

    code, out, err = S.step("check the task commands against the AWS CLI model (uv helper; the fixture's invented `aws widget` "
                            "commands MUST FAIL, exit 5 means uv or the package index was not reachable)",
                            "tasks", "check-cli", "99", expect=(1, 5), keep=3)
    if code == 1:
        report = common.read_json(book / "_build" / "reports" / "cli" / "99.json") or {}
        real = [c for c in report.get("commands", []) if c.get("service") == "ec2"]
        S.check("the two real `aws ec2 describe-...` commands of the new task are ok", len(real) == 2 and all(c.get("ok") for c in real))

    # ---- 6. a diagram
    common.ensure_dir(book / "diagrams" / "src")
    shutil.copyfile(inp / "sample-natgw-zones.json", book / "diagrams" / "src" / "sample-natgw-zones.json")
    S.step("build one diagram (JSON spec to SVG)", "diagram", "build", "sample-natgw-zones", expect=(0, 2), keep=6)
    svg = book / "diagrams" / "svg" / "sample-natgw-zones.svg"
    S.check("the SVG exists and is an svg document", svg.exists() and "<svg" in svg.read_text(encoding="utf-8")[:400])

    # ---- 7. ledger: one stage cycle
    S.step("stage begin (verify-facts)", "stage", "begin", "99", "verify-facts", "--run", "smoke")
    code, out, err = S.step("stage end (runs the facts-final gate)", "stage", "end", "99", "verify-facts", "--note", "w0 smoke", expect=(0, 2))
    S.check("the stage passed", out.startswith("PASS") or '"PASS"' in out)
    S.step("MUST FAIL: begin a stage whose prerequisite has not passed", "stage", "begin", "99", "prose", expect=(3,), keep=3)
    S.step("stage show", "stage", "show", "99", keep=6)

    # ---- 8. the end state
    S.step("sync again", "sync", "99", keep=4)
    S.step("sync --check: generated files are fresh", "sync", "99", "--check", keep=4)
    S.step("gate lint", "gate", "99", "--gate", "lint", expect=(0, 2), keep=4)
    S.step("status", "status", keep=6)
