"""FontStyle -- text decoration enum for VS Code syntax token styling."""

from enum import StrEnum


class FontStyle(StrEnum):
    BOLD = "bold"
    ITALIC = "italic"
    ITALIC_BOLD = "italic bold"
    UNDERLINE = "underline"
    STRIKETHROUGH = "strikethrough"
    NONE = ""
