# Reading and explanation

## Reader and depth

Assume a CS undergraduate foundation: calculus, linear algebra, probability, algorithms and introductory machine learning. Explain specialist concepts at first use with intuition, definition and role in this paper. Familiarity with a research area does not establish mastery of all its tools.

Read the complete body and supplements. Inventory all substantive definitions, assumptions, results and proofs, algorithms, numbered equations, figures, tables, experimental details and reference roles. Record paper locations and the note section covering each. Number coverage finds omissions; it does not prove understanding or correctness.

Write in your own words following the argument. Preserve conditions, negative findings and uncertainty. Use the structure below, adapted from paper-explainer. The full Part I belongs in the method-named main note; it must stand alone as an explanation of the method and evidence. Keep only essential bibliographic properties as specified in `note-contract.md`; omit a separate reading guide and do not add workflow properties. Part II can follow in the same note with folded details, or live in one optional sibling `附加笔记.md` (or `Details.md` for English, identified by filename and a visible return link; no type/topic/parent properties). Its content remains required when applicable even if no extra file is created. Do not split main experiments or ablations out of Part I. Do not create separate method, experiment, theory or code files by default. Keep all Markdown notes directly in the paper folder and link to content rather than repeating it.

## Opening abstract translation

Immediately after the main note's properties, without a repeated note-name/title heading, place an expanded callout with the exact title `TL;DR` using native Obsidian syntax `> [!abstract] TL;DR`. Its content is the complete abstract translated into the note's language, not a shortened takeaway or the explainer's assessment. If the source is already in that language, preserve its wording. Use the abstract from the exact version read, verified against the paper PDF/source or authoritative abstract page; do not mix versions or reconstruct it from the introduction. Preserve all claims, scope, modality, numerical results, comparisons, technical terms and meaningful paragraph structure. Use the same term translations throughout the note and keep necessary English method names/acronyms. Do not strengthen a claim, omit a qualification or insert commentary; any explanation belongs in Part I. If the actual abstract cannot be obtained, record that limitation rather than inventing a translation.

The callout is ordinary visible Markdown; do not wrap it in HTML comments or ZotLit markers. Prefix every content/blank line with `>`; leave the callout expanded (no `-` collapse suffix). Put the single Zotero/article source line immediately after the callout. The required abstract translation precedes Part I's independently written plain-language overview; they serve different purposes. Imported Zotero notes/annotations go later in the file so they do not displace the opening abstract. Do not repeat the translation in the optional detail note.

## Outline

### Part I: understanding the paper — always in the main note

For experiment-driven papers (methods, systems and benchmarks):

1. **The whole paper in plain language:** roughly one to two pages of coherent prose covering the concrete problem, prior gap, core idea, main results, decisive experimental observations, significance and limitations. No displayed formulas or derivations. Introduce only a few key quantities if necessary.
2. **Necessary prerequisites (optional):** tools beyond a CS undergraduate background. For each, give intuition, the definition/properties needed here and its role. Omit this section if short local explanations suffice.
3. **Problem setup and method overview:** task, inputs/outputs, assumptions and an overall pipeline diagram. Introduce notation as it appears.
4. **Key designs:** one substantial design per section, in the order of the argument. Give precise original formulas/algorithms and numbering, explain mechanism and non-obvious conditions, and sketch long derivations. Place short annotated author-code excerpts at the step they clarify. Use descriptive headings, not a single undifferentiated method dump.
5. **Main experiments:** settings needed to interpret the results, all main result tables retyped in full, original figures, and a concise explanation of which claims each experiment supports. These stay in the main note even when long; fold tables/figures when useful.
6. **Ablations and analysis:** component effects, sensitivity and other substantive analyses, including negative results and qualifications.
7. **Discussion:** relevant lines of related work; the authors' conclusions and stated limitations; separately attributed, evidence-based strengths, limitations and open questions. Add only verified, directly relevant follow-up work when useful. Leave user-owned thoughts to the user.
8. **At a glance:** method component | role | formula/algorithm | note location, followed by a notation table. Tables only; introduce no new claims.

For theory papers, use: plain-language overview → optional prerequisites → problem setup → one section per main result in argument order → experiments when present → discussion → at-a-glance results and notation tables. Each main result has its exact statement, original number, one plain-language sentence on meaning, relevant conditions and proof idea. Add a result dependency diagram when it helps. Full proofs belong in Part II.

Do not add a separate generic background chapter. Motivation and contributions belong in the opening overview; prior methods needed for understanding belong in prerequisites/setup. Section titles describe their content. The outline list above specifies content responsibilities, not numbered headings: write them as unnumbered H2 content headings directly after the opening callout/source line, without a note-title wrapper, with unnumbered H3 subsections. “Part I/II” are planning labels only, never an extra title level in the delivered notes. Original numbered equations/results/figures retain their source identifiers. Avoid repeated motivation, repeated statements/formulas and routine end-of-section summaries. Use undergraduate knowledge directly.

