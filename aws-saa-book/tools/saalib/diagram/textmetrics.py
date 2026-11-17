"""Text measurement for the diagram renderer. Standard library only.

Widths come from a committed table of real Arial advance widths (see _widths.py, generated once
with fontTools by tools/helpers/gen_font_widths.py). Diagram text is set in the stack
"Helvetica Neue", Helvetica, Arial, sans-serif; Helvetica and Arial share metrics. SAFETY covers
other fallbacks (for example Roboto) and sub-pixel rounding.
"""
from __future__ import annotations

from . import _widths

SAFETY = 1.05           # multiply every measured width by this margin
FALLBACK = 600          # 1/1000 em for a character missing from the table (wide on purpose)
FONT_STACK = '"Helvetica Neue",Helvetica,Arial,sans-serif'


def text_width(text: str, size: float, bold: bool = False) -> float:
    """Width of one line of text in user units, with the safety margin applied."""
    table = _widths.BOLD if bold else _widths.REGULAR
    total = 0
    for ch in text:
        total += table.get(ch, FALLBACK)
    return total * size / 1000.0 * SAFETY


def wrap(text: str, size: float, max_width: float, bold: bool = False) -> list:
    """Greedy word wrap. An explicit newline in the text always breaks. Words are never split,
    so a returned line can still be wider than max_width; the lint reports that."""
    lines = []
    for para in text.split("\n"):
        words = para.split()
        if not words:
            continue
        cur = words[0]
        for word in words[1:]:
            trial = cur + " " + word
            if text_width(trial, size, bold) <= max_width:
                cur = trial
            else:
                lines.append(cur)
                cur = word
        lines.append(cur)
    return lines or [""]
