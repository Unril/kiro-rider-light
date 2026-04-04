#!/usr/bin/env -S uv run --script

"""Generate the Kiro Rider Light and Dark VS Code color theme JSON files."""

import json
from pathlib import Path

from css.markdown_variables import build_css as build_markdown_css
from lang.base import BaseSyntax
from lang.css import CssLang
from lang.html import HtmlLang
from lang.java import JavaLang
from lang.js import JavaScriptLang
from lang.json_lang import JsonLang
from lang.kotlin import KotlinLang
from lang.markdown import MarkdownLang
from lang.python import PythonLang
from lang.registry import LanguageRegistry
from lang.script import ScriptLang
from lang.semantic import GlobalSemanticTokens
from lang.ts import TypeScriptLang
from lang.yaml import YamlLang
from palette.theme import Theme
from ui.base import BaseSection
from ui.chat import ChatSection
from ui.composer import ColorMapComposition
from ui.debug import DebugSection
from ui.editor import EditorSection
from ui.lists import ListSection
from ui.panels import PanelSection
from ui.symbols import SymbolSection
from ui.tabs import TabSection
from ui.terminal import TerminalSection
from ui.testing import TestingSection
from ui.vcs import VcsSection
from ui.widgets import WidgetSection

_THEMES_DIR = Path(__file__).resolve().parent.parent / "themes"
_STYLES_DIR = Path(__file__).resolve().parent.parent / "styles"
_MARKDOWN_VARS_OUTPUT = _STYLES_DIR / "markdown-variables.css"
_VARIANTS: list[tuple[bool, str, str]] = [
    (False, "Kiro Rider Light", "light"),
    (True, "Kiro Rider Dark", "dark"),
]


_LANG_CLASSES = [
    BaseSyntax,
    JavaLang,
    KotlinLang,
    PythonLang,
    JavaScriptLang,
    TypeScriptLang,
    CssLang,
    HtmlLang,
    MarkdownLang,
    YamlLang,
    JsonLang,
    ScriptLang,
]

_UI_SECTIONS = [
    BaseSection,
    ListSection,
    EditorSection,
    TabSection,
    WidgetSection,
    PanelSection,
    VcsSection,
    ChatSection,
    SymbolSection,
    TerminalSection,
    DebugSection,
    TestingSection,
]


def _generate_variant(*, is_dark: bool, name: str, theme_type: str) -> None:
    theme = Theme.create(is_dark=is_dark)

    composition = ColorMapComposition([cls() for cls in _UI_SECTIONS])
    colors = {k: v.hex for k, v in composition.build(theme).items()}

    registry = LanguageRegistry(GlobalSemanticTokens(theme.syntax))
    for lang_cls in _LANG_CLASSES:
        registry.register(lang_cls())

    token_colors = [rule.to_dict() for rule in registry.build_token_colors(theme)]
    semantic_tokens = registry.build_semantic_tokens(theme)

    output = {
        "$schema": "vscode://schemas/color-theme",
        "name": name,
        "type": theme_type,
        "semanticHighlighting": True,
        "colors": colors,
        "tokenColors": token_colors,
        "semanticTokenColors": semantic_tokens,
    }

    out_path = _THEMES_DIR / f"{name}-color-theme.json"
    _THEMES_DIR.mkdir(parents=True, exist_ok=True)
    _ = out_path.write_text(json.dumps(output, indent=2) + "\n")
    nc, nt, ns = len(colors), len(token_colors), len(semantic_tokens)
    print(f"Wrote {nc} colors, {nt} tokenColors, {ns} semanticTokenColors to {out_path}")


def main() -> None:
    for is_dark, name, theme_type in _VARIANTS:
        _generate_variant(is_dark=is_dark, name=name, theme_type=theme_type)

    _STYLES_DIR.mkdir(parents=True, exist_ok=True)
    _ = _MARKDOWN_VARS_OUTPUT.write_text(build_markdown_css())
    print(f"Wrote markdown variables to {_MARKDOWN_VARS_OUTPUT}")


if __name__ == "__main__":
    main()
