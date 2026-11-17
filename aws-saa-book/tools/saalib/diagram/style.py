"""Sizes, palettes and group conventions shared by layout, routing, SVG output and lint.

All lengths are SVG user units. One unit is one CSS pixel at scale 1; the web app never shows a
figure below scale 0.75.
"""
from __future__ import annotations

# ------------------------------------------------------------------ sizes
ICON = 48               # every icon is drawn at this size
NODE_FS = 13            # node label font size
NODE_LH = 16            # node label line height
LABEL_GAP = 5           # icon bottom to first label line
NODE_MAX_LINES = 2
BOX_H = 48              # height of a node drawn as a labelled box (no icon)
PORT_GAP = 3            # arrows stop this far from the icon or label
PORT_STEP = 12          # distance between two arrows on the same side of a node
PORT_MAX = 4            # arrows per side before the lint complains

GROUP_FS = 11.5
GROUP_BAND = 20         # label band: border to the next nested border, or to the cell
GROUP_TOP_IN = 4        # extra space between the innermost label band and the cell
GROUP_IN = 8            # innermost border to the cell (left, right, bottom)
GROUP_STEP = 10         # lane added per nested border (left, right, bottom)
GROUP_LABEL_INSET = 6
GROUP_LABEL_CLEAR = 3   # free space required between a group label and an edge

CELL_W = 132            # default column width
CELL_W_MAX = 220
CELL_W_STEP = 2
COL_GAP = 26            # routing gutter between two columns
ROW_GAP = 44            # routing gutter between two rows
TRACK = 9               # distance between two parallel edges in one gutter
TRACK_STEP_GAP = 48     # free stretch between edges of different steps that share one gutter track
MARGIN = 5
EMPH_PAD = 3           # highlight ring of an icon node: this far outside the icon; arrows stop at the ring

EDGE_FS = 12
EDGE_LABEL_H = 14
BADGE_R = 9
BADGE_FS = 11
ARROW_LEN = 9
ARROW_HALF = 4.5
BEND_R = 5
EDGE_W = 1.5
EDGE_W_EMPH = 2.25

MIN_SCALE = 0.75
PHONE_FIT = 334         # units a 368 px phone shows at scale 1 (card padding and border taken off)
PHONE_SCALE = 0.85      # a figure of size "s" must reach this scale on that phone
SIZE_BUDGET = {"s": 393, "m": 720, "l": 1040}    # widest drawing per size class, in units (s: PHONE_FIT / PHONE_SCALE)

# ------------------------------------------------------------------ limits (style guide)
MAX_NODES = 12
MAX_EDGES = 14
MAX_AZ = 2
MAX_CROSSINGS = 2
MAX_LABEL_WORDS = 4
MAX_EDGE_LABEL_WORDS = 3
MAX_EMPH = 4

# ------------------------------------------------------------------ palettes
# Token name -> value. Light is baked into standalone files; both are used by the preview page.
LIGHT = {
    "--dg-ink": "#141C2B", "--dg-muted": "#5A667A", "--dg-edge": "#4A5568", "--dg-emph": "#2A3EB1",
    "--dg-node": "#F2F4F8", "--dg-teal": "#00838A", "--dg-pub": "#5B8A0F", "--dg-vpc": "#8C4FFF",
    "--dg-sg": "#DD344C", "--dg-asg": "#C75B00", "--dg-acct": "#C2136B",
    "--dg-ground": "#FFFFFF", "--dg-show-light": "inline", "--dg-show-dark": "none",
}
DARK = {
    "--dg-ink": "#E7EBF3", "--dg-muted": "#98A4B8", "--dg-edge": "#AEB8C8", "--dg-emph": "#93A1FF",
    "--dg-node": "#1E2633", "--dg-teal": "#3CC9CB", "--dg-pub": "#A3CC4A", "--dg-vpc": "#B08CFF",
    "--dg-sg": "#FF7A8C", "--dg-asg": "#FF9A3D", "--dg-acct": "#FF6FB5",
    "--dg-ground": "#171D28", "--dg-show-light": "none", "--dg-show-dark": "inline",
}

# ------------------------------------------------------------------ group conventions
# type -> (css suffix, colour token, stroke width, dash array or "", tinted fill?, human name)
# Every type differs from the others by border pattern or weight as well as by colour.
GROUPS = {
    "region":                ("region", "--dg-teal",  1.5,  "1.5 4.5",          False, "Region: dotted teal"),
    "vpc":                   ("vpc",    "--dg-vpc",   2.0,  "",                 False, "VPC: solid purple, heavy"),
    "az":                    ("az",     "--dg-teal",  1.25, "9 5",              False, "Availability Zone: long dashes, teal"),
    "subnet-public":         ("pub",    "--dg-pub",   1.25, "",                 True,  "Public subnet: solid green, tinted"),
    "subnet-private":        ("priv",   "--dg-teal",  1.25, "10 3 2 3",         True,  "Private subnet: dash-dot teal, tinted"),
    "security-group":        ("sg",     "--dg-sg",    1.25, "4 3",              False, "Security group: short dashes, red"),
    "auto-scaling-group":    ("asg",    "--dg-asg",   1.25, "8 3 2 3 2 3",      False, "Auto Scaling group: dash-dot-dot orange"),
    "account":               ("acct",   "--dg-acct",  1.25, "14 3 5 3",         False, "AWS account: long-short dashes, pink"),
    "corporate-data-center": ("dc",     "--dg-muted", 1.25, "18 4",             True,  "Corporate data center: very long dashes, grey, tinted"),
    "generic":               ("gen",    "--dg-muted", 1.25, "3 5",              False, "Generic group: sparse dashes, grey"),
}


def fmt(value: float) -> str:
    """Stable number formatting for SVG output: at most one decimal, no trailing zero."""
    text = f"{round(float(value) + 0.0, 1):.1f}"
    if text.endswith(".0"):
        text = text[:-2]
    return "0" if text == "-0" else text
