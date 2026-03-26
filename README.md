# Kiro Rider

Light and dark color themes for VS Code and Kiro IDE, inspired by JetBrains Rider.

A class is always purple, a function is always green, a keyword is always blue -- regardless of whether you're in Kotlin, Java, TypeScript, or Python. The palette is generated from an OKLCH harmony wheel so every syntax color passes WCAG AA contrast in both variants.

Includes dedicated highlighting scopes for [Kotlin LSP][kotlin-lsp] and [basedpyright][basedpyright].

<a href="https://raw.githubusercontent.com/Unril/kiro-rider-light/master/img/ui.png"><img src="https://raw.githubusercontent.com/Unril/kiro-rider-light/master/img/ui.png" alt="Light theme UI" width="960"></a>

<a href="https://raw.githubusercontent.com/Unril/kiro-rider-light/master/img/ui_dark.png"><img src="https://raw.githubusercontent.com/Unril/kiro-rider-light/master/img/ui_dark.png" alt="Dark theme UI" width="960"></a>

<img src="https://raw.githubusercontent.com/Unril/kiro-rider-light/master/img/large_kt.png" alt="Kotlin highlighting (light)">

<img src="https://raw.githubusercontent.com/Unril/kiro-rider-light/master/img/large_kt_dark.png" alt="Kotlin highlighting (dark)">

<img src="https://raw.githubusercontent.com/Unril/kiro-rider-light/master/img/large_py.png" alt="Python highlighting (light)">

<img src="https://raw.githubusercontent.com/Unril/kiro-rider-light/master/img/large_py_dark.png" alt="Python highlighting (dark)">

## Screenshots

### Light

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

### Dark

- [Kotlin](https://raw.githubusercontent.com/Unril/kiro-rider-light/master/img/code_dark/kt.png)
- [Java](https://raw.githubusercontent.com/Unril/kiro-rider-light/master/img/code_dark/java.png)
- [TypeScript](https://raw.githubusercontent.com/Unril/kiro-rider-light/master/img/code_dark/ts.png)
- [JavaScript](https://raw.githubusercontent.com/Unril/kiro-rider-light/master/img/code_dark/js.png)
- [Python](https://raw.githubusercontent.com/Unril/kiro-rider-light/master/img/code_dark/py.png)
- [Markdown](https://raw.githubusercontent.com/Unril/kiro-rider-light/master/img/code_dark/md.png)
- [YAML](https://raw.githubusercontent.com/Unril/kiro-rider-light/master/img/code_dark/yaml.png)
- [JSON](https://raw.githubusercontent.com/Unril/kiro-rider-light/master/img/code_dark/json.png)
- [HTML](https://raw.githubusercontent.com/Unril/kiro-rider-light/master/img/code_dark/html.png)
- [CSS](https://raw.githubusercontent.com/Unril/kiro-rider-light/master/img/code_dark/css.png)

## Features

- Works in VS Code and Kiro IDE
- Light and dark variants with the same syntax hues
- Consistent colors across Kotlin, Java, TypeScript, JavaScript, Python, Markdown, YAML, JSON, HTML, and CSS
- Dedicated scopes for [Kotlin LSP][kotlin-lsp] and [basedpyright][basedpyright]
- 17 syntax roles from an OKLCH harmony wheel, all passing WCAG AA (4.5:1)
- 487 UI colors covering editor, terminal, debug, testing, VCS, and more
- Python-based generator for easy customization

## Syntax palette

| Role                   | Light                                                              | Dark                                                               |
| ---------------------- | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| Functions              | ![#007561](https://placehold.co/15x15/007561/007561.png) `#007561` | ![#3FA68E](https://placehold.co/15x15/3FA68E/3FA68E.png) `#3FA68E` |
| Types / Classes        | ![#7922A7](https://placehold.co/15x15/7922A7/7922A7.png) `#7922A7` | ![#D190FF](https://placehold.co/15x15/D190FF/D190FF.png) `#D190FF` |
| Keywords               | ![#305EDD](https://placehold.co/15x15/305EDD/305EDD.png) `#305EDD` | ![#6492FF](https://placehold.co/15x15/6492FF/6492FF.png) `#6492FF` |
| Fields / Properties    | ![#00819D](https://placehold.co/15x15/00819D/00819D.png) `#00819D` | ![#339CB9](https://placehold.co/15x15/339CB9/339CB9.png) `#339CB9` |
| Strings                | ![#A26955](https://placehold.co/15x15/A26955/A26955.png) `#A26955` | ![#B88573](https://placehold.co/15x15/B88573/B88573.png) `#B88573` |
| Numbers                | ![#C24C82](https://placehold.co/15x15/C24C82/C24C82.png) `#C24C82` | ![#D6709A](https://placehold.co/15x15/D6709A/D6709A.png) `#D6709A` |
| Comments               | ![#5C822E](https://placehold.co/15x15/5C822E/5C822E.png) `#5C822E` | ![#7A9B56](https://placehold.co/15x15/7A9B56/7A9B56.png) `#7A9B56` |
| Metadata / Annotations | ![#977100](https://placehold.co/15x15/977100/977100.png) `#977100` | ![#AE8C41](https://placehold.co/15x15/AE8C41/AE8C41.png) `#AE8C41` |

## Installation

Install from the [VS Code Marketplace][marketplace] or [Open VSX][open-vsx], or search for "Kiro Rider" in the Extensions view.

Or install a `.vsix` directly:

```bash
code --install-extension kiro-rider-light-0.2.0.vsix
```

## Generator

Both theme JSON files are generated from Python source in `theme_gen/`:

```bash
cd theme_gen
uv run main.py
```

This writes `themes/Kiro Rider Light-color-theme.json` and `themes/Kiro Rider Dark-color-theme.json`.

## Test locally

1. Open this folder in VS Code or Kiro
2. Press `F5` to launch the Extension Development Host
3. `Cmd+K Cmd+T` and select "Kiro Rider Light" or "Kiro Rider Dark"

## Contributing

Pull requests are welcome. Repository: [github.com/Unril/kiro-rider-light][repo]

## License

MIT

[marketplace]: https://marketplace.visualstudio.com/items?itemName=NikolaiFedorov.kiro-rider-light
[open-vsx]: https://open-vsx.org/extension/NikolaiFedorov/kiro-rider-light
[repo]: https://github.com/Unril/kiro-rider-light
[kotlin-lsp]: https://github.com/Kotlin/kotlin-lsp
[basedpyright]: https://github.com/detachhead/basedpyright
