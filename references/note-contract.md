# Note identity, ownership and recovery

## Folder layout and naming

One paper has one folder directly under the configured literature root. The main file and folder use the same paper name. The default structure has one self-contained main note and, when useful, one sibling experiment note. Figures and verification scripts use support directories; reading notes have no topic subfolders.

```text
Papers/
└── METHOD/
    ├── METHOD.md             background, setup, full method, proofs/code and limitations
    ├── 实验分析.md           optional: settings, detailed results and ablations
    ├── _assets/              figures and crops, not reading notes
    └── checks/               retained independent numerical scripts
```

`METHOD` is an illustrative name, not a template variable or real method. In actual notes, use the following naming order:

1. An explicit name supplied by the user.
2. The authors' method/framework name promoted in the title, abstract or main method section. Preserve its spelling and case; when several names appear, choose the main contribution, not a baseline or subordinate module.
3. If the paper proposes no named method, use a concise name of its actual research object or a shortened paper title. Record this as a descriptive filename, not an author-coined method or invented acronym. Do not force a theory, survey or benchmark paper into a method name.

Sanitize filesystem-invalid characters, reserved names and trailing spaces/dots consistently in both the folder and main filename. Preserve the original method spelling in metadata/text. Before creation, look up library + item identity across existing notes. If the same paper exists, resume it; an alias, version or name change does not create a new folder.

If a different paper already owns the name, disambiguate the new folder/main basename using the publication year; if necessary append library and item identity. For example, `METHOD (2026-<library>-<key>)`. Never merge same-name papers or overwrite existing content. Store the resolved `paper_name` separately from the original `method_name`; omit `method_name` when no author-named method exists.

The main file is the only ZotLit literature note and the complete conceptual reading. Include bibliographic/PDF access, background and prior gaps, problem setup, the full method, necessary theory and explanatory code, limitations and applicable boundaries, plus the key empirical findings needed to assess the method. It must stand on its own rather than act as a navigation stub. Long proofs/code use local collapsible blocks. If an experiment note exists, link to it for settings, detailed tables/results, ablations and supplementary experiments. Use full vault-relative links in both directions because `实验分析.md` recurs across methods. Link only to an actual file.

Use `type: paper-detail`, `topic: experiments`, and `parent-note: "[[Papers/METHOD/METHOD]]"` in the experiment note. Replace the shown path with the actual resolved path. This note has no native `zotero-key`; its parent supplies Zotero access and identity. A short header should visibly link back to the main note as well.

For new papers, start with the main note. Add `实验分析.md` only when experimental details warrant a separate file; otherwise keep them in the main note. Do not create a separate `方法理解.md`, `理论推导.md` or `代码解读.md` by default. Split into additional topics only at the user's explicit request. Full-text extracts and work records live in work state, not as extra reading notes scattered through the vault.

When reorganizing an existing paper is requested, inventory its main/child files and manual edits, plan collision-free moves, perform supported Obsidian moves, repair affected internal links and checkpoint paths, then verify ZotLit lookup. Do not merge or delete existing content just to fit the new outline. Changing this skill alone does not move existing vault files.

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

The following plugin region belongs to the main note only. Main and child notes both have distinct AI and user areas; children omit a ZotLit managed region and carry only their parent link. The same manual-edit preservation rules apply to every file.

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
  /absolute/path/to/note.md --vault /absolute/path/to/vault \
  --paper-folder /absolute/path/to/vault/Papers/METHOD
```

The checker reads only: ownership/managed marker pairing and separation, parent identity, code-fence closure, display-math fence closure, unresolved template placeholders and existence of local wikilink embeds (including cross-platform relative paths). With `--paper-folder`, it also checks that the note and its main parent share that folder, that the main filename matches the folder name, and that a child points to an existing main note with native identity. By default, a child must be named `实验分析.md` with `topic: experiments`. Use `--allow-extra-notes` only for an explicitly user-requested additional topic split; it retains the same folder, parent identity and region checks. The checker does not check whether the chosen method name is scientifically appropriate or whether the main note explains the method completely; review those against the source. It does not fully parse YAML, Markdown or LaTeX, resolve every hyperlink, render the note, check factual coverage or verify citations. Read its diagnostics and manually check those remaining items. Do not describe a passing result as scientific validation.
