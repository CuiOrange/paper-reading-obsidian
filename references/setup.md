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
    "fallback_collection_key": "verified existing collection key"
  },
  "paper_layout": "method-folder",
  "paper_assets_subfolder": "images",
  "work_folder": ".paper-reading/work"
}
```

Use actual collection keys plus human-readable paths. Every paper folder lives directly under `literature_folder`; Zotero classification stays in Zotero collections; keep any workflow classification outside note properties. Ignore an old collection-to-note-folder mapping for new notes under this layout; do not migrate existing notes without checking their identity and links. If no fallback collection exists, resolve it once during setup. Never infer a remote machine's paths from this machine. Generated checks use a task-owned system temporary directory with cleanup after execution; ignore a legacy `paper_checks_subfolder` setting rather than creating that folder in a paper directory. Do not rewrite user configuration merely to apply this rule.

## Initial template setup is separate from paper reading

Installation of this skill does not authorize replacing templates in an existing vault. When setup is requested:

- Inspect and back up only files/settings being changed; show the intended target and changes.
- Preserve custom fields and active user workflows. Prefer a separate selectable template/profile if supported.
- `assets/zotlit/` targets the file-based Liquid templates verified against ZotLit 2.1.4. Other releases may use profile documents or different contracts: adapt using installed defaults and official documentation, not by blindly copying filenames. Do not force a plugin upgrade.
- Preview a real item with the template for the selected output language. The bundled note templates do not render the named `content` template, because that operation may inject ZotLit managed delimiters. After verifying native creation, remove any generated HTML ownership comments or managed-marker lines while keeping imported text visible. Do not globally replace active templates or settings during a reading request.
- Resolve the verified method name from the paper. Place the plugin-created shell at `<literature-root>/<paper-name>/<paper-name>.md` through supported Obsidian operations. Verify and save the real item identity externally before trimming properties. After native keys are removed, locate updates through the saved mapping and body link; do not assume plugin lookup still works.
- Final note properties follow the five-field schema in `note-contract.md`. Remove Zotero and workflow keys after verifying the initial shell; keep only one Zotero jump link and one article link in the main body. Retain the real identity in the compact external checkpoint and do not restore native keys during updates.
- Preview the minimal properties and body source line with a real item. Keep essential bibliographic facts only, omit unknowns, and do not replace global template/frontmatter settings without a setup request.
- When setup is requested, create one scratch note, verify source links, property cleanup and preservation of generated/user text without hidden markers, and inspect formulas, callouts and images. Do not run plugin refresh after final property/marker cleanup unless the installed integration demonstrably preserves that format. Remove only scratch artifacts created by this check.
- Enable optional CSS only if requested; keep the existing theme.

Do not enable automatic Zotero child-note export or invoke bulk/child-note import commands that generate `zotero_notes/`. Inspect the current export behavior before importing notes. Use read-only note/annotation retrieval and write relevant content into the selected paper notes; do not alter global plugin settings during ordinary reading.

## Integrations and evidence of success

| Operation | Evidence required |
| --- | --- |
| Zotero ingestion | Read back parent item, exact library, collection membership and PDF attachment |
| ZotLit note creation | Observed creation outcome and source identity before cleanup; afterward verify the external mapping, minimal properties, marker-free content and body jump link |
| Note update | Diff/readback preserving user edits and imported visible content, without adding hidden delimiters |
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
