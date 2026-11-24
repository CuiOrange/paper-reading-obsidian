# Setup and integration

## Discover before changing anything

1. Find Obsidian's vault registry using the platform's application configuration, then inspect only candidate vaults. With multiple plausible targets, ask which to use once. Read enabled plugins and ZotLit's manifest/configuration; do not dump unrelated plugin settings or secrets.
2. Locate the active note, content and filename templates, or the active profile document. Inspect their actual syntax, frontmatter ownership and output folder. `ZtTemplates` is a conventional folder, not a separate plugin.
3. Identify Zotero's selected user/group library, collection hierarchy and available read/write route. Discover connectors/tools first, then documented APIs/CLI, then UI automation. Use the installed version's official documentation for protocols and template fields. Do not invent HTTP endpoints or command IDs.
4. Determine available PDF extraction tools. Reuse trustworthy full text when available, and inspect PDF pages for equations/tables that extraction damages. MinerU is optional; do not make a machine-specific service or Windows path mandatory.

Record local configuration outside the skill, e.g. `<vault>/.paper-reading/config.json`. Confirm this location during setup; it contains machine paths and is not portable publication data. Keep API credentials in the connector or credential store, not Markdown or this JSON.

Example configuration shape (replace explanatory values with real discovered ones):

```json
{
  "vault_path": "absolute vault path",
  "literature_folder": "Papers",
  "template_folder": "ZtTemplates",
  "library": {"type": "user", "id": "verified library id"},
  "classification": {
    "fallback_collection_key": "verified existing collection key",
    "collection_to_note_folder": {}
  },
  "assets_folder": "Papers/_assets",
  "work_folder": ".paper-reading/work"
}
```

Use actual collection keys plus human-readable paths. An empty folder mapping means one stable literature folder, classification in note properties and indexes. If no fallback collection exists, resolve it once during setup rather than silently creating a new taxonomy. Never infer a remote machine's paths from this machine.

## Initial template setup is separate from paper reading

Installation of this skill does not authorize replacing templates in an existing vault. When setup is requested:

- Inspect and back up only files/settings being changed; show the intended target and changes.
- Preserve custom fields and active user workflows. Prefer a separate selectable template/profile if supported.
- `assets/zotlit/` targets the file-based Liquid templates verified against ZotLit 2.1.4. Other releases may use profile documents or different contracts: adapt using installed defaults and official documentation, not by blindly copying filenames. Do not force a plugin upgrade.
- Preview a real item's template data. The bundled note template renders the named `content` template; in the verified file-based implementation, ZotLit wraps the content render in its managed-region markers. Do not also hardcode those markers in the content asset.
- Native system identity/frontmatter belongs to ZotLit. Configure typed fields through its actual frontmatter system; do not handwrite a guessed item key into template YAML. Retain system keys, including group-library identity.
- Create one sample note in an agreed scratch location. Refresh it through the ordinary update operation and verify that AI and personal sentinel text outside the managed region survives. Inspect formulas, nested code callouts and images in Obsidian. Remove only scratch artifacts created by this check when appropriate.
- Enable optional CSS only if requested; keep the existing theme.

## Integrations and evidence of success

| Operation | Evidence required |
| --- | --- |
| Zotero ingestion | Read back parent item, exact library, collection membership and PDF attachment |
| ZotLit note creation | Operation outcome plus existing file with native `zotero-key` and expected source identity |
| Note update | Diff/readback preserving managed and user-owned regions |
| PDF acquisition | Actual readable file and its source/version |
| Rendering | Observed Obsidian rendering, or explicitly untested |

Do not use direct SQL writes. If only read access is available, record `blocked` at ingestion and continue with provisional reading only if that is useful, keeping it separate from the formal ZotLit note. If ZotLit cannot be invoked, preserve the draft in work state and state that formal note creation remains pending. Repeated retries must not create duplicate records: inspect identifiers after an uncertain result before retrying a mutation.

## Documentation starting points

- https://github.com/aidenlx/zotlit
- https://zotlit.aidenlx.site/docs/reference/templates/syntax
- https://zotlit.aidenlx.site/docs/reference/templates/frontmatter
- https://zotlit.aidenlx.site/blog/v2-release
- https://www.zotero.org/support/dev/web_api/v3/start
- https://help.obsidian.md/callouts

Match documentation to the installed version; live documentation can describe newer releases.
