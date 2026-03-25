"""Theme -- top-level frozen dataclass composing all palettes."""

from dataclasses import dataclass
from typing import Self

from palette.editor import EditorPalette
from palette.palette import Palette
from palette.syntax import SyntaxPalette


@dataclass(frozen=True)
class Theme:
    """Top-level theme: palette + syntax + editor + variant flag."""

    palette: Palette
    syntax: SyntaxPalette
    editor: EditorPalette
    is_dark: bool

    @classmethod
    def create(
        cls,
        *,
        accent_hue: float = 262.0,
        is_dark: bool = False,
    ) -> Self:
        """Build full theme chain from accent_hue + variant.

        Palette.for_light -> SyntaxPalette -> EditorPalette -> Theme.
        Raises NotImplementedError for is_dark=True.
        """
        if is_dark:
            raise NotImplementedError("Dark variant out of scope")

        palette = Palette.for_light(accent_hue)
        syntax = SyntaxPalette.create(
            background=palette.background,
        )
        editor = EditorPalette.create(syntax, palette)
        return cls(
            palette=palette,
            syntax=syntax,
            editor=editor,
            is_dark=False,
        )