### Part II: complete proofs and details — optional separate note

Organize long derivations from the main text first, followed by proofs and derivations in the order of the paper's appendices. Fill nontrivial omitted steps. Link to a theorem/equation already stated in Part I rather than restating it. State an auxiliary result here if it appears only here.

For experiment-driven papers, also include full hyperparameter tables, training and evaluation procedures, implementation details and supplementary experiments. Do not move the main results or substantive ablations out of Part I merely to shorten the main note. Short code that explains the mechanism stays in Part I; extended implementation context can go here.

When Part II is substantial, use `附加笔记.md`; otherwise keep it after Part I in the main note, using collapsible callouts for long passages. Main-to-detail links should target the relevant heading/block; include a visible return link in the detail note. Separate-file placement is optional, coverage is not.

### Explainer appendices — end of the main note

Keep the original three appendix responsibilities as compact sections after Part I (or after inline Part II). Fold long tables. Do not create a third Markdown note by default:

- **版本差异 / Version differences:** substantive differences between the version read and the formal published version. Say when no formal version exists, could not be obtained or has no substantive differences; do not fabricate a comparison.
- **错误与一致性检查 / Errors and consistency checks:** confirmed location, issue, correction, verification and scope. Distinguish missing proof steps from false claims. If nothing was found, state what was actually checked; do not claim independent review unless it happened.
- **参考文献及其作用 / References and their roles:** cover every reference in the version read. Identify references supplying results/methods/data/code individually; group peripheral references by purpose. Avoid repeating the related-work discussion.

Remove inapplicable scaffold headings instead of filling them with boilerplate. Inventory coverage spans the main note and Part II; keep a single canonical location for each full statement, proof, formula and result table.

## Language and English counterparts

An English user request, such as “Read this paper and save English notes in my Obsidian vault, with Zotero collection and annotated code where available”, invokes the same pipeline as “精读这篇论文并存入 Obsidian，收录到 Zotero，适当补充注释代码”. An explicit requested output language wins over the language of the request; otherwise retain the Chinese default. Do not interpret English output as a shorter summary or an English abstract alone.

Use the selected language consistently for prose, headings, callout explanations, captions, links and newly written code comments. Chinese-to-English heading counterparts (choose one language, not both in every heading):

| 中文 | English |
|---|---|
| 不用公式讲清整篇论文 | The paper in plain language |
| 必要的前置知识 | Prerequisites |
| 问题设定与方法总览 | Problem setup and method overview |
| 关键设计与原理 | Key designs and mechanisms |
| 主要实验 | Main experiments |
| 消融实验与分析 | Ablations and analysis |
| 讨论、贡献与局限 | Discussion, contributions and limitations |
| 速查 | At a glance |
| 完整证明与细节 | Complete proofs and details |
| 我的思考 | My thoughts |
| 论文原文 | Paper |
| 返回主笔记 | Return to main note |

In Chinese, introduce each translated method name, specialist term and metric with its exact English original in parentheses: 无损图像压缩（lossless image compression）、分离信源信道编码（separate source-channel coding, SSCC）、峰值信噪比（peak signal-to-noise ratio, PSNR）、结构相似性（structural similarity, SSIM）. Apply this in the abstract translation too. Keep case, punctuation and acronyms faithful to the paper. Repeat the English original in a later independently read section when needed to avoid ambiguity, not mechanically after every occurrence. An original English method/acronym such as DDM-SSCC or DiffuGPT stays unchanged; give its expansion only if verified. English notes use the original terms directly, with an acronym expansion at first use when useful. Keep all math symbols and source labels intact.

## Compact typography and figures

Keep the opening TL;DR and normal Markdown structure, but place a display formula directly between its explanatory sentences without empty lines before or after the `$$` block. Every line in a callout still needs the `>` prefix. Blank lines needed around headings, lists and tables remain; do not flatten derivations into an unreadable single line.

Comparable tall figures, such as multiple two-panel ablation plots, may share two or three columns. Use this native Markdown structure; the first row contains the images, and the next data row contains their captions. There is no extra caption-only heading row. The separator row is Markdown syntax, not content:

```markdown
| ![[Papers/METHOD/images/fig-09.png\|300]] | ![[Papers/METHOD/images/fig-10.png\|300]] | ![[Papers/METHOD/images/fig-11.png\|300]] |
| :---: | :---: | :---: |
| 原文图 9：扩散步数。 | 原文图 10：位置选择。 | 原文图 11：恢复日程。 |
```

