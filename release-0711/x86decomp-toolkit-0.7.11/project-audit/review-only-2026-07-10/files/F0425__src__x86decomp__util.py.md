# Per-file audit: `src/x86decomp/util.py`

## A. File Identity

- **Inventory ID:** `F0425`
- **Relative path:** `src/x86decomp/util.py`
- **SHA-256:** `297c345484d2d0149c886388d244baee0e06227976f7868070464107042f4fa4`
- **File size:** 3711 bytes
- **Language/format:** Python source
- **Classification:** First-party source code
- **Apparent responsibility:** Compatibility utilities backed by the toolkit's canonical contract primitives.
- **Provenance:** First-party or repository-maintained text
- **Review applicability:** Complete-content text/source review
- **Related files / static consumers:** `src/x86decomp/abi.py`, `src/x86decomp/analysis_db.py`, `src/x86decomp/angr_backend.py`, `src/x86decomp/artifacts.py`, `src/x86decomp/benchmarks.py`, `src/x86decomp/cli.py`, `src/x86decomp/coff.py`, `src/x86decomp/coff_archive.py`
- **Key imports/dependencies:** `.contracts`, `.errors`, `__future__`, `os`, `pathlib`, `shutil`, `tempfile`, `typing`

## B. Functional Summary

Compatibility utilities backed by the toolkit's canonical contract primitives. Major symbols: utc_now, sha256_bytes, sha256_file, canonical_json_bytes, load_json, atomic_write_bytes, atomic_write_text, write_json, copy_file_atomic, ensure_relative_path, require_mapping, require_string. Static analysis recorded 1 filesystem, process, database, network, or other side-effect-relevant call(s).

- **Inputs:** Python arguments, project files, structured records, or external-tool outputs as indicated by the symbols and call sites.
- **Outputs:** Return values, written artifacts, process output, or database state as indicated by the implementation.
- **Side effects / external interactions:** 1 scanner-identified relevant call(s); see Section H for the bounded interpretation.
- **Verified versus inferred:** File bytes, structure, hashes, syntax/format validity, symbols, and logged executions are verified. Purpose statements not established by execution are labeled apparent or inferred.

## C. Correctness Review

Python parsed successfully with the standard-library AST parser. Side-effect/trust-sensitive calls reviewed: destination.parent.mkdir×1.

Boundary conditions, malformed input, error propagation, resource cleanup, path handling, encoding, integer/size limits, and partial-operation behavior were assessed where applicable. Findings are listed in Section L; where no finding is listed, the audit did not establish a defect rather than proving none exists.

## D. Documentation and Docstring Review

Module docstring present: yes. Documented definitions: 13/13. No docstring matched the five generic-pattern families used by the expanded audit.

Documentation was judged proportionally: public/non-obvious behavior requires specific contracts, while trivial fixtures and data files do not require artificial prose.

## E. Code Quality and Maintainability

Highest structural complexity: require_int (branches=4, AST nodes=94), require_string (branches=3, AST nodes=76), copy_file_atomic (branches=1, AST nodes=90), require_mapping (branches=1, AST nodes=42), sha256_file (branches=0, AST nodes=25).

Broad exception handlers recorded by the scanner: 0. Global/nonlocal declarations: 0. Pass statements: 0. Each was treated as a review lead, not automatically as a defect.

## F. Potential AI-Generated-Code Indicators

No file-specific AI-like quality indicator was raised. The audit makes no authorship attribution.

No claim about authorship is made without provenance evidence. Alternative explanations include manual boilerplate, generated consistency work, compatibility layers, or repeated domain contracts.

## G. Optimization and Performance

No confirmed performance problem was established for this file. Optimization should be driven by profiling or demonstrated scale limits.

Confirmed performance defects require measured impact; no micro-optimization recommendation is made solely from line count or syntax shape.

## H. Security and Robustness

1 trust-sensitive/side-effect call(s) were inspected. shell=True findings: 0.

Targeted checks included subprocess shell use, path/archive handling, database calls, network calls, deserialization-adjacent behavior, file writes, resource limits, and malformed-input behavior where relevant. Suspicious binaries were not executed.

## I. Testing Review

Static search found direct symbol references in tests: atomic_write_bytes(4), atomic_write_text(1), canonical_json_bytes(1), copy_file_atomic(1), ensure_relative_path(2), load_json(7), require_int(3), require_mapping(3), require_string(3), sha256_bytes(2). The exact 258-test inventory passed; this is evidence of use, not a line-coverage claim.

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
- **Test confidence:** Static search found direct symbol references in tests: atomic_write_bytes(4), atomic_write_text(1), canonical_json_bytes(1), copy_file_atomic(1), ensure_relative_path(2), load_json(7), require_int(3), require_mapping(3), require_string(3), sha256_bytes(2). The exact 258-test inventory passed; this is evidence of use, not a line-coverage claim.
- **Security assessment:** No unqualified security guarantee; file-specific risk evidence is described above.
- **Recommended priority:** Routine
- **Open questions:** None specific; untested behavior remains subject to normal verification.
- **Related follow-up:** Cross-file architecture, documentation, and duplication reports.
- **Final audit status:** **Audited — complete**
