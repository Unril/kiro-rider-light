# Contributing

Pull requests are welcome. Repository: [github.com/Unril/kiro-rider-light](https://github.com/Unril/kiro-rider-light)

## Installation

Install from the [VS Code Marketplace](https://marketplace.visualstudio.com/items?itemName=NikolaiFedorov.kiro-rider-light) or [Open VSX](https://open-vsx.org/extension/NikolaiFedorov/kiro-rider-light), or search for "Kiro Rider" in the Extensions view.

Or install a `.vsix` directly:

```bash
code --install-extension kiro-rider-light-*.vsix
```

## Generator

Both theme JSON files are generated from Python source in `theme_gen/`:

```bash
cd theme_gen
uv run main.py
```

This writes `themes/Kiro Rider Light-color-theme.json` and `themes/Kiro Rider Dark-color-theme.json`.

## Test Locally

1. Open this folder in VS Code or Kiro
2. Press `F5` to launch the Extension Development Host
3. `Cmd+K Cmd+T` and select "Kiro Rider Light" or "Kiro Rider Dark"