Replace the example paths/captions with actual figures and preserve English labels with the needed explanations. Escape a wikilink's width pipe as `\|` inside table cells; do not escape the column delimiters. If plots become too small to read, use two columns or separate rows. Do not change global theme/CSS to compact the page. Verify the table and formula rendering in Obsidian when accessible.

## Mathematics

- Preserve notation and original numbering. Explain symbols, domains/dimensions, assumptions, whether the relation is exact/approximate/an upper bound, and its purpose.
- Use ordinary MathJax-compatible expressions with `$...$` and `$$...$$`. Define needed notation explicitly; do not copy paper-specific LaTeX macros without expansion.
- Give each important result/equation a stable block ID such as `^paper-eq-6` or a unique heading. Link later discussion to it. New derivations have a separate label; do not impersonate original equations.
- Fill nontrivial omitted steps and identify their justification. Standard algebra may be written directly. A proof already stated elsewhere gets a link rather than a repeated theorem box.
- If the same symbol has different meanings, distinguish them and document the change.
- Original numerical values retain their precision. Computed examples are checked by independent scripts in a task-owned system temporary directory, with explicit inputs and seed where relevant. Record the essential setup, result and verification scope in the existing note, then delete the scripts and raw results after execution; do not create persistent `checks/` or check-report files. Follow the cleanup rules in `note-contract.md`. Do not present unexecuted output as observed.
- Toy examples are optional. Use a small example for an abstract quantity or counterintuitive mechanism; reuse its setup and keep example material sparse. Prefer a pipeline diagram for an ordinary computational pipeline.
- Check central identities on small instances when feasible, but distinguish this from proof. A verified counterexample can disprove a universal claim; passing instances cannot prove one.

## Figures, tables and experiments

Use the original figure asset when possible, otherwise a verified PDF crop. Inspect labels, legends and caption context. Add a brief explanation in the note language of what to look at. A simplified redraw supplements the original and is labeled as the note writer's diagram. Save every figure, crop or explanatory diagram used in the notes to the sibling `images/` folder and embed it with a portable link as specified in `note-contract.md`. Both the main and optional detail note share that folder.

Retype numerical tables and algorithms as text. Preserve all results, units and precision; main-result and substantive ablation tables stay in Part I; full hyperparameters and supplementary tables may go in Part II. Compare transcribed cells with the source, not merely the total set of numbers. Extracted text may lose column order, minus signs or superscripts: verify against the rendered PDF.

For each experiment ask what it tests, whether comparisons use matching conditions, and what the result establishes. Record optimizer, learning rate, batch size, epochs, data processing, hardware and evaluation configuration where reported. Separate percentage-point changes from relative percentage gains. Report missing settings as unreported, not inferred.

## Code next to the method

Verify that the repository is the authors' implementation; record a fixed commit. Third-party implementations can be included when useful but must be labeled.

Read loss functions, core modules, training/inference and evaluation code relevant to the contribution. Select short excerpts with comments in the note language explaining inputs, tensor shapes, variables and the operation's role. Position them next to the corresponding equation/algorithm; collapse long snippets.

Every snippet identifies:

- Repository, commit, relative file path and verified line range/permalink.
- Corresponding paper result/equation/module.
- Whether it is an annotated original excerpt, a simplified adaptation or explanatory pseudocode.
- Omitted branches/context and whether it has been executed.

Retain actual logic in original excerpts. Label simplifications and independently written pseudocode clearly. Link helpers instead of pretending incomplete fragments are standalone runnable programs. Respect license/attribution terms. Do not execute downloaded code, install dependencies or launch training merely to understand a snippet. Write independent tiny numerical checks when useful.

Distinguish an implementation detail from a genuine paper/code discrepancy; record the exact code and paper versions. A current repository may implement a later revision.

## Source discipline and issues

Use the actual paper version as primary evidence, with author code/configuration for implementation claims. External explanations are supplemental and attributed. Check an external theorem at its original source if a proof depends on its exact form.

Cite substantive claims with verified source identifiers: use `ch III-B`, `ch 3.2`, or a specific theorem/equation/figure/table identifier. Never use the section symbol. Do not append page numbers to a chapter reference. When a source has no section identifiers, a verified page location alone is an acceptable fallback; do not invent chapter numbering. Never reverse-generate an English quote from a Chinese summary. Quote only actual source text. Verify PDF index versus printed page mapping before adding a page-specific Zotero URI.

Before calling an error, check assumptions, symbol reuse, version differences and whether a missing proof step suffices to repair the argument. Record location, issue, candidate correction, verification and impact. Preserve unresolved doubts as questions. Keep unfavorable results and conditions affecting interpretation. A partial review is not a guarantee of correctness.

Use only existing, materially related notes, giving the specific relation. Group peripheral references by purpose; identify individually the results, methods, data and code this paper actually uses. New concept notes or cross-paper syntheses are separate work unless requested.
