# Per-file audit: `src/x86decomp/reconstruction/acceleration.py`

## A. File Identity

- **Inventory ID:** `F0401`
- **Relative path:** `src/x86decomp/reconstruction/acceleration.py`
- **SHA-256:** `6754b04bf0b1cd6308637226f9861350ae1d9c92f29e21b2be6f4caab4cc18c9`
- **File size:** 97551 bytes
- **Language/format:** Python source
- **Classification:** First-party source code
- **Apparent responsibility:** Human-readable decompilation acceleration helpers.
- **Provenance:** First-party or repository-maintained text
- **Review applicability:** Complete-content text/source review
- **Related files / static consumers:** `src/x86decomp/reconstruction/cli.py`, `tests/reconstruction/test_decomp_acceleration.py`, `tests/reconstruction/test_real_project_acceleration.py`, `tests/test_audit_fixes.py`
- **Key imports/dependencies:** `__future__`, `json`, `pathlib`, `re`, `shutil`, `typing`, `urllib.error`, `urllib.request`, `x86decomp.artifacts`, `x86decomp.contracts`, `x86decomp.cpp_recovery`, `x86decomp.local_llm.matching`, `x86decomp.local_llm.prompts`, `x86decomp.util`, `x86decomp.workflow`

## B. Functional Summary

Human-readable decompilation acceleration helpers. Major symbols: llm_job_from_function_packet, llm_job_from_range, llm_batch_create, llm_batch_match, candidate_promote, source_map_annotate, source_map_verify, module_assign, module_suggest, type_propagate, header_synthesize_project, vtable_recover. Static analysis recorded 40 filesystem, process, database, network, or other side-effect-relevant call(s).

- **Inputs:** Python arguments, project files, structured records, or external-tool outputs as indicated by the symbols and call sites.
- **Outputs:** Return values, written artifacts, process output, or database state as indicated by the implementation.
- **Side effects / external interactions:** 40 scanner-identified relevant call(s); see Section H for the bounded interpretation.
- **Verified versus inferred:** File bytes, structure, hashes, syntax/format validity, symbols, and logged executions are verified. Purpose statements not established by execution are labeled apparent or inferred.

## C. Correctness Review

Python parsed successfully with the standard-library AST parser. Side-effect/trust-sensitive calls reviewed: output.mkdir×8, path.write_text×5, output.parent.mkdir×4, fid.replace×3, bytes_path.write_bytes×2, asm_path.write_text×2, out.parent.mkdir×2, manifest.parent.mkdir×2, output.write_text×2, urllib.request.urlopen×2, dest.parent.mkdir×1, manifest_path.parent.mkdir×1. 5 broad exception handler(s) were inspected in context; no blanket finding was created without a demonstrated failure path.

Boundary conditions, malformed input, error propagation, resource cleanup, path handling, encoding, integer/size limits, and partial-operation behavior were assessed where applicable. Findings are listed in Section L; where no finding is listed, the audit did not establish a defect rather than proving none exists.

## D. Documentation and Docstring Review

Module docstring present: yes. Documented definitions: 70/70. No docstring matched the five generic-pattern families used by the expanded audit.

Documentation was judged proportionally: public/non-obvious behavior requires specific contracts, while trivial fixtures and data files do not require artificial prose.

## E. Code Quality and Maintainability

Highest structural complexity: image_text_compose (branches=13, AST nodes=579), candidate_promote (branches=13, AST nodes=439), llm_job_from_function_packet (branches=12, AST nodes=556), llm_job_from_range (branches=12, AST nodes=423), function_discover (branches=12, AST nodes=350). 91 line(s) exceed 140 characters; this is a maintainability signal, not by itself a defect.

Broad exception handlers recorded by the scanner: 5. Global/nonlocal declarations: 0. Pass statements: 0. Each was treated as a review lead, not automatically as a defect.

## F. Potential AI-Generated-Code Indicators

No file-specific AI-like quality indicator was raised. The audit makes no authorship attribution.

No claim about authorship is made without provenance evidence. Alternative explanations include manual boilerplate, generated consistency work, compatibility layers, or repeated domain contracts.

## G. Optimization and Performance

No confirmed performance problem was established for this file. Optimization should be driven by profiling or demonstrated scale limits.

Confirmed performance defects require measured impact; no micro-optimization recommendation is made solely from line count or syntax shape.

## H. Security and Robustness

40 trust-sensitive/side-effect call(s) were inspected. shell=True findings: 0.

Targeted checks included subprocess shell use, path/archive handling, database calls, network calls, deserialization-adjacent behavior, file writes, resource limits, and malformed-input behavior where relevant. Suspicious binaries were not executed.

## I. Testing Review

Static search found direct symbol references in tests: asset_inventory(3), candidate_promote(3), candidate_search(3), class_scaffold(1), compiler_compare_flags(3), compiler_rule_learn(3), compiler_rule_report(1), decompiler_cleanup(3), diff_explain(1), function_boundary_reconcile(3). The exact 258-test inventory passed; this is evidence of use, not a line-coverage claim.

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
- **Test confidence:** Static search found direct symbol references in tests: asset_inventory(3), candidate_promote(3), candidate_search(3), class_scaffold(1), compiler_compare_flags(3), compiler_rule_learn(3), compiler_rule_report(1), decompiler_cleanup(3), diff_explain(1), function_boundary_reconcile(3). The exact 258-test inventory passed; this is evidence of use, not a line-coverage claim.
- **Security assessment:** No unqualified security guarantee; file-specific risk evidence is described above.
- **Recommended priority:** Routine
- **Open questions:** None specific; untested behavior remains subject to normal verification.
- **Related follow-up:** Cross-file architecture, documentation, and duplication reports.
- **Final audit status:** **Audited — complete**
