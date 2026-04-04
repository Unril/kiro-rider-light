# Kiro Rider

Light and dark color themes for VS Code and Kiro IDE, inspired by JetBrains Rider.

A class is always purple, a function is always green, a keyword is always blue -- regardless of whether you're in Kotlin, Java, TypeScript, or Python. Includes a themed markdown preview with colored headings, syntax-highlighted code blocks, and styled tables.

Dedicated highlighting scopes for [Kotlin LSP][kotlin-lsp], [basedpyright][basedpyright], and [highlight.js](https://highlightjs.org) in the markdown preview.

<a href="https://raw.githubusercontent.com/Unril/kiro-rider-light/master/img/ui.png"><img src="https://raw.githubusercontent.com/Unril/kiro-rider-light/master/img/ui.png" alt="Light theme UI" width="960"></a>

<a href="https://raw.githubusercontent.com/Unril/kiro-rider-light/master/img/ui_dark.png"><img src="https://raw.githubusercontent.com/Unril/kiro-rider-light/master/img/ui_dark.png" alt="Dark theme UI" width="960"></a>

Kotlin with semantic highlighting from [Kotlin LSP][kotlin-lsp]:

<a href="https://raw.githubusercontent.com/Unril/kiro-rider-light/master/img/large_kt.png"><img src="https://raw.githubusercontent.com/Unril/kiro-rider-light/master/img/large_kt.png" alt="Kotlin highlighting (light)" width="960"></a>

<a href="https://raw.githubusercontent.com/Unril/kiro-rider-light/master/img/large_kt_dark.png"><img src="https://raw.githubusercontent.com/Unril/kiro-rider-light/master/img/large_kt_dark.png" alt="Kotlin highlighting (dark)" width="960"></a>

Python with semantic highlighting from [basedpyright][basedpyright]:

<a href="https://raw.githubusercontent.com/Unril/kiro-rider-light/master/img/large_py.png"><img src="https://raw.githubusercontent.com/Unril/kiro-rider-light/master/img/large_py.png" alt="Python highlighting (light)" width="960"></a>

<a href="https://raw.githubusercontent.com/Unril/kiro-rider-light/master/img/large_py_dark.png"><img src="https://raw.githubusercontent.com/Unril/kiro-rider-light/master/img/large_py_dark.png" alt="Python highlighting (dark)" width="960"></a>

## Markdown Preview

The markdown preview uses the same syntax palette for code blocks, colored headings that follow the hue-shifted series, and styled tables, blockquotes, and lists. Toggle with `kiro-rider.markdownPreview.enabled`.

Colored headings, syntax-highlighted code blocks, and endpoint table:

<a href="https://raw.githubusercontent.com/Unril/kiro-rider-light/master/img/preview/light-top.png"><img src="https://raw.githubusercontent.com/Unril/kiro-rider-light/master/img/preview/light-top.png" alt="Markdown preview (light, top)" width="960"></a>

<a href="https://raw.githubusercontent.com/Unril/kiro-rider-light/master/img/preview/dark-top.png"><img src="https://raw.githubusercontent.com/Unril/kiro-rider-light/master/img/preview/dark-top.png" alt="Markdown preview (dark, top)" width="960"></a>

Nested lists with colored markers, styled blockquotes, and depth-adapted coloring:

<a href="https://raw.githubusercontent.com/Unril/kiro-rider-light/master/img/preview/light-bottom.png"><img src="https://raw.githubusercontent.com/Unril/kiro-rider-light/master/img/preview/light-bottom.png" alt="Markdown preview (light, bottom)" width="960"></a>

<a href="https://raw.githubusercontent.com/Unril/kiro-rider-light/master/img/preview/dark-bottom.png"><img src="https://raw.githubusercontent.com/Unril/kiro-rider-light/master/img/preview/dark-bottom.png" alt="Markdown preview (dark, bottom)" width="960"></a>

## Features

- Light and dark variants with the same syntax hues
- Consistent colors across Kotlin, Java, TypeScript, JavaScript, Python, Markdown, YAML, JSON, HTML, and CSS
- Dedicated scopes for [Kotlin LSP][kotlin-lsp] and [basedpyright][basedpyright]
- 17 syntax roles from an OKLCH harmony wheel, all passing WCAG AA (4.5:1)
- 487 UI colors covering editor, terminal, debug, testing, VCS, and more
- Themed markdown preview with colored headings, code blocks, tables, blockquotes, and lists
- Python-based generator for easy customization

## Syntax Palette

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

## Installation

Install from the [VS Code Marketplace][marketplace] or [Open VSX][open-vsx], or search for "Kiro Rider" in the Extensions view.

See [CONTRIBUTING.md][contributing] for generator usage, local testing, and development setup.

## License

MIT

[marketplace]: https://marketplace.visualstudio.com/items?itemName=NikolaiFedorov.kiro-rider-light
[open-vsx]: https://open-vsx.org/extension/NikolaiFedorov/kiro-rider-light
[contributing]: https://github.com/Unril/kiro-rider-light/blob/master/CONTRIBUTING.md
[kotlin-lsp]: https://github.com/Kotlin/kotlin-lsp
[basedpyright]: https://github.com/detachhead/basedpyright
