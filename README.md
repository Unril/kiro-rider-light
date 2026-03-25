# Kiro Rider Light

A light color theme for VS Code and Kiro IDE inspired by JetBrains Rider Light.

Designed to feel light and clean while keeping syntax readable. Classes, functions, and keywords look the same whether you're in Kotlin, Java, TypeScript, or Python -- so switching between languages doesn't mean re-learning the color map.

Includes dedicated highlighting scopes for [Kotlin LSP][kotlin-lsp] and [basedpyright][basedpyright], with WCAG AA contrast ratios throughout.

<a href="https://raw.githubusercontent.com/Unril/kiro-rider-light/master/img/ui.png"><img src="https://raw.githubusercontent.com/Unril/kiro-rider-light/master/img/ui.png" alt="Overall UI" width="960"></a>

<img src="https://raw.githubusercontent.com/Unril/kiro-rider-light/master/img/large_kt.png" alt="Kotlin highlighting">

<img src="https://raw.githubusercontent.com/Unril/kiro-rider-light/master/img/large_py.png" alt="Python highlighting">

## Screenshots

- [Kotlin](https://raw.githubusercontent.com/Unril/kiro-rider-light/master/img/code/kt.png)
- [Java](https://raw.githubusercontent.com/Unril/kiro-rider-light/master/img/code/java.png)
- [TypeScript](https://raw.githubusercontent.com/Unril/kiro-rider-light/master/img/code/ts.png)
- [JavaScript](https://raw.githubusercontent.com/Unril/kiro-rider-light/master/img/code/js.png)
- [Python](https://raw.githubusercontent.com/Unril/kiro-rider-light/master/img/code/py.png)
- [Markdown](https://raw.githubusercontent.com/Unril/kiro-rider-light/master/img/code/md.png)
- [YAML](https://raw.githubusercontent.com/Unril/kiro-rider-light/master/img/code/yaml.png)
- [JSON](https://raw.githubusercontent.com/Unril/kiro-rider-light/master/img/code/json.png)
- [HTML](https://raw.githubusercontent.com/Unril/kiro-rider-light/master/img/code/html.png)
- [CSS](https://raw.githubusercontent.com/Unril/kiro-rider-light/master/img/code/css.png)

## Features

- Works in VS Code and Kiro IDE
- Consistent syntax colors across Kotlin, Java, TypeScript, JavaScript, Python, Markdown, YAML, JSON, HTML, and CSS -- a class is always purple, a function is always green, regardless of language
- Dedicated scopes for [Kotlin LSP][kotlin-lsp] and [basedpyright][basedpyright] so Kotlin and Python get proper semantic highlighting
- 17 syntax roles generated from an OKLCH harmony wheel, all passing WCAG AA (4.5:1) on white
- 465 UI colors covering editor, terminal, debug, testing, VCS, and more
- Full 16-color ANSI terminal palette at perceptually uniform lightness
- Python-based generator for easy customization

## Syntax palette

| Role                   | Color                                                                |
| ---------------------- | -------------------------------------------------------------------- |
| Functions              | ![#007561](https://placehold.co/15x15/007561/007561.png) Green       |
| Types / Classes        | ![#7922A7](https://placehold.co/15x15/7922A7/7922A7.png) Purple      |
| Keywords               | ![#305EDD](https://placehold.co/15x15/305EDD/305EDD.png) Blue        |
| Fields / Properties    | ![#00819D](https://placehold.co/15x15/00819D/00819D.png) Teal        |
| Strings                | ![#A26955](https://placehold.co/15x15/A26955/A26955.png) Brown       |
| Numbers                | ![#C24C82](https://placehold.co/15x15/C24C82/C24C82.png) Magenta     |
| Comments               | ![#5C822E](https://placehold.co/15x15/5C822E/5C822E.png) Muted green |
| Metadata / Annotations | ![#977100](https://placehold.co/15x15/977100/977100.png) Olive       |

## Installation

Install from the [VS Code Marketplace][marketplace] or [Open VSX][open-vsx], or search for "Kiro Rider Light" in the Extensions view.

Or install a `.vsix` directly:

```bash
code --install-extension kiro-rider-light-0.1.0.vsix
```

## Generator

The theme JSON is generated from Python source in `theme_gen/`. To regenerate after changes:

```bash
cd theme_gen
uv run main.py
```

This writes `themes/Kiro Rider Light-color-theme.json` and prints a summary of color/token/semantic counts.

## Test locally

1. Open this folder in VS Code or Kiro
2. Press `F5` to launch the Extension Development Host
3. In the new window: `Cmd+K Cmd+T` and select "Kiro Rider Light"

## Contributing

Pull requests are welcome. Repository: [github.com/Unril/kiro-rider-light][repo]

## License

MIT

[marketplace]: https://marketplace.visualstudio.com/items?itemName=NikolaiFedorov.kiro-rider-light
[open-vsx]: https://open-vsx.org/extension/NikolaiFedorov/kiro-rider-light
[repo]: https://github.com/Unril/kiro-rider-light
[kotlin-lsp]: https://github.com/Kotlin/kotlin-lsp
[basedpyright]: https://github.com/detachhead/basedpyright
