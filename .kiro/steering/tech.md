# Tech Stack

## Theme Package (VS Code Extension)

- Format: VS Code color theme extension (`package.json` with `contributes.themes`)
- Output: `themes/Kiro Rider Light-color-theme.json` (generated, not hand-edited)
- Engine: VS Code `^1.90.0`

## Theme Generator (`theme_gen/`)

- Language: Python 3.13 (pinned in `.python-version`)
- Package manager: `uv` (lockfile: `uv.lock`, venv: `.venv/`)
- Key dependencies:
  - `coloraide` -- OKLCH color math and gamut mapping
  - `scipy` -- contrast optimization (`with_min_contrast`)
  - `pyjson5` -- JSON5 parsing for reference files
  - `structlog` -- structured logging
- Linter/formatter: `ruff` (line length 120, target py313, `ALL` rules minus `D EM T20 S TRY003 COM812 ERA001`)
- Type checker: `mypy` (strict mode) + `basedpyright`
- Test runner: `pytest`

## Common Commands

All commands run from `theme_gen/`:

```bash
# Regenerate the theme JSON
uv run main.py

# Run tests
uv run -m pytest

# Lint
uv run ruff check .

# Type check
uv run mypy .

# Sync dependencies (after pyproject.toml changes)
uv sync
```

## VS Code Extension Testing

From the workspace root, press `F5` to launch the Extension Development Host, then `Cmd+K Cmd+T` to select the theme.

## Packaging

```bash
# Install vsce if needed
npm install -g @vscode/vsce

# Package
vsce package
```
