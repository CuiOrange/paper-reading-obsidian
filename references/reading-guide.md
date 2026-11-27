# Reading and explanation

## Reader and depth

Assume a CS undergraduate foundation: calculus, linear algebra, probability, algorithms and introductory machine learning. Explain specialist concepts at first use with intuition, definition and role in this paper. Familiarity with a research area does not establish mastery of all its tools.

Read the complete body and supplements. Inventory all substantive definitions, assumptions, results and proofs, algorithms, numbered equations, figures, tables, experimental details and reference roles. Record paper locations and the note section covering each. Number coverage finds omissions; it does not prove understanding or correctness.

Write in your own words following the argument. Preserve conditions, negative findings and uncertainty. Use the structure below, adapted from paper-explainer. The full Part I belongs in the method-named main note; it must stand alone as an explanation of the method and evidence. Keep only essential bibliographic properties as specified in `note-contract.md`; omit a separate reading guide and do not add workflow properties. Part II can follow in the same note with folded details, or live in one optional sibling `附加笔记.md` (or `Details.md` for English, identified by filename and a visible return link; no type/topic/parent properties). Its content remains required when applicable even if no extra file is created. Do not split main experiments or ablations out of Part I. Do not create separate method, experiment, theory or code files by default. Keep all Markdown notes directly in the paper folder and link to content rather than repeating it.

## Opening abstract translation

Immediately after the main note's properties, without a repeated note-name/title heading, place an expanded callout with the exact title `TL;DR` using native Obsidian syntax `> [!abstract] TL;DR`. Its content is the complete abstract translated into the note's language, not a shortened takeaway or the explainer's assessment. If the source is already in that language, preserve its wording. Use the abstract from the exact version read, verified against the paper PDF/source or authoritative abstract page; do not mix versions or reconstruct it from the introduction. Preserve all claims, scope, modality, numerical results, comparisons, technical terms and meaningful paragraph structure. Use the same term translations throughout the note and keep necessary English method names/acronyms. Do not strengthen a claim, omit a qualification or insert commentary; any explanation belongs in Part I. If the actual abstract cannot be obtained, record that limitation rather than inventing a translation.

The callout is ordinary visible Markdown; do not wrap it in HTML comments or ZotLit markers. Prefix every content/blank line with `>`; leave the callout expanded (no `-` collapse suffix). Put the single Zotero/article source line immediately after the callout. The required abstract translation precedes Part I's independently written plain-language overview; they serve different purposes. Imported Zotero notes/annotations go later in the file so they do not displace the opening abstract. Do not repeat the translation in the optional detail note.

## Outline

### Main-note hierarchy

After the TL;DR and single source line, use exactly seven unnumbered H1 groups in the order below. Section wording may fit the actual paper, but the nesting must remain. Do not repeat the note title or add a “Part I” wrapper. The numbering in this instruction is a planning aid only, never heading text in a note.

1. **Plain-language explanation:** tell the problem, prior gap, core idea, results, decisive observations and significance in coherent prose. No displayed formulas or derivations. Motivation belongs here rather than a separate background chapter.
2. **Prerequisites:** explain only specialist tools needed beyond a CS undergraduate background. If no separate tools are needed, give one concise statement of the assumed foundation, not a glossary or an empty placeholder.
3. **Method overview:** use H2 subsections for **problem setup and overall pipeline**, then **each substantive component** in argument order. Introduce inputs/outputs, assumptions, notation and a useful pipeline diagram in setup. For each component, give exact formulas/algorithms, its role, non-obvious conditions, relevant annotated code and proof ideas. A theory paper uses main results/dependencies as the component subsections, with exact original result numbers and a plain-language meaning; full proofs can move to the optional detail note. Do not promote setup or individual components to separate H1 sections.
4. **Experiments:** use H2 subsections for **main experiments** and **ablations/analysis**. Include settings needed to interpret the evidence, full main tables, original figures, what each experiment establishes, sensitivity and negative findings. Main results and substantive ablations stay here. If the paper has no experiments, state this fact briefly within this group; do not invent results or delete the group.
5. **Discussion:** explain related-work differences, the authors' conclusions/limitations, and separately attributed evidence-based assessment and open questions. Verified relevant follow-up work is optional. Do not write the user's own opinions here.
6. **Appendix:** one H1 `附录` in Chinese or `Appendix` in English. Use H2 subsections for method/component lookup, notation, version differences, errors/consistency checks and references with their roles. Keep lookup tables concise and introduce no new method claims. All these topics belong here, not in standalone top-level sections.
7. **Personal thoughts:** the last H1 group, such as `思考` / `My thoughts`. Preserve existing user text and leave it unfilled otherwise. Do not invent first-person reflections.

All lower-level headings are unnumbered too. Keep original equation/theorem/algorithm/figure numbering; this is independent of note heading numbers. Avoid repeated statements/formulas and routine section summaries. The source title can be in properties, while chapter references use the existing `ch` convention.

### Heading example

```markdown
# 不用公式讲解
# 前置知识
# 方法概述
## 问题设定和总览
## 组件一的实际名称
## 组件二的实际名称
# 实验
## 主实验
## 消融与分析
# 讨论
# 附录
## 方法定位
## 符号表
## 版本差异
## 错误与一致性检查
## 参考文献及其作用
# 思考
```

Replace component placeholders with the actual contributions; add or remove component subsections as needed. Retain all seven H1 groups and their responsibilities in the stated order, including for theory papers. Variants such as “实验评估” for experiments or “贡献与局限” for discussion are fine.

### Part II: complete proofs and details — optional separate note

Organize long derivations from the main text first, followed by proofs and derivations in the order of the paper's appendices. Fill nontrivial omitted steps. Link to a theorem/equation already stated in Part I rather than restating it. State an auxiliary result here if it appears only here.

