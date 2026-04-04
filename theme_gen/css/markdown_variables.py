"""Generate markdown-variables.css with theme colors as CSS custom properties.

The generated file defines --kiro-* CSS variables on body.vscode-light /
body.vscode-dark, consumed by the static markdown-preview.css and
markdown-highlight.css stylesheets.
"""

from palette.theme import Theme

_HEADER = """\
/*
 * Kiro Rider -- Generated CSS custom properties for markdown preview.
 * Do not edit by hand. Regenerate with: cd theme_gen && uv run main.py
 */
"""


def _extract_vars(theme: Theme) -> list[str]:
    """Extract CSS custom properties from a theme."""
    p = theme.palette
    s = theme.syntax
    h = list(enumerate(s.hue_shifted))

    pairs = [
        # Surfaces
        ("bg", p.background),
        ("fg", p.foreground),
        ("accent", p.accent),
        ("border", p.border),
        ("panel", p.panel_bg),
        ("muted", p.fg_muted),
        # Syntax
        ("keyword", s.keyword),
        ("type", s.type),
        ("function", s.function),
        ("string", s.string),
        ("number", s.number),
        ("comment", s.comment),
        ("field", s.field),
        ("metadata", s.metadata),
        ("escape", s.escape),
        # Status
        ("error", p.error),
        ("warning", p.warning),
        ("success", p.success),
        # Headings + quote variants: same hue-shifted series
        *((f"h{i + 1}", c) for i, c in h),
        *((f"h{i + 1}-quote", c.much_darker.muted if theme.is_dark else c.much_lighter.muted) for i, c in h),
        # Blockquote / list chrome
        ("quote-fg", p.fg_muted),
    ]
    return [f"    --kiro-{name}: {col.hex};" for name, col in pairs]


def build_css() -> str:
    """Build the full CSS string with light and dark variables."""
    light = Theme.create(is_dark=False)
    dark = Theme.create(is_dark=True)

    light_vars = "\n".join(_extract_vars(light))
    dark_vars = "\n".join(_extract_vars(dark))

    return (
        f"{_HEADER}\n"
        f"/* Light variant */\n\n"
        f"body.vscode-light {{\n{light_vars}\n}}\n\n"
        f"/* Dark variant */\n\n"
        f"body.vscode-dark {{\n{dark_vars}\n}}\n"
    )
