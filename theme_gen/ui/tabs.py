"""TabSection -- editor groups, tabs, breadcrumbs.

GitHub Light pattern: tabs container is muted, active tab is white with accent top border.
Tab separators use borderColor-default. Borders everywhere, same color.
"""

from typing import override

from core.tcol import TCol
from palette.theme import Theme
from ui.protocol import UISection


class TabSection(UISection):
    @override
    def build(self, theme: Theme) -> dict[str, TCol]:
        p = theme.palette
        fg = p.foreground
        editor_bg = p.background

        return {
            # Editor groups
            "editorGroup.border": p.border,
            "editorGroup.dropBackground": p.drop_bg,
            "editorGroup.focusedEmptyBorder": p.accent,
            # Tab container — white, same as editor
            "editorGroupHeader.tabsBackground": editor_bg,
            "editorGroupHeader.tabsBorder": p.border,
            # Active tab — white bg, accent TOP border
            "tab.activeBackground": editor_bg,
            "tab.activeForeground": fg,
            "tab.activeBorderTop": p.accent,
            "tab.activeBorder": editor_bg,
            "tab.unfocusedActiveBorder": editor_bg,
            "tab.unfocusedActiveBorderTop": p.border,
            # Inactive tab — light grey to distinguish from active white
            "tab.inactiveBackground": p.panel_bg,
            "tab.inactiveForeground": p.fg_muted,
            # Tab separators — same border color as everything
            "tab.border": p.border,
            # Hover — opaque light blue
            "tab.hoverBackground": p.hover_bg_opaque,
            "tab.hoverForeground": fg,
            "tab.unfocusedHoverBackground": p.hover_bg_opaque,
            # Unfocused
            "tab.unfocusedActiveForeground": fg,
            "tab.unfocusedInactiveForeground": p.fg_disabled,
            # Modified indicators
            "tab.activeModifiedBorder": p.secondary,
            "tab.unfocusedActiveModifiedBorder": p.secondary.a50,
            # Breadcrumbs — readable path, accent on focus
            "breadcrumb.foreground": p.fg_muted,
            "breadcrumb.focusForeground": fg,
            "breadcrumb.activeSelectionForeground": fg,
            "breadcrumb.background": editor_bg,
        }
