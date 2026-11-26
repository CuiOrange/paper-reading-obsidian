# Reading and explanation

## Reader and depth

Assume a CS undergraduate foundation: calculus, linear algebra, probability, algorithms and introductory machine learning. Explain specialist concepts at first use with intuition, definition and role in this paper. Familiarity with a research area does not establish mastery of all its tools.

Read the complete body and supplements. Inventory all substantive definitions, assumptions, results and proofs, algorithms, numbered equations, figures, tables, experimental details and reference roles. Record paper locations and the note section covering each. Number coverage finds omissions; it does not prove understanding or correctness.

Write in your own words following the argument. Avoid sentence-by-sentence paraphrase. Preserve conditions, negative findings and uncertainty. The method-named main note must provide a complete explanation of the background, problem, method and limitations without requiring a second method note. Include essential formulas, derivations and annotated code at the point where they explain the mechanism. Use collapsible blocks to control length. Detailed experimental setup, results, ablations and supplementary tables may go in sibling `实验分析.md` (`type: paper-detail`, `topic: experiments`, with a vault-relative `parent-note` link to the main note). Keep the decisive experimental findings and what they support in the main note. Use one file if a separate experiment note adds no value. Do not create `方法理解.md`, or split theory/code into other files unless the user explicitly requests a different organization. All Markdown notes for this paper stay directly in the same folder. The inventory covers both files; do not duplicate full explanations or result tables.

## Outline

Use the following content map as sections, not mandatory files. The main note owns background, setup, the complete method/theoretical argument, necessary proofs and code, and limitations. The optional `实验分析.md` owns experimental details and results; the main note retains a concise account of the evidence needed to assess the method. A reader must be able to understand what the method does, why it works and where it fails by reading the main note alone. Retain this division of labor:

1. **Reading entrance:** concrete problem, existing gap, core idea, main findings and boundaries in a few coherent paragraphs, mostly without formulas. No derivations here.
2. **Preliminaries and setup:** unfamiliar tools, task, inputs/outputs, assumptions and notation introduced where needed. Omit a standalone preliminaries section if explanations fit locally.
3. **Method or theoretical argument:** one substantive design/result at a time; explain why needed, what it does, and how it connects. Use exact original result numbers and one plain-language sentence on meaning. Explain non-obvious conditions and what fails without them.
4. **Experiments and analysis:** what each experiment tests, data/baselines/metrics/settings, results, ablations and supplementary experiments. Explain which claims the evidence supports.
5. **Full derivations and implementation details:** keep complete substantive proofs, important omitted steps and explanatory code in collapsible blocks beside the relevant main-note argument. Put full experimental hyperparameters and extra result tables in the experiment note when one exists. Preserve the details rather than omitting them to shorten the main note.
6. **Assessment and open questions:** author-stated limitations, source-supported additional assessment and unresolved questions, attributed separately. Leave the personal area for the user.
7. **Lookup and relations:** result/component and notation tables, genuine links to existing notes, version differences, issue/check records and reference roles. This section introduces no new claims.

Theory papers emphasize theorem dependencies and complete proofs. Method/system papers emphasize pipeline, component decisions, implementation and evaluation. Remove inapplicable scaffold headings rather than filling them with boilerplate.

## Mathematics

- Preserve notation and original numbering. Explain symbols, domains/dimensions, assumptions, whether the relation is exact/approximate/an upper bound, and its purpose.
- Use ordinary MathJax-compatible expressions with `$...$` and `$$...$$`. Define needed notation explicitly; do not copy paper-specific LaTeX macros without expansion.
- Give each important result/equation a stable block ID such as `^paper-eq-6` or a unique heading. Link later discussion to it. New derivations have a separate label; do not impersonate original equations.
- Fill nontrivial omitted steps and identify their justification. Standard algebra may be written directly. A proof already stated elsewhere gets a link rather than a repeated theorem box.
- If the same symbol has different meanings, distinguish them and document the change.
- Original numerical values retain their precision. Computed examples have an executed independent script in the paper's checks directory, with reproducible inputs and seed where relevant. Do not present unexecuted output as observed.
- Toy examples are optional. Use a small example for an abstract quantity or counterintuitive mechanism; reuse its setup and keep example material sparse. Prefer a pipeline diagram for an ordinary computational pipeline.
- Check central identities on small instances when feasible, but distinguish this from proof. A verified counterexample can disprove a universal claim; passing instances cannot prove one.

## Figures, tables and experiments

Use the original figure asset when possible, otherwise a verified PDF crop. Inspect labels, legends and caption context. Add a brief Chinese explanation of what to look at. A simplified redraw supplements the original and is labeled as the note writer's diagram.

Retype numerical tables and algorithms as text. Preserve all results, units and precision; a long experimental table may move to `实验分析.md`. Compare transcribed cells with the source, not merely the total set of numbers. Extracted text may lose column order, minus signs or superscripts: verify against the rendered PDF.

For each experiment ask what it tests, whether comparisons use matching conditions, and what the result establishes. Record optimizer, learning rate, batch size, epochs, data processing, hardware and evaluation configuration where reported. Separate percentage-point changes from relative percentage gains. Report missing settings as unreported, not inferred.

## Code next to the method

Verify that the repository is the authors' implementation; record a fixed commit. Third-party implementations can be included when useful but must be labeled.

Read loss functions, core modules, training/inference and evaluation code relevant to the contribution. Select short excerpts with Chinese comments on inputs, tensor shapes, variables and the operation's role. Position them next to the corresponding equation/algorithm; collapse long snippets.

Every snippet identifies:

- Repository, commit, relative file path and verified line range/permalink.
- Corresponding paper result/equation/module.
- Whether it is an annotated original excerpt, a simplified adaptation or explanatory pseudocode.
- Omitted branches/context and whether it has been executed.

Retain actual logic in original excerpts. Label simplifications and independently written pseudocode clearly. Link helpers instead of pretending incomplete fragments are standalone runnable programs. Respect license/attribution terms. Do not execute downloaded code, install dependencies or launch training merely to understand a snippet. Write independent tiny numerical checks when useful.

Distinguish an implementation detail from a genuine paper/code discrepancy; record the exact code and paper versions. A current repository may implement a later revision.

## Source discipline and issues

Use the actual paper version as primary evidence, with author code/configuration for implementation claims. External explanations are supplemental and attributed. Check an external theorem at its original source if a proof depends on its exact form.

Provide reliable sections, theorem/equation/figure/table IDs, or verified PDF page locations for substantive claims. Never reverse-generate an English quote from a Chinese summary. Quote only actual source text. Verify PDF index versus printed page mapping before adding a page-specific Zotero URI.

Before calling an error, check assumptions, symbol reuse, version differences and whether a missing proof step suffices to repair the argument. Record location, issue, candidate correction, verification and impact. Preserve unresolved doubts as questions. Keep unfavorable results and conditions affecting interpretation. A partial review is not a guarantee of correctness.

Use only existing, materially related notes, giving the specific relation. Group peripheral references by purpose; identify individually the results, methods, data and code this paper actually uses. New concept notes or cross-paper syntheses are separate work unless requested.
