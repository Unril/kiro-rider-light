"""ListSection -- list/tree, activity bar, sidebar.

GitHub Light pattern: activity bar is white (bgColor-default).
Sidebar is muted (bgColor-muted). One border color everywhere.
"""

from typing import override

from core.tcol import TCol
from palette.theme import Theme
from ui.protocol import UISection


class ListSection(UISection):
    @override
    def build(self, theme: Theme) -> dict[str, TCol]:
        p = theme.palette
        fg = p.foreground

        return {
            # Lists — selection is darker than hover for clear distinction
            "list.activeSelectionBackground": p.selection_bg,
            "list.activeSelectionForeground": fg,
            "list.focusBackground": p.drop_bg,
            "list.focusForeground": fg,
            "list.hoverBackground": p.hover_bg,
            "list.hoverForeground": fg,
            "list.inactiveSelectionBackground": p.selection_bg,
            "list.inactiveSelectionForeground": fg,
            "list.highlightForeground": p.accent,
            "list.activeSelectionIconForeground": fg,
            "list.errorForeground": p.error,
            "list.warningForeground": p.warning,
            "list.focusOutline": p.accent,
            "list.focusAndSelectionOutline": p.accent,
            "list.focusHighlightForeground": p.accent,
            "list.filterMatchBackground": p.secondary.a15,
            "list.dropBackground": p.hover_bg,
            "list.inactiveFocusBackground": p.drop_bg,
            "tree.indentGuidesStroke": p.border,
            # Activity Bar — WHITE background (bgColor-default)
            "activityBar.background": p.background,
            "activityBar.foreground": fg,
            "activityBar.inactiveForeground": p.fg_muted,
            "activityBar.border": p.border,
            "activityBar.activeBorder": p.accent,
            "activityBar.activeBackground": p.selection_bg,
            "activityBarBadge.background": p.accent,
            "activityBarBadge.foreground": p.fg_on_accent,
            # Activity Bar Top (when positioned at top)
            "activityBarTop.foreground": fg,
            "activityBarTop.inactiveForeground": p.fg_muted,
            "activityBarTop.activeBorder": p.accent,
            "activityBarTop.background": p.background,
            "activityBarTop.activeBackground": p.selection_bg,
            # Side Bar — white tree area, muted header
            "sideBar.background": p.background,
            "sideBar.foreground": fg,
            "sideBar.border": p.border,
            "sideBarTitle.foreground": fg,
            "sideBarTitle.background": p.panel_bg,
            "sideBarSectionHeader.foreground": fg,
            "sideBarSectionHeader.background": p.panel_bg,
            "sideBarSectionHeader.border": p.border,
            "sideBar.dropBackground": p.hover_bg,
            # Sticky scroll in sidebar
            "sideBarStickyScroll.background": p.background,
            "sideBarStickyScroll.border": p.border,
        }
