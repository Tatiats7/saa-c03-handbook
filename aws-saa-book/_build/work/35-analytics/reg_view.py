"""register-35: print parts of reg-build-report.json (read-only). Arg: refused | displays | dropped"""
import json, sys

R = json.load(open("/Users/tatiatsmindashvili/Desktop/tatia/2026-plans/aws-saa-book/_build/work/35-analytics/reg-build-report.json"))
what = sys.argv[1]
if what == "refused":
    for r in R["refused"]:
        print(json.dumps(r, ensure_ascii=False)[:1500])
elif what == "displays":
    for fid, a, b in R["display_changes"]:
        if b is not None:
            print("%s\n   %s\n-> %s" % (fid, a, b))
elif what == "dropped":
    for fid, a, b in R["display_changes"]:
        if b is None:
            print(fid, "|", a)
