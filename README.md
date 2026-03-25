# Kiro Rider Light

A light color theme for VS Code / Kiro IDE inspired by JetBrains Rider Light. Brings Rider's distinctive syntax palette (green functions, purple types, blue keywords) to VS Code with consistent cross-language highlighting and WCAG AA accessible contrast ratios.

## Features

- 15 perceptually distinct syntax colors, all passing WCAG AA (4.5:1+) on white
- Consistent coloring across Kotlin, Java, TypeScript, Python, Markdown, YAML, JSON, HTML, CSS
- Separate namespace/package color (muted indigo) distinct from types (purple)
- UI colors adapted from JetBrains RiderDay palette
- Generated from Python source for easy customization

## Project structure

```text
scripts/
  generate_theme.py        # Main generator — builds the JSON theme
  extract_ui_colors.py     # Extract UI colors to CSV
  extract_syntax_colors.py # Extract syntax colors to CSV
  color_tool.py            # OKLCH color manipulation utilities
  check_consistency.py     # Cross-language consistency checker
  parse_intellij_scheme.py # Parse IntelliJ editor scheme XML
  parse_intellij_theme.py  # Parse IntelliJ UI theme JSON
  parse_vscode_theme.py    # Parse VS Code theme JSON
  lib/                     # Shared libraries
    palette.py             # All color constants (syntax + UI palette)
    syntax.py              # Token colors and semantic token rules
    ui.py                  # VS Code workbench UI color mappings
    extract_colors.py      # Color extraction library
  tests/                   # Unit tests
themes/                    # Generated output (do not edit directly)
references/                # JetBrains + VS Code reference files
```

## Build

Requires Python 3.10+ and the `coloraide` package (for `color_tool.py` only).

```bash
pip install coloraide
```

Generate the theme JSON from source:

```bash
python3 scripts/generate_theme.py
```

This writes `themes/Kiro Rider Light-color-theme.json`. The generator prints a summary of color/token/semantic counts.

## Test locally

### Option A: F5 (Extension Development Host)

1. Open this folder in VS Code / Kiro
2. Press `F5` to launch the Extension Development Host
3. In the new window: `Ctrl+K Ctrl+T` (or `Cmd+K Cmd+T`) and select "Kiro Rider Light"
4. Open files in Kotlin, Java, TypeScript, Python etc. to preview

Changes to the theme file are applied live in the dev host window.

### Option B: Symlink into extensions

```bash
ln -s "$(pwd)" ~/.vscode/extensions/kiro-rider-light
```

Then restart VS Code and select the theme. For Kiro IDE, use `~/.kiro/extensions/` instead.

## Inspect tokens

Use the scope inspector to verify token coloring:

1. Open a source file
2. `Ctrl+Shift+P` / `Cmd+Shift+P` > "Developer: Inspect Editor Tokens and Scopes"
3. Click on any token to see its TextMate scopes and semantic token type

## Check consistency

Run the cross-language consistency checker:

```bash
python3 scripts/check_consistency.py "themes/Kiro Rider Light-color-theme.json"
```

Use `--check-only` to show only inconsistencies:

```bash
python3 scripts/check_consistency.py "themes/Kiro Rider Light-color-theme.json" --check-only
```

## Color tools

Adjust colors using the OKLCH-based color tool:

```bash
python3 scripts/color_tool.py info "#007D58"
python3 scripts/color_tool.py darken "#007D58" --amount 0.05
python3 scripts/color_tool.py compare "#007D58" "#007494"
python3 scripts/color_tool.py from_oklch 0.52 0.10 225
```

## Publish

### Package as VSIX

```bash
npm install -g @vscode/vsce
vsce package --allow-missing-repository
```

This creates `kiro-rider-light-0.0.1.vsix`.

### Install VSIX locally

```bash
code --install-extension kiro-rider-light-0.0.1.vsix
```

### Publish to marketplace

```bash
vsce login <publisher-name>
vsce publish
```

See [Publishing Extensions](https://code.visualstudio.com/api/working-with-extensions/publishing-extension) for setup details (publisher account, PAT token).

## Customizing

All colors live in `scripts/lib/palette.py`. Edit a constant, run `python3 scripts/generate_theme.py`, and the theme updates. The palette is organized as:

- **UI palette**: RiderDay grays, blues, reds, yellows, greens
- **Semantic UI variables**: mapped roles (PANEL_BG, BORDER, ACCENT, etc.)
- **Syntax palette**: 15 primary colors for code highlighting
- **Editor decoration colors**: caret, gutter, diff, find, etc.
- **Terminal ANSI colors**: from RiderLight.xml console output colors

## License

MIT
