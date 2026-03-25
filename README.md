# Kiro Rider Light

A light color theme for VS Code and Kiro IDE inspired by JetBrains Rider Light.

Designed to feel light and clean while keeping syntax readable. Classes, functions, and keywords look the same whether you're in Kotlin, Java, TypeScript, or Python -- so switching between languages doesn't mean re-learning the color map.

Includes dedicated highlighting scopes for [Kotlin LSP][kotlin-lsp] and [basedpyright][basedpyright], with WCAG AA contrast ratios throughout.

## Screenshots

<img src="https://raw.githubusercontent.com/Unril/kiro-rider-light/main/img/ui.png" alt="Overall UI" width="960">

| | |
| --- | --- |
| <img src="https://raw.githubusercontent.com/Unril/kiro-rider-light/main/img/large_kt.png" alt="Kotlin highlighting" width="480"> | <img src="https://raw.githubusercontent.com/Unril/kiro-rider-light/main/img/large_py.png" alt="Python highlighting" width="480"> |

Click any thumbnail below to view the full-size image.

| | |
| --- | --- |
| <a href="https://raw.githubusercontent.com/Unril/kiro-rider-light/main/img/kt.png"><img src="https://raw.githubusercontent.com/Unril/kiro-rider-light/main/img/kt.png" alt="Kotlin" width="400"></a> | <a href="https://raw.githubusercontent.com/Unril/kiro-rider-light/main/img/java.png"><img src="https://raw.githubusercontent.com/Unril/kiro-rider-light/main/img/java.png" alt="Java" width="400"></a> |
| Kotlin | Java |
| <a href="https://raw.githubusercontent.com/Unril/kiro-rider-light/main/img/ts.png"><img src="https://raw.githubusercontent.com/Unril/kiro-rider-light/main/img/ts.png" alt="TypeScript" width="400"></a> | <a href="https://raw.githubusercontent.com/Unril/kiro-rider-light/main/img/js.png"><img src="https://raw.githubusercontent.com/Unril/kiro-rider-light/main/img/js.png" alt="JavaScript" width="400"></a> |
| TypeScript | JavaScript |
| <a href="https://raw.githubusercontent.com/Unril/kiro-rider-light/main/img/py.png"><img src="https://raw.githubusercontent.com/Unril/kiro-rider-light/main/img/py.png" alt="Python" width="400"></a> | <a href="https://raw.githubusercontent.com/Unril/kiro-rider-light/main/img/md.png"><img src="https://raw.githubusercontent.com/Unril/kiro-rider-light/main/img/md.png" alt="Markdown" width="400"></a> |
| Python | Markdown |
| <a href="https://raw.githubusercontent.com/Unril/kiro-rider-light/main/img/yaml.png"><img src="https://raw.githubusercontent.com/Unril/kiro-rider-light/main/img/yaml.png" alt="YAML" width="400"></a> | <a href="https://raw.githubusercontent.com/Unril/kiro-rider-light/main/img/json.png"><img src="https://raw.githubusercontent.com/Unril/kiro-rider-light/main/img/json.png" alt="JSON" width="400"></a> |
| YAML | JSON |
| <a href="https://raw.githubusercontent.com/Unril/kiro-rider-light/main/img/html.png"><img src="https://raw.githubusercontent.com/Unril/kiro-rider-light/main/img/html.png" alt="HTML" width="400"></a> | <a href="https://raw.githubusercontent.com/Unril/kiro-rider-light/main/img/css.png"><img src="https://raw.githubusercontent.com/Unril/kiro-rider-light/main/img/css.png" alt="CSS" width="400"></a> |
| HTML | CSS |

## Features

- Works in VS Code and Kiro IDE
- Consistent syntax colors across Kotlin, Java, TypeScript, JavaScript, Python, Markdown, YAML, JSON, HTML, and CSS -- a class is always purple, a function is always green, regardless of language
- Dedicated scopes for [Kotlin LSP][kotlin-lsp] and [basedpyright][basedpyright] so Kotlin and Python get proper semantic highlighting
- 17 syntax roles generated from an OKLCH harmony wheel, all passing WCAG AA (4.5:1) on white
- 465 UI colors covering editor, terminal, debug, testing, VCS, and more
- Full 16-color ANSI terminal palette at perceptually uniform lightness
- Python-based generator for easy customization

## Syntax palette

| Role | Color |
| --- | --- |
| Functions | <span style="color:#007561">Green</span> |
| Types / Classes | <span style="color:#7922A7">Purple</span> |
| Keywords | <span style="color:#305EDD">Blue</span> |
| Fields / Properties | <span style="color:#00819D">Teal</span> |
| Strings | <span style="color:#A26955">Brown</span> |
| Numbers | <span style="color:#C24C82">Magenta</span> |
| Comments | <span style="color:#5C822E">Muted green</span> |
| Metadata / Annotations | <span style="color:#977100">Olive</span> |

## Installation

Install from the [VS Code Marketplace][marketplace] or search for "Kiro Rider Light" in the Extensions view.

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
[repo]: https://github.com/Unril/kiro-rider-light
[kotlin-lsp]: https://github.com/Kotlin/kotlin-lsp
[basedpyright]: https://github.com/detachhead/basedpyright
