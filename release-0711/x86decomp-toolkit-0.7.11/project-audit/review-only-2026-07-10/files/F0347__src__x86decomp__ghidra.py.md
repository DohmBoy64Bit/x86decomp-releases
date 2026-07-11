# Per-file audit: `src/x86decomp/ghidra.py`

## A. File Identity

- **Inventory ID:** `F0347`
- **Relative path:** `src/x86decomp/ghidra.py`
- **SHA-256:** `ea266fe809d4d14f1e3171b1c8884c87acc22aa98c4655c2f70907a742a1b60d`
- **File size:** 3688 bytes
- **Language/format:** Python source
- **Classification:** First-party source code
- **Apparent responsibility:** Safe command construction for Ghidra headless analysis.
- **Provenance:** First-party or repository-maintained text
- **Review applicability:** Complete-content text/source review
- **Related files / static consumers:** `src/x86decomp/cli.py`, `test-suite/src/x86decomp_testkit/toolkit_tests/test_public_api_contract.py`, `tests/test_ghidra.py`
- **Key imports/dependencies:** `.errors`, `.tools`, `.util`, `__future__`, `pathlib`, `subprocess`, `typing`

## B. Functional Summary

Safe command construction for Ghidra headless analysis. Major symbols: build_export_command, run_export. Static analysis recorded 3 filesystem, process, database, network, or other side-effect-relevant call(s).

- **Inputs:** Python arguments, project files, structured records, or external-tool outputs as indicated by the symbols and call sites.
- **Outputs:** Return values, written artifacts, process output, or database state as indicated by the implementation.
- **Side effects / external interactions:** 3 scanner-identified relevant call(s); see Section H for the bounded interpretation.
- **Verified versus inferred:** File bytes, structure, hashes, syntax/format validity, symbols, and logged executions are verified. Purpose statements not established by execution are labeled apparent or inferred.

## C. Correctness Review

Python parsed successfully with the standard-library AST parser. Side-effect/trust-sensitive calls reviewed: ghidra_project_dir.mkdir×1, output_dir.mkdir×1, subprocess.run×1.

Boundary conditions, malformed input, error propagation, resource cleanup, path handling, encoding, integer/size limits, and partial-operation behavior were assessed where applicable. Findings are listed in Section L; where no finding is listed, the audit did not establish a defect rather than proving none exists.

## D. Documentation and Docstring Review

Module docstring present: yes. Documented definitions: 2/2. No docstring matched the five generic-pattern families used by the expanded audit.

Documentation was judged proportionally: public/non-obvious behavior requires specific contracts, while trivial fixtures and data files do not require artificial prose.

## E. Code Quality and Maintainability

Highest structural complexity: build_export_command (branches=9, AST nodes=251), run_export (branches=6, AST nodes=225).

Broad exception handlers recorded by the scanner: 0. Global/nonlocal declarations: 0. Pass statements: 0. Each was treated as a review lead, not automatically as a defect.

## F. Potential AI-Generated-Code Indicators

No file-specific AI-like quality indicator was raised. The audit makes no authorship attribution.

No claim about authorship is made without provenance evidence. Alternative explanations include manual boilerplate, generated consistency work, compatibility layers, or repeated domain contracts.

## G. Optimization and Performance

No confirmed performance problem was established for this file. Optimization should be driven by profiling or demonstrated scale limits.

Confirmed performance defects require measured impact; no micro-optimization recommendation is made solely from line count or syntax shape.

## H. Security and Robustness

3 trust-sensitive/side-effect call(s) were inspected. shell=True findings: 0.

Targeted checks included subprocess shell use, path/archive handling, database calls, network calls, deserialization-adjacent behavior, file writes, resource limits, and malformed-input behavior where relevant. Suspicious binaries were not executed.

## I. Testing Review

Static search found direct symbol references in tests: build_export_command(3), run_export(3). The exact 258-test inventory passed; this is evidence of use, not a line-coverage claim.

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
- **Test confidence:** Static search found direct symbol references in tests: build_export_command(3), run_export(3). The exact 258-test inventory passed; this is evidence of use, not a line-coverage claim.
- **Security assessment:** No unqualified security guarantee; file-specific risk evidence is described above.
- **Recommended priority:** Routine
- **Open questions:** None specific; untested behavior remains subject to normal verification.
- **Related follow-up:** Cross-file architecture, documentation, and duplication reports.
- **Final audit status:** **Audited — complete**
