"""ColorMapComposition -- merges UI sections and detects key conflicts."""

from core.tcol import TCol
from palette.theme import Theme
from ui.protocol import UISection


class ColorMapComposition:
    """Collects UISection instances and merges their dicts."""

    def __init__(self, sections: list[UISection]) -> None:
        self._sections: list[UISection] = sections

    def build(self, theme: Theme) -> dict[str, TCol]:
        result: dict[str, TCol] = {}
        seen: dict[str, str] = {}  # key -> section class name

        for section in self._sections:
            section_name = type(section).__name__
            colors = section.build(theme)
            for key, value in colors.items():
                if key in seen:
                    raise ValueError(f"Duplicate color key '{key}' in {section_name} (already set by {seen[key]})")
                seen[key] = section_name
                result[key] = value

        return result
