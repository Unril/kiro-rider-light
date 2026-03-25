"""Palette -- central seed values derived from accent_hue + variant parameters."""

from dataclasses import dataclass
from typing import Self

from core.tcol import TCol

# Status color hues (OKLCH, fixed by convention)
_HUE_ERROR = 20.0
_HUE_WARNING = 75.0
_HUE_SUCCESS = 150.0

# Chroma levels (base chroma is at s500 peak; steps scale from this)
_CHROMA_VIVID = 0.163

# Secondary accent offset (complementary hue)
_SECONDARY_HUE_OFFSET = 180.0


@dataclass(frozen=True)
class Palette:
    """Seed values + derived chromatic alpha variants for a theme variant."""

    # 5 chromatic anchors (opaque)
    accent: TCol
    secondary: TCol
    error: TCol
    warning: TCol
    success: TCol

    # Surfaces (achromatic)
    foreground: TCol
    background: TCol
    panel_bg: TCol
    border: TCol

    # Foreground variants
    fg_muted: TCol
    fg_disabled: TCol
    fg_icon: TCol
    fg_on_accent: TCol

    # Interactive surfaces (list/tree hover, selection, line highlight)
    hover_bg: TCol
    selection_bg: TCol
    line_highlight: TCol

    # Derived: accent
    link: TCol
    accent_hover: TCol

    # Validation backgrounds and borders
    error_bg: TCol
    error_border: TCol
    warn_bg: TCol
    warn_border: TCol
    info_bg: TCol
    info_border: TCol

    # Gutter / diff markers
    gutter_add: TCol
    gutter_mod: TCol
    gutter_del: TCol
    diff_insert: TCol
    diff_remove: TCol

    # Minimap highlights
    minimap_error: TCol
    minimap_warning: TCol
    minimap_slider: TCol

    # Scrollbar
    scrollbar_thumb: TCol
    scrollbar_hover: TCol
    scrollbar_active: TCol

    # UI chrome (neutral derived)
    btn_secondary_bg: TCol
    text_separator: TCol
    status_prominent_bg: TCol

    # Reusable overlays and tints
    shadow: TCol  # fg @ 15% -- widget shadow, button border, preformat bg
    drop_bg: TCol  # accent @ 15% -- drop targets, focus backgrounds, slash cmd bg
    accent_wash: TCol  # accent @ 5% -- very faint accent tint (chat request bg)
    hover_bg_opaque: TCol  # accent s100 -- opaque accent tint for terminal/sticky hover

    @classmethod
    def for_light(cls, accent_hue: float = 262.0) -> Self:
        """Light variant: derive all fields from accent_hue.

        Surface hierarchy:
          L=1.00  editor background, inputs, sidebar tree, active tab
          L=0.98  line highlight
          L=0.96  inactive tabs, tab container, panel headers
          L=0.90  borders, dividers

        Foreground hierarchy:
          L=0.20  foreground, icons (near-black)
          L=0.56  muted text (descriptions, inactive tabs, line numbers)
          L=0.72  disabled text (placeholders, ghost text)
        """
        accent_base = TCol.from_oklch(0.50, _CHROMA_VIVID, accent_hue)
        secondary_base = TCol.from_oklch(0.50, _CHROMA_VIVID, accent_hue + _SECONDARY_HUE_OFFSET)
        neutral = TCol.from_oklch(0.50, 0.0, 0.0)

        # Surfaces — GitHub Light inspired: two bg levels + one border color
        white = TCol.from_oklch(1.0, 0.0, 0.0)  # editor, activity bar, status bar, active tab
        panel = TCol.from_oklch(0.96, 0.0, 0.0)  # sidebar, tabs container, panel, inactive tab
        line_hl = TCol.from_oklch(0.98, 0.0, 0.0)  # editor line highlight
        border_val = TCol.from_oklch(0.88, 0.0, 0.0)  # borders, dividers

        # Foregrounds — darker than before for better contrast (Rider uses #000000)
        fg = TCol.from_oklch(0.20, 0.0, 0.0)

        accent = accent_base.s600
        secondary = secondary_base.s600
        error_base = TCol.from_oklch(0.50, _CHROMA_VIVID, _HUE_ERROR)
        warning_base = TCol.from_oklch(0.50, _CHROMA_VIVID, _HUE_WARNING)
        success_base = TCol.from_oklch(0.50, _CHROMA_VIVID, _HUE_SUCCESS)
        error = error_base.s600
        warning = warning_base.s400.with_min_contrast(white, 4.5)
        success = success_base.s600.with_min_contrast(white, 4.5)

        return cls(
            accent=accent,
            secondary=secondary,
            error=error,
            warning=warning,
            success=success,
            foreground=fg,
            background=white,
            panel_bg=panel,
            border=border_val,
            fg_muted=neutral.s600.with_min_contrast(white, 4.5),
            fg_disabled=neutral.s400,
            fg_icon=fg,
            fg_on_accent=white,
            hover_bg=accent.with_alpha(0.08),
            selection_bg=accent.with_alpha(0.15),
            line_highlight=line_hl,
            link=accent_base.s800,
            accent_hover=accent_base.s500,
            error_bg=error.a05,
            error_border=error.a50,
            warn_bg=warning.a05,
            warn_border=warning.a50,
            info_bg=accent.a05,
            info_border=accent.a50,
            gutter_add=success.a50,
            gutter_mod=accent.a50,
            gutter_del=error.a50,
            diff_insert=success.a15,
            diff_remove=error.a15,
            minimap_error=error.a80,
            minimap_warning=warning.a80,
            minimap_slider=neutral.s400.a25,
            scrollbar_thumb=fg.a25,
            scrollbar_hover=fg.a50,
            scrollbar_active=fg.a80,
            btn_secondary_bg=neutral.s100,
            text_separator=fg,
            status_prominent_bg=accent.muted.s600.a50,
            shadow=fg.a15,
            drop_bg=accent.a15,
            accent_wash=accent.a05,
            hover_bg_opaque=accent.s100,
        )

    @classmethod
    def for_dark(cls, _accent_hue: float = 262.0) -> Self:
        """Dark variant -- not yet implemented."""
        raise NotImplementedError("Dark variant out of scope")
