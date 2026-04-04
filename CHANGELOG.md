# Changelog

All notable changes to the "kiro-rider-light" extension will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/).

## [0.3.0] - 2026-04-03

### Added

- Markdown preview styling with theme-matched colors for both light and dark variants
- Colored heading hierarchy (H1-H6) using the same hue-shifted series as bracket pairs and SCM graph
- Syntax highlighting in preview code blocks via highlight.js scope mapping to theme colors
- Inline code colored with comment-green to match editor styling
- Colored list markers, blockquote accent borders, and nested blockquote distinction
- Table styling: rounded corners, zebra striping, horizontal-only separators
- Task list styling: checked items get line-through and reduced opacity
- Max-width (980px) layout for comfortable reading on wide monitors
- Setting `kiro-rider.markdownPreview.enabled` to toggle preview styling (default: on)
- CSS variables generated on `body.vscode-light` / `body.vscode-dark` for reliable theming
- `SyntaxPalette.hue_shifted` field: single source for bracket, SCM graph, heading, and preview heading colors

## [0.2.0] - 2026-03-26

### Added

- Dark theme variant ("Kiro Rider Dark") with warm-tinted background (OKLCH H=82)
- Same 8 syntax hues as light theme with contrast-matched dark lightness tiers
- Bidirectional `with_min_contrast` -- lightens on dark backgrounds, darkens on light
- `TCol.mix` for blending two colors in sRGB space
- Dark-aware ANSI terminal colors (Lab L*=60 normal, L*=68 bright)
- Dark-aware editor highlights with scaled alpha overlays
- Staged git decoration colors using accent/foreground mix
- Missing UI keys: peek view foregrounds, editor marker navigation, notification borders, markdown alert colors, status bar warning/error states, menu border

### Changed

- Extension renamed to "Kiro Rider" (covers both variants)
- `SyntaxPalette.create` accepts `is_dark` and `foreground` parameters
- `Palette` includes `is_dark` field
- `EditorPalette.create` uses `_tint` and `_overlay` helpers instead of inline conditionals
- `editorInfo.foreground` uses accent blue instead of muted gray
- `descriptionForeground` uses muted foreground instead of full foreground
- `button.hoverBackground` is lighter than button on dark theme
- Warning hue shifted from olive (H=75) to orange-amber (H=55)
- `minimap.background` and `editorOverviewRuler.background` match editor background
- Scrollbar/minimap slider alpha reduced for dark theme
- `panelTitle.activeBackground` matches panel background

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
