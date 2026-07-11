# Per-file audit: `src/x86decomp/pe32.py`

## A. File Identity

- **Inventory ID:** `F0395`
- **Relative path:** `src/x86decomp/pe32.py`
- **SHA-256:** `9b9e3b948c92f68bfa352544f7117329d4d3baaaecc0f25d0cc87ffda35b3fbb`
- **File size:** 45678 bytes
- **Language/format:** Python source
- **Classification:** First-party source code
- **Apparent responsibility:** Strict, dependency-free parser for native x86 PE32 images.
- **Provenance:** First-party or repository-maintained text
- **Review applicability:** Complete-content text/source review
- **Related files / static consumers:** `src/x86decomp/__init__.py`, `src/x86decomp/msvc_metadata.py`, `src/x86decomp/pe.py`, `test-suite/src/x86decomp_testkit/toolkit_tests/test_public_api_contract.py`, `tests/test_pe32.py`
- **Key imports/dependencies:** `.binary_reader`, `.errors`, `.util`, `__future__`, `dataclasses`, `pathlib`, `struct`, `typing`

## B. Functional Summary

Strict, dependency-free parser for native x86 PE32 images. Major symbols: DataDirectory, Section, ImportSymbol, ImportLibrary, ExportSymbol, BaseRelocation, DebugRecord, TLSInfo, ResourceLeaf, DelayImportLibrary, LoadConfigInfo, PE32Image. No side-effect-relevant call matched the audit scanner’s rule set.

- **Inputs:** Python arguments, project files, structured records, or external-tool outputs as indicated by the symbols and call sites.
- **Outputs:** Return values, written artifacts, process output, or database state as indicated by the implementation.
- **Side effects / external interactions:** 0 scanner-identified relevant call(s); see Section H for the bounded interpretation.
- **Verified versus inferred:** File bytes, structure, hashes, syntax/format validity, symbols, and logged executions are verified. Purpose statements not established by execution are labeled apparent or inferred.

## C. Correctness Review

Python parsed successfully with the standard-library AST parser.

Boundary conditions, malformed input, error propagation, resource cleanup, path handling, encoding, integer/size limits, and partial-operation behavior were assessed where applicable. Findings are listed in Section L; where no finding is listed, the audit did not establish a defect rather than proving none exists.

## D. Documentation and Docstring Review

Module docstring present: yes. Documented definitions: 42/42. No docstring matched the five generic-pattern families used by the expanded audit.

Documentation was judged proportionally: public/non-obvious behavior requires specific contracts, while trivial fixtures and data files do not require artificial prose.

## E. Code Quality and Maintainability

Highest structural complexity: parse_pe32 (branches=14, AST nodes=995), _parse_debug_records (branches=12, AST nodes=453), _parse_delay_imports (branches=10, AST nodes=371), _parse_relocations (branches=10, AST nodes=294), _parse_exports (branches=9, AST nodes=453).

Broad exception handlers recorded by the scanner: 0. Global/nonlocal declarations: 1. Pass statements: 0. Each was treated as a review lead, not automatically as a defect.

## F. Potential AI-Generated-Code Indicators

Boilerplate/duplication indicator: 3 normalized-AST duplicate group(s); behavioral differences and context are documented in the cross-file matrix.

No claim about authorship is made without provenance evidence. Alternative explanations include manual boilerplate, generated consistency work, compatibility layers, or repeated domain contracts.

## G. Optimization and Performance

No confirmed performance problem was established for this file. Optimization should be driven by profiling or demonstrated scale limits.

Confirmed performance defects require measured impact; no micro-optimization recommendation is made solely from line count or syntax shape.

## H. Security and Robustness

No call matched the targeted process/network/database/file-write risk scanner; this is not a proof of security.

Targeted checks included subprocess shell use, path/archive handling, database calls, network calls, deserialization-adjacent behavior, file writes, resource limits, and malformed-input behavior where relevant. Suspicious binaries were not executed.

## I. Testing Review

Static search found direct symbol references in tests: BaseRelocation(1), DataDirectory(1), DebugRecord(1), DelayImportLibrary(3), ExportSymbol(3), ImportLibrary(3), ImportSymbol(3), LoadConfigInfo(3), PE32Image(2), ResourceLeaf(3). The exact 258-test inventory passed; this is evidence of use, not a line-coverage claim.

The exact non-duplicated inventory executed 258 tests in 86 reconciled partitions with zero failures, errors, or skips. The packaged duplicate self-test tree executed separately with 21 passes. A passing suite does not establish exhaustive semantic correctness.

## J. Missing Elements

No addition was recommended solely to increase complexity. Any unverified behavior is stated in the testing and verdict sections.

## K. Redundancy and Consolidation Opportunities

Normalized-AST duplicate group 13: src/x86decomp/pe.py:TLS64Info.to_dict, src/x86decomp/pe32.py:TLSInfo.to_dict. Consolidation safety is assessed in CROSS_FILE_ANALYSIS.md. Normalized-AST duplicate group 14: src/x86decomp/pe.py:PE64Image.entry_va, src/x86decomp/pe32.py:PE32Image.entry_va. Consolidation safety is assessed in CROSS_FILE_ANALYSIS.md. Normalized-AST duplicate group 15: src/x86decomp/pe.py:_parse_delay_imports64.to_rva, src/x86decomp/pe32.py:_parse_delay_imports.to_rva. Consolidation safety is assessed in CROSS_FILE_ANALYSIS.md.

## L. File-Level Findings

| Finding ID | Severity | Confidence | Symbol or line range | Summary | Evidence | Impact | Recommendation | Verification status |
|---|---|---|---|---|---|---|---|---|
| — | — | — | — | No file-specific finding was raised. | Complete-content and cross-file checks found no issue meeting the findings threshold. | — | — | Verified review status only; absence of a finding is not proof of defect absence. |

## M. File-Level Verdict

- **Overall quality:** No material file-specific issue was verified.
- **Documentation quality:** Proportionate to file type, subject to repository-wide documentation findings.
- **Correctness confidence:** Moderate; complete static review plus repository tests, without exhaustive state-space proof.
- **Maintainability assessment:** No file-specific maintainability finding beyond cross-repository observations.
- **Test confidence:** Static search found direct symbol references in tests: BaseRelocation(1), DataDirectory(1), DebugRecord(1), DelayImportLibrary(3), ExportSymbol(3), ImportLibrary(3), ImportSymbol(3), LoadConfigInfo(3), PE32Image(2), ResourceLeaf(3). The exact 258-test inventory passed; this is evidence of use, not a line-coverage claim.
- **Security assessment:** No unqualified security guarantee; file-specific risk evidence is described above.
- **Recommended priority:** Routine
- **Open questions:** None specific; untested behavior remains subject to normal verification.
- **Related follow-up:** Cross-file architecture, documentation, and duplication reports.
- **Final audit status:** **Audited — complete**
