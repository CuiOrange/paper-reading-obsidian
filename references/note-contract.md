# Note identity, ownership and recovery

## Folder layout and naming

One paper has one folder directly under the configured literature root. The main file and folder use the same paper name. All of Part I and the explainer appendices stay in the main note. Part II can be inline or in one optional sibling detail note in the output language. Only image attachments use a support directory inside the paper folder. Verification scripts and outputs live temporarily outside the vault; reading notes have no topic subfolders.

```text
Papers/
└── METHOD/
    ├── METHOD.md             Part I and explainer appendices; only essential bibliographic properties
    ├── 附加笔记.md           optional: Part II, complete proofs and full details
    └── images/              original figures, crops and explanatory diagrams
```

`METHOD` is an illustrative name, not a template variable or real method. In actual notes, use the following naming order:

1. An explicit name supplied by the user.
2. The authors' method/framework name promoted in the title, abstract or main method section. Preserve its spelling and case; when several names appear, choose the main contribution, not a baseline or subordinate module.
3. If the paper proposes no named method, use a concise name of its actual research object or a shortened paper title. Record this as a descriptive filename, not an author-coined method or invented acronym. Do not force a theory, survey or benchmark paper into a method name.

Sanitize filesystem-invalid characters, reserved names and trailing spaces/dots consistently in both the folder and main filename. Preserve the original method spelling in metadata/text. Before creation, look up library + item identity across existing notes. If the same paper exists, resume it; an alias, version or name change does not create a new folder.

If a different paper already owns the name, disambiguate the new folder/main basename using the publication year; if necessary append library and item identity. For example, `METHOD (2026-<library>-<key>)`. Never merge same-name papers or overwrite existing content. Store the resolved paper name and original method name, when needed, in the external checkpoint or prose rather than additional note properties.

The main file is the only ZotLit literature note. Its properties hold only essential bibliography; its body has the single Zotero/article source line. Its body contains all of Part I as defined in `reading-guide.md`, including main experiments and substantive ablations, with lookup/source-check material inside one appendix group, followed by personal thoughts. It is a complete conceptual reading, not a navigation stub. Part II may follow inline or live in `附加笔记.md`; use collapsible blocks for long passages. Use full vault-relative links in both directions, with heading/block targets for the statement-to-proof route. Link only to files actually created.

Identify `附加笔记.md` (English: `Details.md`) by its filename and visible return link to `[[Papers/METHOD/METHOD]]` (replace with the actual vault-relative path). Do not add type, topic, parent-note or Zotero properties. Organize its body as Part II, not as a second general introduction.

For new papers, start with the main note. Create `附加笔记.md` only when separating Part II helps reading. Otherwise retain all applicable Part II content inline. Do not create separate `方法理解.md`, `实验分析.md`, `理论推导.md` or `代码解读.md` by default. Additional topic files require an explicit user request. Full-text extracts and work records remain in work state.

When reorganizing an existing paper is requested, inventory its main/child files and manual edits, plan collision-free moves, perform supported Obsidian moves, repair affected internal links and checkpoint paths, then verify the saved identity mapping and body Zotero link. Do not merge or delete existing content just to fit the new outline. Changing this skill alone does not move existing vault files.

Do not generate `zotero_notes/` (including at the vault root) or a separate exported Markdown file for each Zotero note/annotation. Zotero remains the owner of the originals. Read them without exporting child-note files and integrate relevant quotations or observations into the existing main/detail note with attribution. Annotation image copies used in the note belong in its shared `images/`. Do not call automatic bulk/child-note export commands or template helpers that create a note-export directory. If an existing integration cannot avoid creating that directory, use a read-only retrieval path for the annotations and update the already resolved paper note instead. Existing user files are not deleted merely by changing this rule.

## Minimal properties and source links

Final frontmatter has only these five allowed keys, in this order when available:

```yaml
title: "Original paper title"
authors:
  - "Author name"
venue: "arXiv"
code: "https://verified-author-repository"
year: 2026
```

This is a schema example, not content to copy literally. Use the actual conference/journal name, or `arXiv` for an arXiv-only preprint; do not invent a venue. Keep author names as a list. Use the actual publication year, or the preprint year when no formal publication is verified. Omit unknown values, including `code` if no author repository is verified; do not fill placeholders. The title is required. Reuse these essential fields in the optional detail note only when useful; it can use title alone.

Remove all Zotero properties (`zotero-key`, library/item/attachment identifiers, `citekey`, `collections`, Zotero URLs) and auxiliary workflow properties (`type`, `topic`, `parent-note`, reading/verification statuses, dates, reading routes, prerequisites, duplicate titles/method names, DOI/arXiv identifiers, and extra URL fields). Do not insert comments or hidden YAML keys to retain them. Do not add CSS properties by default. Keep source/version details in the relevant body discussion or external checkpoint instead.

