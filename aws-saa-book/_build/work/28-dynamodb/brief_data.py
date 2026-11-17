# Data of brief-28, split into parts; build_brief.py runs this file. Each part adds keys to BRIEF.
BRIEF = {}
for _part in ("brief_part_a.py", "brief_part_b.py", "brief_part_c.py", "brief_part_d.py", "brief_part_e.py", "brief_part_f.py"):
    exec((HERE / _part).read_text())
