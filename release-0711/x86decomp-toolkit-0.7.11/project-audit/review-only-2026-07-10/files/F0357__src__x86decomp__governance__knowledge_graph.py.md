# Per-file audit: `src/x86decomp/governance/knowledge_graph.py`

## A. File Identity

- **Inventory ID:** `F0357`
- **Relative path:** `src/x86decomp/governance/knowledge_graph.py`
- **SHA-256:** `f3650b738f42a860011c51c2e24bfd31ac4d59e72643518cd65c7d975eb09e58`
- **File size:** 5822 bytes
- **Language/format:** Python source
- **Classification:** First-party source code
- **Apparent responsibility:** Provide the current runtime implementation for the `x86decomp.governance.knowledge_graph` module.
- **Provenance:** First-party or repository-maintained text
- **Review applicability:** Complete-content text/source review
- **Related files / static consumers:** `src/x86decomp/governance/cli.py`, `tests/governance/test_core.py`
- **Key imports/dependencies:** `.store`, `__future__`, `collections`, `json`, `typing`, `x86decomp.contracts`

## B. Functional Summary

Provide the current runtime implementation for the `x86decomp.governance.knowledge_graph` module. Major symbols: KnowledgeGraph, KnowledgeGraph.upsert_node, KnowledgeGraph.add_edge, KnowledgeGraph.get_node, KnowledgeGraph.impact. Static analysis recorded 6 filesystem, process, database, network, or other side-effect-relevant call(s).

- **Inputs:** Python arguments, project files, structured records, or external-tool outputs as indicated by the symbols and call sites.
- **Outputs:** Return values, written artifacts, process output, or database state as indicated by the implementation.
- **Side effects / external interactions:** 6 scanner-identified relevant call(s); see Section H for the bounded interpretation.
- **Verified versus inferred:** File bytes, structure, hashes, syntax/format validity, symbols, and logged executions are verified. Purpose statements not established by execution are labeled apparent or inferred.

## C. Correctness Review

Python parsed successfully with the standard-library AST parser. Side-effect/trust-sensitive calls reviewed: connection.execute×6.

Boundary conditions, malformed input, error propagation, resource cleanup, path handling, encoding, integer/size limits, and partial-operation behavior were assessed where applicable. Findings are listed in Section L; where no finding is listed, the audit did not establish a defect rather than proving none exists.

## D. Documentation and Docstring Review

Module docstring present: yes. Documented definitions: 6/6. 4 generic low-information docstring pattern hit(s) are enumerated in evidence/generic-docstrings.json and tracked by DOC-001.

Documentation was judged proportionally: public/non-obvious behavior requires specific contracts, while trivial fixtures and data files do not require artificial prose.

## E. Code Quality and Maintainability

Highest structural complexity: KnowledgeGraph.impact (branches=13, AST nodes=423), KnowledgeGraph.add_edge (branches=6, AST nodes=238), KnowledgeGraph.upsert_node (branches=4, AST nodes=148), KnowledgeGraph.get_node (branches=1, AST nodes=84), KnowledgeGraph.__init__ (branches=0, AST nodes=23). 7 line(s) exceed 140 characters; this is a maintainability signal, not by itself a defect.

Broad exception handlers recorded by the scanner: 0. Global/nonlocal declarations: 0. Pass statements: 0. Each was treated as a review lead, not automatically as a defect.

## F. Potential AI-Generated-Code Indicators

Low-authorship-quality indicator: generic docstring wording. This is evidence about text quality only and is not evidence of AI authorship. Boilerplate/duplication indicator: 1 normalized-AST duplicate group(s); behavioral differences and context are documented in the cross-file matrix.

No claim about authorship is made without provenance evidence. Alternative explanations include manual boilerplate, generated consistency work, compatibility layers, or repeated domain contracts.

## G. Optimization and Performance

No confirmed performance problem was established for this file. Optimization should be driven by profiling or demonstrated scale limits.

Confirmed performance defects require measured impact; no micro-optimization recommendation is made solely from line count or syntax shape.

## H. Security and Robustness

6 trust-sensitive/side-effect call(s) were inspected. shell=True findings: 0.

Targeted checks included subprocess shell use, path/archive handling, database calls, network calls, deserialization-adjacent behavior, file writes, resource limits, and malformed-input behavior where relevant. Suspicious binaries were not executed.

## I. Testing Review

Static search found direct symbol references in tests: KnowledgeGraph(7), add_edge(2), get_node(1), impact(7), upsert_node(3). The exact 258-test inventory passed; this is evidence of use, not a line-coverage claim.

The exact non-duplicated inventory executed 258 tests in 86 reconciled partitions with zero failures, errors, or skips. The packaged duplicate self-test tree executed separately with 21 passes. A passing suite does not establish exhaustive semantic correctness.

## J. Missing Elements

Remediation and verification work is defined by: DOC-001.

## K. Redundancy and Consolidation Opportunities

Normalized-AST duplicate group 6: src/x86decomp/governance/campaigns.py:CampaignEngine.__init__, src/x86decomp/governance/consensus.py:ConsensusEngine.__init__, src/x86decomp/governance/hypotheses.py:HypothesisLedger.__init__, src/x86decomp/governance/knowledge_graph.py:KnowledgeGraph.__init__, src/x86decomp/governance/plugins.py:PluginRegistry.__init__, src/x86decomp/governance/proofs.py:ProofLedger.__init__, src/x86decomp/governance/reviews.py:ReviewQueue.__init__, src/x86decomp/governance/workers.py:WorkerRegistry.__init__. Consolidation safety is assessed in CROSS_FILE_ANALYSIS.md.

## L. File-Level Findings

| Finding ID | Severity | Confidence | Symbol or line range | Summary | Evidence | Impact | Recommendation | Verification status |
|---|---|---|---|---|---|---|---|---|
| DOC-001 | Medium | Verified | 364 modules, classes, functions, and methods listed in evidence/generic-docstrings.json | Docstring quality gate passes 364 generic low-information docstrings | A full AST scan inspected 1,853 documented symbols and identified 364 (19.6%) matching five generic forms: 231 “Perform the … operation”, 60 module-level “Provide the current runtime implementation …”, 43 generic constructor statements, 28 “Represent … data and behavior”, and 2 “Run the requested operation”. | API readers receive little information about contracts, side effects, failure modes, or domain purpose; the release gate overstates documentation quality. | Replace generic docstrings with behavior-specific contracts and expand the quality gate using an allowlisted semantic-pattern policy plus reviewable exceptions. | Open |

## M. File-Level Verdict

- **Overall quality:** Material issue(s) require remediation.
- **Documentation quality:** See DOC-001/DOC-002 where applicable.
- **Correctness confidence:** Moderate; complete static review plus repository tests, without exhaustive state-space proof.
- **Maintainability assessment:** No file-specific maintainability finding beyond cross-repository observations.
- **Test confidence:** Static search found direct symbol references in tests: KnowledgeGraph(7), add_edge(2), get_node(1), impact(7), upsert_node(3). The exact 258-test inventory passed; this is evidence of use, not a line-coverage claim.
- **Security assessment:** No unqualified security guarantee; file-specific risk evidence is described above.
- **Recommended priority:** Medium
- **Open questions:** Repeat the full AST scan and manually sample each pattern family after remediation.
- **Related follow-up:** DOC-001
- **Final audit status:** **Audited — complete**