For experiment-driven papers, also include full hyperparameter tables, training and evaluation procedures, implementation details and supplementary experiments. Do not move the main results or substantive ablations out of Part I merely to shorten the main note. Short code that explains the mechanism stays in Part I; extended implementation context can go here.

When complete details are substantial, use `附加笔记.md` (English: `Details.md`); otherwise fold them beside the method argument they support, or put them as subsections of the appendix. Do not introduce another H1 group in the main note for “Part II” or complete details. Main-to-detail links should target the relevant heading/block; include a visible return link in the detail note. Separate-file placement is optional, coverage is not.

### Appendix contents — one group before personal thoughts

Within the single H1 `附录` / `Appendix`, keep the following unnumbered H2 subsections, after method/component lookup and the notation table. Fold long tables. Do not create a third Markdown note or promote appendix subsections to H1:

- **版本差异 / Version differences:** substantive differences between the version read and the formal published version. Say when no formal version exists, could not be obtained or has no substantive differences; do not fabricate a comparison.
- **错误与一致性检查 / Errors and consistency checks:** confirmed location, issue, correction, verification and scope. Distinguish missing proof steps from false claims. If nothing was found, state what was actually checked; do not claim independent review unless it happened.
- **参考文献及其作用 / References and their roles:** cover every reference in the version read. Identify references supplying results/methods/data/code individually; group peripheral references by purpose. Avoid repeating the related-work discussion.

Within the required groups, remove inapplicable component/detail placeholders rather than filling them with boilerplate. For version comparisons or checks that cannot be performed, state the actual availability or scope briefly in their appendix subsection. Inventory coverage spans the main note and Part II; keep a single canonical location for each full statement, proof, formula and result table.

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
| 方法定位 | Method and component lookup |
| 符号表 | Notation |
| 附录 | Appendix |
| 完整证明与细节 | Complete proofs and details |
| 我的思考 | My thoughts |
| 论文原文 | Paper |
| 返回主笔记 | Return to main note |

At first use of a term, give its English original: Chinese explanations use “中文译名（English original）”, then consistently use that Chinese translation thereafter. For example, introduce 线性探测（linear probe） once and use 线性探测 subsequently. This applies to translated method names, specialist terms and metrics, including those first introduced in the abstract translation. Keep case, punctuation and acronyms faithful to the paper. An original English method/acronym such as DDM-SSCC or DiffuGPT stays unchanged; give its expansion only if verified. English notes use the original terms directly, with an acronym expansion at first use when useful. Keep all math symbols and source labels intact.

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

## Algorithm pseudocode with line numbers

When an algorithm helps explain the method, use the line-numbered, ruled MathJax format below inside `$$...$$`. Place it beside the corresponding method/component explanation under the existing hierarchy, not in a new top-level group or file. Use `array{r l}` for right-aligned line numbers and left-aligned statements, nested inside `array{l}` with `\hline` around the title and body. Use `\quad` / `\qquad` for nesting and explicit `end if` / `end for` where applicable. Keep the block adjacent to its explanatory prose without empty lines.

- Transcribe the paper's algorithm faithfully, preserving its original identifier, inputs/outputs, initialization, operation order, conditions, loop scope and termination behavior. If line numbers are added or changed, references to them must clearly mean the note's line numbers rather than the source's.
- Label independently reconstructed or simplified algorithms as “补充伪代码” / “Explanatory pseudocode”, cite the actual source section/equation and identify meaningful omissions. Use the paper's notation; do not invent a source algorithm number or fill missing implementation details with assumptions.
- Match the title, input/output labels and explanations to the note language: `算法 / 输入 / 输出` in Chinese, `Algorithm / Input / Output` in English. Control-flow keywords such as `for`, `if`, `break` and `return` may stay in English in either language. Explain unfamiliar keywords once when needed.
- MathJax does not load full LaTeX algorithm packages through `$$...$$`. Use the array-based syntax here rather than `algorithm`, `algorithmic`, `algorithm2e`, `\State`, `\For`, `\caption` or `\usepackage`. Keep real author-code excerpts in fenced code blocks with the appropriate programming language.
- Maintain line numbers manually. Split long statements with continuation indentation or explain them in prose; avoid oversized arrays and large paragraphs of comments. Verify rendering in Obsidian when accessible, including nested indentation and line-number alignment.

This self-written gradient-descent example demonstrates formatting only. Replace its title, symbols and operations with the actual paper's algorithm; do not copy its optimization or stopping rule into an unrelated note. Here $f$ is differentiable, $\theta_0$ is the initial parameter, $\eta>0$ is the step size, $T$ is a nonnegative integer update limit and $\varepsilon\geq0$ is the gradient-norm threshold. The loop checks the gradient before updating and returns the initialized parameter even when $T=0$.

```latex
$$
\begin{array}{l}
\hline
\textbf{Algorithm 1}\quad\text{Gradient Descent} \\
\hline
\begin{array}{r l}
& \textbf{Input: } f,\ \theta_0,\ \eta,\ T,\ \varepsilon \\
& \textbf{Output: } \theta \\
1: & \theta \leftarrow \theta_0 \\
2: & \mathbf{for}\ t=1,\ldots,T\ \mathbf{do} \\
3: & \quad g \leftarrow \nabla f(\theta) \\
4: & \quad \mathbf{if}\ \lVert g\rVert_2\leq\varepsilon\ \mathbf{then} \\
5: & \qquad \mathbf{break} \\
6: & \quad \mathbf{end\ if} \\
7: & \quad \theta \leftarrow \theta-\eta g \\
8: & \mathbf{end\ for} \\
9: & \mathbf{return}\ \theta
\end{array} \\
\hline
\end{array}
$$
```

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
