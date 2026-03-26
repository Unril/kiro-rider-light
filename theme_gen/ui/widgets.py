"""WidgetSection -- editor widgets, suggest, peek, quick picker, notifications, settings.

Border philosophy: widgets use shadow for separation, not borders.
Only peek view uses accent border as a design element.
"""

from typing import override

from core.tcol import TCol
from palette.theme import Theme
from ui.protocol import UISection


class WidgetSection(UISection):
    @override
    def build(self, theme: Theme) -> dict[str, TCol]:
        p = theme.palette
        e = theme.editor
        fg = p.foreground

        return {
            "editorWidget.background": p.background,
            "editorWidget.border": p.border,
            "editorSuggestWidget.background": p.background,
            "editorSuggestWidget.border": p.border,
            "editorSuggestWidget.foreground": fg,
            "editorSuggestWidget.selectedBackground": p.selection_bg,
            "editorSuggestWidget.highlightForeground": p.accent,
            "editorSuggestWidget.focusHighlightForeground": p.accent,
            # Hover widget — slightly elevated surface
            "editorHoverWidget.background": p.panel_bg,
            "editorHoverWidget.border": p.border,
            "editorHoverWidget.foreground": fg,
            "editorHoverWidget.highlightForeground": p.accent,
            # Quick input / command palette
            "quickInput.background": p.background,
            "quickInput.foreground": fg,
            # Peek view — accent border is intentional design element
            "peekView.border": p.accent,
            "peekViewEditor.background": p.panel_bg,
            "peekViewResult.background": p.panel_bg,
            "peekViewTitle.background": p.panel_bg,
            "peekViewResult.selectionBackground": p.selection_bg,
            "peekViewResult.selectionForeground": fg,
            "peekViewTitleLabel.foreground": fg,
            "peekViewTitleDescription.foreground": p.fg_muted,
            "peekViewResult.fileForeground": fg,
            "peekViewResult.lineForeground": p.fg_muted,
            "peekViewEditor.matchHighlightBackground": e.widgets.peek_match_hl,
            "peekViewResult.matchHighlightBackground": e.widgets.peek_match_hl,
            # Notifications — white bg, NO border (shadow handles it)
            "notifications.background": p.background,
            "notifications.foreground": fg,
            "notificationCenterHeader.background": p.background,
            "notificationCenterHeader.foreground": fg,
            "notificationsErrorIcon.foreground": p.error,
            "notificationsWarningIcon.foreground": p.warning,
            "notificationsInfoIcon.foreground": p.accent,
            "notificationLink.foreground": p.accent,
            "notificationCenter.border": p.border,
            "notificationToast.border": p.border,
            # Quick picker
            "quickInputList.focusBackground": p.selection_bg,
            "pickerGroup.border": p.border,
            "pickerGroup.foreground": p.fg_muted,
            # Toolbar
            "toolbar.hoverBackground": p.hover_bg,
            "toolbar.activeBackground": p.selection_bg,
            # Search editor
            "searchEditor.textInputBorder": p.border,
            # Input option hover
            "inputOption.hoverBackground": p.hover_bg,
            # Settings
            "settings.dropdownBackground": p.background,
            "settings.dropdownBorder": p.border,
            "settings.headerForeground": fg,
            "settings.numberInputBorder": p.border,
            "settings.textInputBorder": p.border,
            "settings.modifiedItemIndicator": e.widgets.settings_modified,
            "settings.rowHoverBackground": p.hover_bg,
            # Welcome page
            "welcomePage.tileBackground": p.panel_bg,
            "welcomePage.tileHoverBackground": p.hover_bg,
            # Action bar
            "actionBar.toggledBackground": p.border,
        }
