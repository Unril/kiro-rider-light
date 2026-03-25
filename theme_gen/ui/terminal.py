"""TerminalSection -- ANSI colors, cursor, selection, find, sticky scroll, command decorations.

ANSI color generation strategy for a light theme:
  6 chromatic hues at standard ANSI positions in OKLCH space.
  Normal: CIELab L*=45, chroma=0.15, WCAG AA floor (4.5:1 on white).
  Bright: CIELab L*=55, chroma=0.18, 3.0:1 floor (lighter for bold text).
  Black/white: achromatic at fixed OKLCH lightness levels.
"""

from dataclasses import dataclass
from typing import override

from core.tcol import TCol
from palette.theme import Theme
from ui.protocol import UISection

# Standard ANSI hue angles (OKLCH)
_HUE_RED = 25.0
_HUE_GREEN = 145.0
_HUE_YELLOW = 85.0
_HUE_BLUE = 260.0
_HUE_MAGENTA = 320.0
_HUE_CYAN = 195.0

# Normal: dark enough for white bg, WCAG AA
_NORMAL_LAB_L = 45.0
_NORMAL_CHROMA = 0.15
_NORMAL_FLOOR = 4.5

# Bright: lighter for bold/bright text
_BRIGHT_LAB_L = 55.0
_BRIGHT_CHROMA = 0.18
_BRIGHT_FLOOR = 3.0


@dataclass(frozen=True)
class AnsiColors:
    """16 ANSI terminal colors generated from standard hues."""

    black: TCol
    red: TCol
    green: TCol
    yellow: TCol
    blue: TCol
    magenta: TCol
    cyan: TCol
    white: TCol
    bright_black: TCol
    bright_red: TCol
    bright_green: TCol
    bright_yellow: TCol
    bright_blue: TCol
    bright_magenta: TCol
    bright_cyan: TCol
    bright_white: TCol

    @classmethod
    def for_light(cls, background: TCol) -> "AnsiColors":
        """Generate 16 ANSI colors for a light terminal background."""

        def _normal(hue: float) -> TCol:
            return TCol.from_lab_l(_NORMAL_LAB_L, _NORMAL_CHROMA, hue).with_min_contrast(background, _NORMAL_FLOOR)

        def _bright(hue: float) -> TCol:
            return TCol.from_lab_l(_BRIGHT_LAB_L, _BRIGHT_CHROMA, hue).with_min_contrast(background, _BRIGHT_FLOOR)

        return cls(
            black=TCol.from_oklch(0.25, 0.0, 0.0),
            red=_normal(_HUE_RED),
            green=_normal(_HUE_GREEN),
            yellow=_normal(_HUE_YELLOW),
            blue=_normal(_HUE_BLUE),
            magenta=_normal(_HUE_MAGENTA),
            cyan=_normal(_HUE_CYAN),
            white=TCol.from_oklch(0.80, 0.0, 0.0),
            bright_black=TCol.from_oklch(0.45, 0.0, 0.0),
            bright_red=_bright(_HUE_RED),
            bright_green=_bright(_HUE_GREEN),
            bright_yellow=_bright(_HUE_YELLOW),
            bright_blue=_bright(_HUE_BLUE),
            bright_magenta=_bright(_HUE_MAGENTA),
            bright_cyan=_bright(_HUE_CYAN),
            bright_white=TCol.from_oklch(0.95, 0.0, 0.0),
        )


class TerminalSection(UISection):
    @override
    def build(self, theme: Theme) -> dict[str, TCol]:
        p = theme.palette
        sel = theme.editor.selection
        ansi = AnsiColors.for_light(p.background)

        return {
            # Terminal foreground
            "terminal.foreground": p.foreground,
            # ANSI normal
            "terminal.ansiBlack": ansi.black,
            "terminal.ansiRed": ansi.red,
            "terminal.ansiGreen": ansi.green,
            "terminal.ansiYellow": ansi.yellow,
            "terminal.ansiBlue": ansi.blue,
            "terminal.ansiMagenta": ansi.magenta,
            "terminal.ansiCyan": ansi.cyan,
            "terminal.ansiWhite": ansi.white,
            # ANSI bright
            "terminal.ansiBrightBlack": ansi.bright_black,
            "terminal.ansiBrightRed": ansi.bright_red,
            "terminal.ansiBrightGreen": ansi.bright_green,
            "terminal.ansiBrightYellow": ansi.bright_yellow,
            "terminal.ansiBrightBlue": ansi.bright_blue,
            "terminal.ansiBrightMagenta": ansi.bright_magenta,
            "terminal.ansiBrightCyan": ansi.bright_cyan,
            "terminal.ansiBrightWhite": ansi.bright_white,
            # Cursor
            "terminalCursor.foreground": p.accent,
            "terminalCursor.background": p.background,
            # Selection -- match editor selection
            "terminal.selectionBackground": sel.primary,
            "terminal.inactiveSelectionBackground": sel.inactive,
            # Find -- must be transparent (VS Code spec)
            "terminal.findMatchBackground": sel.find_hl,
            "terminal.findMatchHighlightBackground": sel.find_hl,
            # Hover and sticky scroll
            "terminal.hoverHighlightBackground": p.hover_bg_opaque,
            "terminalStickyScroll.background": p.background,
            "terminalStickyScroll.border": p.border,
            "terminalStickyScrollHover.background": p.hover_bg_opaque,
            # Command decorations
            "terminalCommandDecoration.defaultBackground": p.fg_muted,
            "terminalCommandDecoration.successBackground": p.success,
            "terminalCommandDecoration.errorBackground": p.error,
            # Terminal background (panel content area)
            "terminal.background": p.background,
        }