After the opening TL;DR in the main note, put one short source line (`Paper` replaces `论文原文` in English):

```markdown
[Zotero](zotero://select/library/items/VERIFIED_KEY) · [论文原文](https://verified-article-page)
```

Replace both example targets with verified values; use the actual personal/group-library URI. Choose one authoritative article page (preferably version-specific when available), or the actual PDF when no article page is available. Do not also add PDF, DOI, arXiv or repeated article-page URLs elsewhere in the note. Source attributions later use `ch` section references or equation/figure identifiers, with no page numbers attached to chapter references and internal links to the single source line or relevant explanation. The optional detail note uses a visible, full vault-relative return link to the main note and inherits these two source links rather than duplicating them. Do not keep its parent link in frontmatter.

Verify a newly created ZotLit shell against the real Zotero record before removing plugin fields. Preserve the item/library/attachment identity, source version, current main/detail paths and any necessary update baseline in the compact external checkpoint. On future reads, match that record and the main body jump link to locate the existing note. Treat its Zotero association as a verified link, not a guarantee of native plugin indexing: deleting `zotero-key` may prevent ZotLit lookup and ordinary refresh. Do not invoke a create/refresh/metadata operation that duplicates the note or re-adds unwanted fields. Use supported Obsidian edits against the resolved file; do not change global plugin settings merely to enforce this note schema.

## Visible content and preservation

Delivered notes contain no HTML comments, no `paper-reading:*` ownership markers, and no ZotLit managed delimiters (neither the opening nor closing line). Do not place hidden identifiers in the body or substitute another hidden marker. Preserve useful imported annotations as ordinary visible Markdown with attribution. The bundled note template deliberately does not render the named `content` template, since the plugin can wrap it in managed markers.

For a new note, verify the real ZotLit creation and identity first, then remove plugin marker lines while retaining their enclosed content; also apply the minimal property schema. For an explicitly requested revision of an old note, strip only ownership comments/delimiter lines and preserve the enclosed text. Never run a regex rewrite across original program snippets or quotations as incidental formatting cleanup; use targeted edits.

Before an update, read the complete current note. Keep the last generated baseline, user-owned passages/sections and integration mapping in the compact external checkpoint when needed. Compare actual content with that baseline and merge changes. Without a baseline, make targeted additions/revisions rather than assuming the entire note is generated. Preserve “我的思考” / “My thoughts” as an ordinary visible user section and never invent the user's first-person judgments. Do not invoke ZotLit refresh/overwrite/metadata commands that re-add markers, properties or duplicates after cleanup.

## Appearance and navigation

The main note starts with properties, then immediately the expanded TL;DR and the single source-link line. Keep the paper title in the filename/title property; do not repeat the note name, method name or title property as an extra body heading. The same rule applies to the optional detail note. Use seven unnumbered H1 groups in order: plain-language explanation, prerequisites, method overview, experiments, discussion, appendix, personal thoughts. Put setup and individual components under method overview at H2; put main experiments and ablations under experiments at H2. Method lookup, notation, version differences, errors/checks and reference roles all use H2 inside the single H1 `附录` / `Appendix`. Do not add separate top-level lookup or version/reference sections. The thoughts group stays last. Wording can vary; this hierarchy cannot. Do not add a “Part I / 第一部分” wrapper or heading numbers. Detail notes likewise use unnumbered headings and a visible return link. Keep source equation/theorem/figure numbering. Do not add HTML comments or managed delimiters.

- Use native `abstract`, `info`, `tip`, `example`, `warning`, `question` and `note` callouts with explicit titles such as “原文结论” or “补充推导”. Meaning/attribution must be readable without colors.
- Keep display formulas adjacent to prose without empty lines, while retaining necessary heading/list/table spacing. Arrange comparable tall figures in a two- or three-column Markdown image row with captions in the next data row; see `reading-guide.md`.
- Keep ordinary narrative as paragraphs. Fold long proofs/code with `[!info]-` or `[!example]-`. Every line of a callout, including blank lines, code fences and math fences, needs a `>` prefix.
- Use headings, existing wikilinks and stable block IDs for lookup. Avoid ambiguous duplicate filenames by linking vault-relative paths.
- Store all note image attachments (original figures, PDF crops, annotation images and explanatory diagrams) in `<literature-root>/<paper-name>/images/`, a sibling directory of `<paper-name>.md` and optional `附加笔记.md`. Create it when the first image is saved; both notes share it. Use descriptive, collision-safe filenames such as `fig-02-pipeline.png` and reuse an existing image rather than creating a duplicate. Embed with portable vault-relative wikilinks such as `![[Papers/METHOD/images/fig-02-pipeline.png]]` (replace the example path), or standard Markdown relative links such as `![方法流程](images/fig-02-pipeline.png)`. Retain source/figure/page attribution. Do not rely on temporary paths, absolute filesystem paths, external hotlinks or a global attachment folder for newly added note images. Keep bibliographic PDFs in Zotero; this rule governs the note's image copies. A Zotero reader URI points to the actual verified library/attachment; do not fabricate page parameters.
- Use `$...$` and `$$...$$` for Obsidian files. Chat formulas continue to follow user-specific instructions. Do not rely on CSS to repair broken math.
- Use Mermaid for useful method/dependency diagrams, Markdown tables for comparisons, and task lists for concrete questions. Additional plugins, CSS and concept-note creation are optional.
- `assets/paper-note.css` is scoped to `.paper-reading`. Add that CSS class only if the style is enabled or desired. Do not alter unrelated note appearance or install third-party plugins by default.

