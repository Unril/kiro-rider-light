"""DebugSection -- debug toolbar, console, token expressions, icons."""

from typing import override

from core.tcol import TCol
from palette.theme import Theme
from ui.protocol import UISection


class DebugSection(UISection):
    @override
    def build(self, theme: Theme) -> dict[str, TCol]:
        p = theme.palette
        s = theme.syntax
        fg = p.foreground

        return {
            # Debug toolbar
            "debugToolBar.background": p.panel_bg,
            # Debug console
            "debugConsole.infoForeground": fg,
            "debugConsole.warningForeground": p.warning,
            "debugConsole.errorForeground": p.error,
            "debugConsole.sourceForeground": p.fg_muted,
            "debugConsoleInputIcon.foreground": p.accent,
            # Debug token expressions (Variables/Watch view)
            "debugTokenExpression.name": s.field,
            "debugTokenExpression.type": s.type,
            "debugTokenExpression.value": s.foreground,
            "debugTokenExpression.string": s.string,
            "debugTokenExpression.number": s.number,
            "debugTokenExpression.boolean": s.keyword,
            "debugTokenExpression.error": p.error,
            # Debug view labels
            "debugView.exceptionLabelBackground": p.error.a15,
            "debugView.exceptionLabelForeground": p.error,
            "debugView.stateLabelBackground": p.accent.a15,
            "debugView.stateLabelForeground": p.accent,
            "debugView.valueChangedHighlight": p.accent.a25,
            # Debug exception widget
            "debugExceptionWidget.background": p.error_bg,
            "debugExceptionWidget.border": p.error_border,
            # Debug icons
            "debugIcon.breakpointForeground": p.error,
            "debugIcon.breakpointDisabledForeground": p.fg_disabled,
            "debugIcon.breakpointUnverifiedForeground": p.fg_muted,
            "debugIcon.breakpointCurrentStackframeForeground": p.warning,
            "debugIcon.breakpointStackframeForeground": p.success,
            "debugIcon.startForeground": p.success,
            "debugIcon.continueForeground": p.accent,
            "debugIcon.pauseForeground": p.accent,
            "debugIcon.stepOverForeground": p.accent,
            "debugIcon.stepIntoForeground": p.accent,
            "debugIcon.stepOutForeground": p.accent,
            "debugIcon.stepBackForeground": p.accent,
            "debugIcon.restartForeground": p.success,
            "debugIcon.stopForeground": p.error,
            "debugIcon.disconnectForeground": p.error,
        }
