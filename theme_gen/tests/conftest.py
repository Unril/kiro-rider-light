"""Shared test fixtures and helpers."""

import pytest

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


def generate_theme_dict() -> dict[str, object]:
    """Full generation pipeline matching main.py -- single source of truth for tests."""
    theme = Theme.create()

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

    return {
        "$schema": "vscode://schemas/color-theme",
        "name": "Kiro Rider Light",
        "type": "light",
        "semanticHighlighting": True,
        "colors": colors,
        "tokenColors": token_colors,
        "semanticTokenColors": semantic_tokens,
    }


@pytest.fixture(scope="session")
def theme_output() -> dict[str, object]:
    """Session-scoped fixture: full theme dict generated once per test run."""
    return generate_theme_dict()
