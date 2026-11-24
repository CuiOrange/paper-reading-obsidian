# Note identity, ownership and recovery

## Identity and properties

Keep ZotLit's system-managed frontmatter exactly as produced by the installed release. In particular, retain `zotero-key`; group-library values may encode library identity. Do not replace it with a homemade `zotero_key`. Store explicit library identity and attachment key separately when needed for external tooling.

Reuse template properties. Useful additional unmanaged properties, configured to avoid plugin overwrite, include:

```yaml
type: literature-note
cssclasses:
  - paper-reading
reading_status: queued
verification_status: pending
```

Use actual values for `paper_version`, DOI/arXiv ID, categories/tags, dates, repository/commit and attachment identity when known; omit unknown facts. Keep native bibliography fields typed through the plugin where possible. Do not construct YAML by injecting unescaped paper titles or author names into quoted strings.

`reading_status`: `queued`, `reading`, `partial`, `complete`.
`verification_status`: `pending`, `partial`, `checked`, `blocked`.
`checked` means the documented planned checks completed, not that every scientific claim is proven. Never set completion from file existence alone.

For detail notes use `type: paper-detail` and a real `parent-note` wikilink. The parent literature note is the single canonical ZotLit literature note; do not duplicate its native `zotero-key` into detail-note metadata unless the installed plugin explicitly supports that use without indexing duplicates.

## Region ownership

The bundled note asset places three regions in one file:

1. ZotLit's content render: the plugin owns the native managed region (`%%zt-managed%%` … `%%/zt-managed%%` in the verified 2.x release). It may regenerate imported notes/annotations.
2. `<!-- paper-reading:ai:start -->` … `<!-- paper-reading:ai:end -->`: AI explanations, outside the native managed region.
3. `<!-- paper-reading:user:start -->` … `<!-- paper-reading:user:end -->`: user-owned thinking, never filled with invented first-person judgments.

Use HTML comments for skill ownership and the plugin's own Obsidian comments for its managed region; these are distinct contracts. Do not nest them. Verify actual generated output before depending on it. Do not insert native managed markers manually into a content template already wrapped by ZotLit.

Before editing, read the whole note and save the previous AI-region snapshot/hash in work state. Compare against the last generated snapshot when available. If the current region differs, preserve manual changes with a targeted merge; absent a baseline, avoid whole-region replacement. Region markers do not imply ownership of every future user edit.

An ordinary ZotLit update preserves outside text in the verified version. Its overwrite operation can replace the body and must not be used for routine refreshes. Frontmatter updates have separate field ownership and merge strategies; placing text outside the managed region alone does not protect managed YAML properties.

## Appearance and navigation

- Use native `abstract`, `info`, `tip`, `example`, `warning`, `question` and `note` callouts with explicit titles such as “原文结论” or “补充推导”. Meaning/attribution must be readable without colors.
- Keep ordinary narrative as paragraphs. Fold long proofs/code with `[!info]-` or `[!example]-`. Every line of a callout, including blank lines, code fences and math fences, needs a `>` prefix.
- Use headings, existing wikilinks and stable block IDs for lookup. Avoid ambiguous duplicate filenames by linking vault-relative paths.
- Store original figure/crop assets inside the vault with portable relative links, grouped by stable paper identity. A Zotero reader URI points to the actual verified library/attachment; do not fabricate page parameters.
- Use `$...$` and `$$...$$` for Obsidian files. Chat formulas continue to follow user-specific instructions. Do not rely on CSS to repair broken math.
- Use Mermaid for useful method/dependency diagrams, Markdown tables for comparisons, and task lists for concrete questions. Additional plugins, CSS and concept-note creation are optional.
- `assets/paper-note.css` is scoped to `.paper-reading`. Add that CSS class only if the style is enabled or desired. Do not alter unrelated note appearance or install third-party plugins by default.

## Work state

Use a configured local folder, e.g. `<vault>/.paper-reading/work/<library>-<parent-key>/`. Before a key exists use a stable DOI/arXiv-derived token; migrate state once resolved. Keep work state and private snapshots out of a published skill repository.

Keep an inventory, outline with section statuses, issues, independently written checks and a compact stage record. A useful stage record includes source URL/version, library/item/attachment identity, note path, code commit, per-stage status and any retryable reason. Stage status is `pending`, `running`, `complete` or `blocked`. The record itself is an account of observations, not a simulated tool outcome.

Stages: identity, collection, PDF acquisition, fulltext reading, ZotLit shell, analysis, validation. Checkpoint after actual transitions. Resume by checking artifacts and identities, then perform missing work. After a source-version change, update dependent sections and validation. Keep check scripts referenced by the final note; do not delete the only evidence of verification.

Complete collection requires the real Zotero item, collection and PDF. Complete shell creation requires a real plugin-created linked note. Complete reading requires coverage of the body and appendices (across main/detail notes). Complete validation requires the checks actually reported, with UI rendering separately recorded as performed or untested. Blocked stages leave downstream stages incomplete.

## Structural validation

Run from any directory:

```bash
python3 /absolute/path/to/skill/scripts/validate_note.py \
  /absolute/path/to/note.md --vault /absolute/path/to/vault
```

The checker reads only: ownership/managed marker pairing and separation, parent identity, code-fence closure, display-math fence closure, unresolved template placeholders and existence of local wikilink embeds (including cross-platform relative paths). It does not fully parse YAML, Markdown or LaTeX, resolve every hyperlink, render the note, check factual coverage or verify citations. Read its diagnostics and manually check those remaining items. Do not describe a passing result as scientific validation.
