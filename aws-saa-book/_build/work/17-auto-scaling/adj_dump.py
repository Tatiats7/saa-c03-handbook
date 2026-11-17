"""Read-only: dump disputed facts of chapter 17 with their non-positive votes (adjudicate-17)."""
import json, sys, pathlib

ROOT = pathlib.Path(__file__).resolve().parents[3]
out = pathlib.Path(sys.argv[1])
status_want = sys.argv[2] if len(sys.argv) > 2 else "disputed"
lines = []
for svc in ("ec2-auto-scaling", "aws-auto-scaling"):
    facts = [json.loads(l) for l in (ROOT / "data/facts" / f"{svc}.jsonl").read_text().splitlines() if l.strip()]
    votes = [json.loads(l) for l in (ROOT / "_build/facts/votes" / f"{svc}.jsonl").read_text().splitlines() if l.strip()]
    for f in facts:
        if f.get("home_chapter") != "17" or f.get("status") != status_want:
            continue
        lines.append("=" * 100)
        lines.append(f"ID {f['id']}  rev={f['rev']} repairs={f.get('repairs', 0)} kind={f['kind']} hard={f['hard']} vol={f.get('volatility')} changed={f.get('changed')}")
        lines.append(f"CLAIM: {f['claim']}")
        lines.append(f"QUESTION: {f.get('question')}")
        lines.append("VALUES: " + json.dumps(f.get("values"), ensure_ascii=False))
        lines.append("QUAL: " + json.dumps(f.get("qualifiers"), ensure_ascii=False))
        if f.get("derivation"):
            lines.append("DERIV: " + json.dumps(f.get("derivation"), ensure_ascii=False))
        if f.get("change_items"):
            lines.append("CHANGE_ITEMS: " + json.dumps(f.get("change_items"), ensure_ascii=False))
        for e in f.get("evidence", []):
            lines.append(f"  EV [{e['source_id']}] th={e.get('table_header')} h={e.get('heading')}")
            lines.append(f"     Q: {e['quote'][:700]}")
        for v in votes:
            if v["fact"] == f["id"] and v["rev"] == f["rev"]:
                lines.append(f"  VOTE {v['lens']} {v['verdict']} by {v['voter']}: {v.get('reason')}")
                if v.get("quote"):
                    lines.append(f"     VQ [{v.get('source_id')}]: {v['quote'][:500]}")
out.write_text("\n".join(lines) + "\n")
print(f"wrote {out}")
