"""BaseSection -- root colors, text, button, input, dropdown, scrollbar, badge, progress."""

from typing import override

from core.tcol import TCol
from palette.theme import Theme
from ui.protocol import UISection


class BaseSection(UISection):
    @override
    def build(self, theme: Theme) -> dict[str, TCol]:
        p = theme.palette
        fg = p.foreground

        return {
            "foreground": fg,
            "accent": p.accent,
            "background": p.background,
            "focusBorder": p.accent,
            "sash.hoverBorder": p.accent,
            "widget.shadow": p.shadow,
            "widget.border": p.border,
            "selection.background": p.selection_bg,
            "icon.foreground": p.fg_icon,
            "descriptionForeground": fg,
            "errorForeground": p.error,
            "disabledForeground": p.fg_disabled,
            # Text
            "textLink.foreground": p.accent,
            "textLink.activeForeground": p.accent,
            "textBlockQuote.background": p.panel_bg,
            "textBlockQuote.border": p.border,
            "textCodeBlock.background": p.panel_bg,
            "textPreformat.foreground": fg,
            "textPreformat.background": p.shadow,
            "textSeparator.foreground": p.text_separator,
            # Button
            "button.background": p.accent,
            "button.foreground": p.fg_on_accent,
            "button.border": p.shadow,
            "button.hoverBackground": p.accent_hover,
            "button.secondaryBackground": p.btn_secondary_bg,
            "button.secondaryForeground": fg,
            "button.secondaryHoverBackground": p.drop_bg,
            # Input
            "input.background": p.background,
            "input.border": p.border,
            "input.foreground": fg,
            "input.placeholderForeground": p.fg_muted,
            "inputOption.activeBorder": p.accent,
            "inputOption.activeBackground": p.selection_bg,
            "inputOption.activeForeground": fg,
            "inputValidation.errorBackground": p.error_bg,
            "inputValidation.errorBorder": p.error_border,
            "inputValidation.warningBackground": p.warn_bg,
            "inputValidation.warningBorder": p.warn_border,
            "inputValidation.infoBackground": p.info_bg,
            "inputValidation.infoBorder": p.info_border,
            # Dropdown (menu inherits from these)
            "dropdown.background": p.background,
            "dropdown.border": p.border,
            "dropdown.foreground": fg,
            # Scrollbar
            "scrollbar.shadow": p.shadow,
            "scrollbarSlider.background": p.scrollbar_thumb,
            "scrollbarSlider.hoverBackground": p.scrollbar_hover,
            "scrollbarSlider.activeBackground": p.scrollbar_active,
            # Badge / Progress
            "badge.background": p.accent,
            "badge.foreground": p.fg_on_accent,
            "progressBar.background": p.accent,
            # Keybinding
            "keybindingLabel.foreground": fg,
        }
