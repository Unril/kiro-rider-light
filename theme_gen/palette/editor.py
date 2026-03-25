"""EditorPalette -- editor chrome colors derived from palette base colors.

All values are derived from Palette seed colors using TCol lightness/chroma/alpha
steps. No hardcoded hex values.

Sub-palettes group related fields:
  SymbolColors   -- symbol icon colors mapped from syntax roles
  OutputColors   -- terminal/output panel log-level tokens
  EditorChrome   -- caret, line numbers, brackets, guides, inlay hints
  SelectionColors -- selection, word highlights, find matches (transparent)
  WidgetColors   -- status bar, peek view, settings, chat, notebook
"""

from dataclasses import dataclass
from typing import Self

from core.tcol import TCol
from palette.palette import Palette
from palette.syntax import SyntaxPalette


@dataclass(frozen=True)
class SymbolColors:
    """Symbol icon colors mapped from syntax roles."""

    cls: TCol  # class/struct
    function: TCol
    interface: TCol
    variable: TCol
    constant: TCol
    enum: TCol
    enum_member: TCol
    property: TCol
    keyword: TCol
    namespace: TCol
    string: TCol
    number: TCol


@dataclass(frozen=True)
class OutputColors:
    """Terminal and output panel log-level token colors."""

    info: TCol
    warn: TCol
    error: TCol
    debug: TCol


@dataclass(frozen=True)
class EditorChrome:
    """Editor surface colors: caret, guides, brackets, inlay hints."""

    caret: TCol
    caret_row: TCol
    line_num: TCol
    indent_guide: TCol
    indent_guide_active: TCol
    bracket_match: TCol
    bracket_match_border: TCol
    whitespace: TCol
    ruler: TCol
    inlay_bg: TCol
    inlay_fg: TCol
    codelens: TCol
    info_fg: TCol
    stack_frame: TCol
    stack_focused: TCol
    debug_bg: TCol


@dataclass(frozen=True)
class SelectionColors:
    """Selection and highlight colors (transparent -- must not hide decorations)."""

    primary: TCol  # editor selection
    inactive: TCol  # inactive editor selection
    highlight: TCol  # other occurrences of selected text
    word_read: TCol  # symbol read-access highlight
    word_write: TCol  # symbol write-access highlight
    word_text: TCol  # textual occurrence highlight (secondary accent)
    hover_bg: TCol  # range/hover highlight
    find_match: TCol  # current find match
    find_hl: TCol  # other find matches
    find_ruler: TCol  # find match in overview ruler


@dataclass(frozen=True)
class WidgetColors:
    """UI chrome: status bar, peek view, settings, chat, notebook."""

    status_error_bg: TCol
    peek_match_hl: TCol
    settings_modified: TCol
    chat_edited_fg: TCol
    notebook_cell_bg: TCol
    slash_cmd_fg: TCol
    chat_lines_add: TCol
    chat_lines_remove: TCol


@dataclass(frozen=True)
class EditorPalette:
    """Editor chrome colors bridging syntax and UI.

    Composed of five sub-palettes for logical grouping.
    Consumers access fields via sub-palette: ``e.chrome.caret``, ``e.selection.primary``, etc.
    """

    symbols: SymbolColors
    output: OutputColors
    chrome: EditorChrome
    selection: SelectionColors
    widgets: WidgetColors

    @classmethod
    def create(cls, syntax: SyntaxPalette, palette: Palette) -> Self:
        """Derive all editor chrome from palette base colors."""
        accent = palette.accent
        secondary = palette.secondary
        warning = palette.warning
        success = palette.success
        error = palette.error

        # Bracket match uses a pink-shifted accent for visual distinction
        bracket_base = secondary.much_lighter

        return cls(
            symbols=SymbolColors(
                cls=syntax.type,
                function=syntax.function,
                interface=syntax.type,
                variable=syntax.field,
                constant=syntax.field,
                enum=syntax.type,
                enum_member=syntax.enum_member,
                property=syntax.field,
                keyword=syntax.keyword,
                namespace=syntax.namespace,
                string=syntax.string,
                number=syntax.number,
            ),
            output=OutputColors(
                info=accent,
                warn=warning,
                error=error,
                debug=palette.fg_muted,
            ),
            chrome=EditorChrome(
                caret=accent,
                caret_row=palette.foreground.a05,
                line_num=palette.fg_disabled,
                indent_guide=palette.foreground.a15,
                indent_guide_active=palette.foreground.a25,
                whitespace=palette.fg_disabled,
                ruler=palette.foreground.a15,
                inlay_bg=palette.panel_bg,
                inlay_fg=palette.fg_muted,
                codelens=palette.fg_muted,
                info_fg=palette.fg_muted,
                bracket_match=bracket_base.muted,
                bracket_match_border=bracket_base.soft,
                stack_frame=warning.much_lighter.muted,
                stack_focused=success.much_lighter.muted,
                debug_bg=success.muted,
            ),
            selection=SelectionColors(
                primary=accent.a15,
                inactive=accent.a50,
                highlight=accent.a15,
                word_read=accent.a25,
                word_write=accent.a25,
                word_text=secondary.a15,
                hover_bg=accent.a05,
                find_match=accent.much_lighter.soft,
                find_hl=warning.a25,
                find_ruler=warning.a50,
            ),
            widgets=WidgetColors(
                status_error_bg=error.vivid,
                peek_match_hl=warning.a25,
                settings_modified=secondary.vivid,
                chat_edited_fg=secondary.s700,
                notebook_cell_bg=accent.much_lighter.muted.a80,
                slash_cmd_fg=accent.darker.vivid,
                chat_lines_add=success.a80,
                chat_lines_remove=error.a80,
            ),
        )