## Work state

For a long or interrupted reading, reuse one compact local checkpoint outside the paper folder, e.g. `<vault>/.paper-reading/work/<library>-<parent-key>/state.json`. Before a key exists use a stable DOI/arXiv-derived token. Consolidate identity, coverage inventory, outline, issues, stage state and any previous generated-content baseline needed for preserving edits in that checkpoint rather than separate Markdown inventories, reports or log files. Do not persist executable checks or raw check outputs there. Keep private state out of a published skill repository.

Keep the coverage inventory, outline with section statuses, issues and compact stage record together in the checkpoint when one is needed. A useful stage record includes source URL/version, library/item/attachment identity, note path, code commit, per-stage status and any retryable reason. Stage status is `pending`, `running`, `complete` or `blocked`. The record itself is an account of observations, not a simulated tool outcome.

Stages: identity, collection, PDF acquisition, fulltext reading, ZotLit shell, analysis, validation. Checkpoint after actual transitions. Resume by checking artifacts and identities, then perform missing work. After a source-version change, update dependent sections and validation. Before removing temporary checks, retain the meaningful verification facts in the note or checkpoint: what was tested, inputs/seed where relevant, method, actual result and scope. Avoid a standalone verification document or links to temporary scripts/results.

Complete collection requires the real Zotero item, collection and PDF. Complete shell creation requires a real plugin-created linked note. Complete reading requires coverage of the body and appendices (across main/detail notes). Complete validation requires the checks actually reported, with UI rendering separately recorded as performed or untested. Blocked stages leave downstream stages incomplete.

## Temporary checks and cleanup

Generated check scripts, a generated `checks/` directory, raw outputs, screenshots used only for QA, and validation logs belong in a task-owned system temporary directory outside the vault and installed skill. Use the system temp API, e.g. `tempfile.TemporaryDirectory(prefix="paper-reading-")`, with `checks/` beneath it if useful. Do not hardcode one platform's temp path, use the paper folder as scratch space or copy checks into the delivered notes.

Execute the check, capture its outcome, and write only the essential verification facts into an existing note or checkpoint. Then remove its scripts, outputs and owned temporary directory in `finally` (or the context manager's exit), including when a check fails. Record a failure and the remaining uncertainty before cleanup; recreate a check when retrying instead of retaining its executable files. If interruption prevents cleanup, remove only this task's identified temporary directory on resume. Never clear the system temp root or someone else's files.

No finished note may link to a deleted script, output JSON or screenshot. Cite the source location and describe the check's inputs, method, outcome and limits in prose. Keep images actually used in the note in `images/`; only QA-only screenshots are temporary. The reusable `scripts/validate_note.py` shipped with this skill stays in the skill package and runs read-only; it is not a per-paper generated check to delete.

## Structural validation

Run from any directory:

```bash
python3 /absolute/path/to/skill/scripts/validate_note.py \
  /absolute/path/to/note.md --vault /absolute/path/to/vault \
  --paper-folder /absolute/path/to/vault/Papers/METHOD
```

The checker reads only: absence of hidden markers, unnumbered direct headings, compact display-math spacing, minimal property keys, source-link counts, visible parent link, code-fence closure, display-math fence closure, unresolved template placeholders and existence of local wikilink embeds (including cross-platform relative paths). With `--paper-folder`, it also checks that the note and its main parent share that folder, that the main filename matches the folder name, and that a child visibly links to the existing main note. By default, a child must be named `附加笔记.md` or `Details.md`, with its parent expressed only as a visible return link. Use `--allow-extra-notes` only for an explicitly user-requested additional topic split; it retains the same folder, visible parent-link and formatting checks. The checker does not check whether the chosen method name is scientifically appropriate or whether the main note explains the method completely; review those against the source. It does not fully parse YAML, Markdown or LaTeX, resolve every hyperlink, render the note, check factual coverage or verify citations. Read its diagnostics and manually check those remaining items. Do not describe a passing result as scientific validation.
