#!/usr/bin/env -S uv run --script

"""Generate the Kiro Rider Light VS Code color theme JSON."""

import json
from pathlib import Path

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

_OUTPUT = Path(__file__).resolve().parent.parent / "themes" / "Kiro Rider Light-color-theme.json"


def main() -> None:
    theme = Theme.create()

    # UI colors
    composition = ColorMapComposition(
        [
            BaseSection(),
            ListSection(),
            EditorSection(),
            TabSection(),
            WidgetSection(),
            PanelSection(),
            VcsSection(),
            ChatSection(),
            SymbolSection(),
            TerminalSection(),
            DebugSection(),
            TestingSection(),
        ],
    )
    colors = {k: v.hex for k, v in composition.build(theme).items()}

    # Language tokens
    registry = LanguageRegistry(GlobalSemanticTokens(theme.syntax))
    for lang_cls in [
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
    ]:
        registry.register(lang_cls())

    token_colors = [rule.to_dict() for rule in registry.build_token_colors(theme)]
    semantic_tokens = registry.build_semantic_tokens(theme)

    output = {
        "$schema": "vscode://schemas/color-theme",
        "name": "Kiro Rider Light",
        "type": "light",
        "semanticHighlighting": True,
        "colors": colors,
        "tokenColors": token_colors,
        "semanticTokenColors": semantic_tokens,
    }

    _OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    _ = _OUTPUT.write_text(json.dumps(output, indent=2) + "\n")
    nc, nt, ns = len(colors), len(token_colors), len(semantic_tokens)
    print(f"Wrote {nc} colors, {nt} tokenColors, {ns} semanticTokenColors to {_OUTPUT}")


if __name__ == "__main__":
    main()
