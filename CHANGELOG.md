# Changelog

All notable changes to the "kiro-rider-light" extension will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/).

## [0.1.0] - 2026-03-25

### Added

- 17 syntax roles generated from an OKLCH harmony wheel with 45° hue spacing
- All syntax roles pass WCAG AA (4.5:1) contrast on white
- Full cross-language support: Kotlin, Java, TypeScript, JavaScript, Python, Markdown, YAML, JSON, HTML, CSS
- 465 UI colors covering editor, terminal, debug, testing, VCS, panels, and more
- 16-color ANSI terminal palette generated from standard hues at perceptually uniform CIELab lightness
- Debug token expressions and debug icons (Variables/Watch view, breakpoints, toolbar)
- Testing icons with pass/fail/skip states and coverage indicators
- SCM graph colors using the same hue-shifted series as bracket pair colorization
- Merge conflict colors (current/incoming/common)
- Additional symbol icons (array, boolean, constructor, event, field, module, struct, etc.)
- Secondary (complementary gold) color applied to lightbulb, gutter comment markers, list filter matches, and git blame
- Python-based generator (`theme_gen/`) with snapshot integration tests
- Extension icon
