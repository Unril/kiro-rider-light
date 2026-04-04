// @ts-check
const vscode = require('vscode');

const configSection = 'kiro-rider';
const enabledKey = 'markdownPreview.enabled';

function isEnabled() {
    const settings = vscode.workspace.getConfiguration(configSection, null);
    return settings.get(enabledKey, true);
}

exports.activate = function (/** @type {vscode.ExtensionContext} */ ctx) {
    ctx.subscriptions.push(
        vscode.workspace.onDidChangeConfiguration(e => {
            if (e.affectsConfiguration(configSection)) {
                vscode.commands.executeCommand('markdown.preview.refresh');
            }
        })
    );

    return {
        extendMarkdownIt(/** @type {import('markdown-it')} */ md) {
            return md.use(plugin);
        },
    };
};

function plugin(/** @type {import('markdown-it')} */ md) {
    const render = md.renderer.render;
    md.renderer.render = (...args) => {
        if (!isEnabled()) {
            return render.apply(md.renderer, args);
        }
        return `<div class="kiro-rider-preview">${render.apply(md.renderer, args)}</div>`;
    };
    return md;
}
