# theme-gen

VS Code theme generation toolkit. Manages color palettes and token scopes to produce
consistent editor themes.

## Prerequisites

- Python >= 3.13
- [uv] -- fast Python package and project manager

Install uv following the [official instructions](https://docs.astral.sh/uv/getting-started/installation/).

## Quick start

```bash
cd theme_gen

# Sync the virtual environment and install all dependencies (including dev)
uv sync

# Run the generator
uv run main.py

# Run tests
uv run -m pytest
```

`uv sync` reads `pyproject.toml` and `uv.lock`, creates a `.venv`, and installs
pinned dependencies in one step. See the [projects guide] for a full walkthrough.

## `uv run` vs `uvx`

Use `uv run` for commands that belong to the project -- they execute inside the
project's `.venv` with all declared dependencies available:

```bash
uv run main.py
uv run -m pytest
uv run ruff check .
uv run mypy .
```

Use `uvx` (alias for `uv tool run`) for external tools you want to run without
adding them to the project's dependencies:

```bash
uvx cookiecutter gh:user/template
uvx some-cli --version
```

Rule of thumb:

- Part of the repo's contract (CI, teammates need it) -> `uv add` + `uv run`
- One-off or trying a tool -> `uvx`

This project's dev tools (ruff, mypy, black, flake8, pylint, pytest) are all
declared in `[dependency-groups]`, so use `uv run` for them.

See the [tools guide] for details on `uvx` and `uv tool`.

## Managing dependencies

```bash
# Add a runtime dependency
uv add coloraide

# Add a dev-only dependency
uv add --group dev pytest

# Remove a dependency
uv remove coloraide

# Upgrade a single package to its latest compatible version
uv lock --upgrade-package coloraide
```

Dependencies are declared in `pyproject.toml` under `[project].dependencies` and
`[dependency-groups]`. The lockfile `uv.lock` pins exact versions for reproducible
installs and should be committed to version control.

## Configuration

uv reads project-level settings from the `[tool.uv]` table in `pyproject.toml`, or
from a standalone `uv.toml` file in the project root. User-level defaults live in
`~/.config/uv/uv.toml` on macOS/Linux. Project settings take precedence over user
settings, and CLI flags take precedence over both.

See the [configuration files] docs for the full precedence rules and available
settings.

## Project structure

```text
theme_gen/
  pyproject.toml                # Project metadata, dependencies, uv/tool config
  uv.lock                      # Cross-platform lockfile (committed)
  .python-version              # Pinned Python version (3.13)
  .venv/                       # Virtual environment (git-ignored)
  main.py                      # Entry point: Theme.create() -> JSON
  core/                        # TCol (OKLCH color), SemCol, FontStyle
  palette/                     # SyntaxPalette, VariantPreset, UIPalette, EditorPalette
  lang/                        # Language protocol + per-language TextMate rules
  ui/                          # UISection protocol + per-section VS Code color mappings
  tools/                       # Standalone CLIs (color_tool, analysis/extraction)
  tests/
    test_tcol.py
    test_semcol.py
    test_syntax_palette.py
    test_theme_palette.py
    test_generate_theme.py
    fixtures/
      expected_theme.json      # Snapshot for output validation
```

## Further reading

- [Working on projects][projects guide] -- creating, running, and building uv projects
- [Projects concept][projects concept] -- project structure and advanced use cases
- [Configuration files] -- `pyproject.toml` and `uv.toml` settings reference
- [Tools guide] -- `uvx`, `uv tool run`, and `uv tool install`
- [Scripts guide] -- running and creating executable Python scripts

[uv]: https://docs.astral.sh/uv/
[projects guide]: https://docs.astral.sh/uv/guides/projects/
[projects concept]: https://docs.astral.sh/uv/concepts/projects/
[configuration files]: https://docs.astral.sh/uv/concepts/configuration-files/
[tools guide]: https://docs.astral.sh/uv/guides/tools/
[scripts guide]: https://docs.astral.sh/uv/guides/scripts/
