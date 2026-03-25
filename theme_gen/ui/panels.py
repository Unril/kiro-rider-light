"""PanelSection -- panel, status bar, title bar, menu, command center, debug console.

GitHub Light pattern: status bar and title bar are WHITE (bgColor-default).
Panel is muted. Borders everywhere, same color.
"""

from typing import override

from core.tcol import TCol
from palette.theme import Theme
from ui.protocol import UISection


class PanelSection(UISection):
    @override
    def build(self, theme: Theme) -> dict[str, TCol]:
        p = theme.palette
        e = theme.editor
        fg = p.foreground

        return {
            # Panel — white content, muted section headers
            "panel.background": p.background,
            "panel.border": p.border,
            "panelTitle.activeBorder": p.accent,
            "panelTitle.activeForeground": fg,
            "panelTitle.activeBackground": p.panel_bg,
            "panelTitle.inactiveForeground": p.fg_muted,
            "panelTitle.border": p.border,
            "panelInput.border": p.border,
            "panelSectionHeader.background": p.panel_bg,
            "panelSectionHeader.foreground": fg,
            "panelSectionHeader.border": p.border,
            "panelSection.border": p.border,
            # Panel content areas
            "outputView.background": p.background,
            # Sticky scroll in panel
            "panelStickyScroll.background": p.background,
            "panelStickyScroll.border": p.border,
            # Status Bar — WHITE background (bgColor-default)
            "statusBar.background": p.background,
            "statusBar.foreground": fg,
            "statusBar.border": p.border,
            "statusBar.debuggingBackground": e.chrome.debug_bg,
            "statusBar.debuggingForeground": p.fg_on_accent,
            "statusBar.noFolderBackground": p.background,
            "statusBar.focusBorder": p.accent.a50,
            "statusBarItem.hoverBackground": p.hover_bg,
            "statusBarItem.hoverForeground": fg,
            "statusBarItem.activeBackground": p.selection_bg,
            "statusBarItem.compactHoverBackground": p.border,
            "statusBarItem.focusBorder": p.accent,
            "statusBarItem.errorBackground": e.widgets.status_error_bg,
            "statusBarItem.prominentBackground": p.hover_bg,
            "statusBarItem.remoteBackground": p.hover_bg,
            "statusBarItem.remoteForeground": fg,
            # Title Bar — white, stays white when unfocused (only text dims)
            "titleBar.activeBackground": p.background,
            "titleBar.activeForeground": fg,
            "titleBar.inactiveBackground": p.background,
            "titleBar.inactiveForeground": p.fg_muted,
            "titleBar.border": p.border,
            # Menu
            "menu.selectionBackground": p.selection_bg,
            "menu.selectionForeground": fg,
            "menu.separatorBackground": p.border,
            "menubar.selectionBackground": p.selection_bg,
            "menubar.selectionForeground": fg,
            # Command Center
            "commandCenter.foreground": fg,
            "commandCenter.activeForeground": fg,
            "commandCenter.background": p.background,
            "commandCenter.activeBackground": p.background,
            "commandCenter.border": p.border,
            "commandCenter.activeBorder": p.accent,
            "commandCenter.inactiveForeground": p.fg_muted,
            "commandCenter.inactiveBorder": p.border,
        }
