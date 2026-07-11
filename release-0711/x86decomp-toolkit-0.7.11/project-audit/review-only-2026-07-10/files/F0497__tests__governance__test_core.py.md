# Per-file audit: `tests/governance/test_core.py`

## A. File Identity

- **Inventory ID:** `F0497`
- **Relative path:** `tests/governance/test_core.py`
- **SHA-256:** `55141cbe8519f2a616967bf67cc86fcf18376fab304ffcbe78d1809deea66f05`
- **File size:** 9827 bytes
- **Language/format:** Python source
- **Classification:** Test code
- **Apparent responsibility:** Executable regression tests for the behavior indicated by the filename and test symbols.
- **Provenance:** First-party or repository-maintained text
- **Review applicability:** Complete-content text/source review
- **Related files / static consumers:** No direct relationship established beyond directory and manifest context.
- **Key imports/dependencies:** `__future__`, `pathlib`, `pytest`, `x86decomp.contracts`, `x86decomp.governance.campaigns`, `x86decomp.governance.candidates`, `x86decomp.governance.consensus`, `x86decomp.governance.counterexamples`, `x86decomp.governance.family`, `x86decomp.governance.hypotheses`, `x86decomp.governance.knowledge_graph`, `x86decomp.governance.reviews`, `x86decomp.governance.store`

## B. Functional Summary

Executable regression tests for the behavior indicated by the filename and test symbols. Major symbols: store, test_store_is_additive_and_audit_chain, test_audit_tamper_detected, test_hypothesis_gate_and_accept, test_hypothesis_contradiction_blocks_acceptance, test_hypothesis_dependency_cycle_rejected, test_campaign_lifecycle_and_planner, test_campaign_budget_blocks, test_campaign_branch, test_candidate_branch_compare_and_promotion, test_candidate_rejects_traversal, test_ddmin_and_counterexample_promotion. Static analysis recorded 10 filesystem, process, database, network, or other side-effect-relevant call(s).

- **Inputs:** Python arguments, project files, structured records, or external-tool outputs as indicated by the symbols and call sites.
- **Outputs:** Return values, written artifacts, process output, or database state as indicated by the implementation.
- **Side effects / external interactions:** 10 scanner-identified relevant call(s); see Section H for the bounded interpretation.
- **Verified versus inferred:** File bytes, structure, hashes, syntax/format validity, symbols, and logged executions are verified. Purpose statements not established by execution are labeled apparent or inferred.

## C. Correctness Review

Python parsed successfully with the standard-library AST parser. Side-effect/trust-sensitive calls reviewed: con.execute×4, source.write_text×2, f.write_text×1, a.write_bytes×1, b.write_bytes×1, f.write_bytes×1.

Boundary conditions, malformed input, error propagation, resource cleanup, path handling, encoding, integer/size limits, and partial-operation behavior were assessed where applicable. Findings are listed in Section L; where no finding is listed, the audit did not establish a defect rather than proving none exists.

## D. Documentation and Docstring Review

Module docstring present: yes. Documented definitions: 18/18. No docstring matched the five generic-pattern families used by the expanded audit.

Documentation was judged proportionally: public/non-obvious behavior requires specific contracts, while trivial fixtures and data files do not require artificial prose.

## E. Code Quality and Maintainability

Highest structural complexity: test_hypothesis_gate_and_accept (branches=2, AST nodes=155), test_ddmin_and_counterexample_promotion (branches=1, AST nodes=125), test_hypothesis_contradiction_blocks_acceptance (branches=1, AST nodes=107), test_family_report_path (branches=1, AST nodes=89), test_graph_impact (branches=1, AST nodes=78). 6 line(s) exceed 140 characters; this is a maintainability signal, not by itself a defect.

Broad exception handlers recorded by the scanner: 0. Global/nonlocal declarations: 0. Pass statements: 0. Each was treated as a review lead, not automatically as a defect.

## F. Potential AI-Generated-Code Indicators

No file-specific AI-like quality indicator was raised. The audit makes no authorship attribution.

No claim about authorship is made without provenance evidence. Alternative explanations include manual boilerplate, generated consistency work, compatibility layers, or repeated domain contracts.

## G. Optimization and Performance

No confirmed performance problem was established for this file. Optimization should be driven by profiling or demonstrated scale limits.

Confirmed performance defects require measured impact; no micro-optimization recommendation is made solely from line count or syntax shape.

## H. Security and Robustness

10 trust-sensitive/side-effect call(s) were inspected. shell=True findings: 0.

Targeted checks included subprocess shell use, path/archive handling, database calls, network calls, deserialization-adjacent behavior, file writes, resource limits, and malformed-input behavior where relevant. Suspicious binaries were not executed.

## I. Testing Review

Executed in the exact inventory: 17 collected test(s), all passing.

The exact non-duplicated inventory executed 258 tests in 86 reconciled partitions with zero failures, errors, or skips. The packaged duplicate self-test tree executed separately with 21 passes. A passing suite does not establish exhaustive semantic correctness.

## J. Missing Elements

No addition was recommended solely to increase complexity. Any unverified behavior is stated in the testing and verdict sections.

## K. Redundancy and Consolidation Opportunities

No exact normalized-function duplicate involving this file was identified by the AST scan.

## L. File-Level Findings

| Finding ID | Severity | Confidence | Symbol or line range | Summary | Evidence | Impact | Recommendation | Verification status |
|---|---|---|---|---|---|---|---|---|
| — | — | — | — | No file-specific finding was raised. | Complete-content and cross-file checks found no issue meeting the findings threshold. | — | — | Verified review status only; absence of a finding is not proof of defect absence. |

## M. File-Level Verdict

- **Overall quality:** No material file-specific issue was verified.
- **Documentation quality:** Proportionate to file type, subject to repository-wide documentation findings.
- **Correctness confidence:** Moderate; complete static review plus repository tests, without exhaustive state-space proof.
- **Maintainability assessment:** No file-specific maintainability finding beyond cross-repository observations.
- **Test confidence:** Executed in the exact inventory: 17 collected test(s), all passing.
- **Security assessment:** No unqualified security guarantee; file-specific risk evidence is described above.
- **Recommended priority:** Routine
- **Open questions:** None specific; untested behavior remains subject to normal verification.
- **Related follow-up:** Cross-file architecture, documentation, and duplication reports.
- **Final audit status:** **Audited — complete**
