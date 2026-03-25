"""VcsSection -- diff editor, git decorations, minimap VCS markers."""

from typing import override

from core.hue_series import hue_series
from core.tcol import TCol
from palette.theme import Theme
from ui.protocol import UISection


class VcsSection(UISection):
    @override
    def build(self, theme: Theme) -> dict[str, TCol]:
        p = theme.palette
        e = theme.editor

        return {
            # Diff editor
            "diffEditor.insertedTextBackground": p.diff_insert,
            "diffEditor.removedTextBackground": p.diff_remove,
            "diffEditor.insertedLineBackground": p.diff_insert,
            "diffEditor.removedLineBackground": p.diff_remove,
            "diffEditorOverview.insertedForeground": p.gutter_add,
            "diffEditorOverview.removedForeground": p.gutter_del,
            "diffEditor.unchangedRegionBackground": p.panel_bg,
            # Minimap
            "minimap.background": p.panel_bg,
            "minimap.findMatchHighlight": e.selection.find_hl,
            "minimap.selectionHighlight": e.selection.primary,
            "minimap.errorHighlight": p.minimap_error,
            "minimap.warningHighlight": p.minimap_warning,
            "minimap.infoHighlight": e.chrome.info_fg,
            "minimapSlider.background": p.minimap_slider,
            "minimapSlider.hoverBackground": p.scrollbar_thumb,
            "minimapSlider.activeBackground": p.scrollbar_hover,
            "minimapGutter.addedBackground": p.gutter_add,
            "minimapGutter.modifiedBackground": p.gutter_mod,
            "minimapGutter.deletedBackground": p.gutter_del,
            # Git decorations
            "gitDecoration.addedResourceForeground": p.success,
            "gitDecoration.modifiedResourceForeground": p.accent,
            "gitDecoration.deletedResourceForeground": p.error,
            "gitDecoration.untrackedResourceForeground": p.success,
            "gitDecoration.ignoredResourceForeground": p.fg_disabled,
            "gitDecoration.conflictingResourceForeground": p.error,
            "gitDecoration.renamedResourceForeground": p.success,
            # Git blame -- warm muted for historical annotations
            "git.blame.editorDecorationForeground": p.secondary.a50,
            # Merge conflicts
            "merge.currentHeaderBackground": p.success.a25,
            "merge.currentContentBackground": p.success.a15,
            "merge.incomingHeaderBackground": p.accent.a25,
            "merge.incomingContentBackground": p.accent.a15,
            "merge.commonHeaderBackground": p.fg_muted.a25,
            "merge.commonContentBackground": p.fg_muted.a15,
            # SCM graph -- same hue-shifted series as bracket pair colorization
            **{f"scmGraph.foreground{i + 1}": color for i, color in enumerate(hue_series(theme.syntax.enum_member, 5))},
        }
