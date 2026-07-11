# Per-file audit: `src/x86decomp/pe.py`

## A. File Identity

- **Inventory ID:** `F0394`
- **Relative path:** `src/x86decomp/pe.py`
- **SHA-256:** `ef9ab01d711a61c9dede6021b860ca005fe371f0c56caea8bc6da00782ba24a6`
- **File size:** 22929 bytes
- **Language/format:** Python source
- **Classification:** First-party source code
- **Apparent responsibility:** Architecture-dispatching PE parser with PE32+ x86-64 support.
- **Provenance:** First-party or repository-maintained text
- **Review applicability:** Complete-content text/source review
- **Related files / static consumers:** `src/x86decomp/__init__.py`, `src/x86decomp/cli.py`, `src/x86decomp/convergence.py`, `src/x86decomp/exe_diff.py`, `src/x86decomp/image_match.py`, `src/x86decomp/linker_layout.py`, `src/x86decomp/linker_reconstruction.py`, `src/x86decomp/msvc_metadata.py`
- **Key imports/dependencies:** `.errors`, `.pe32`, `.util`, `__future__`, `dataclasses`, `pathlib`, `struct`, `typing`

## B. Functional Summary

Architecture-dispatching PE parser with PE32+ x86-64 support. Major symbols: TLS64Info, RuntimeFunction, PE64Image, parse_pe64, inspect_pe_kind, parse_pe, TLS64Info.to_dict, RuntimeFunction.to_dict, PE64Image.entry_va, PE64Image.to_dict, _parse_delay_imports64.to_rva. No side-effect-relevant call matched the audit scanner’s rule set.

- **Inputs:** Python arguments, project files, structured records, or external-tool outputs as indicated by the symbols and call sites.
- **Outputs:** Return values, written artifacts, process output, or database state as indicated by the implementation.
- **Side effects / external interactions:** 0 scanner-identified relevant call(s); see Section H for the bounded interpretation.
- **Verified versus inferred:** File bytes, structure, hashes, syntax/format validity, symbols, and logged executions are verified. Purpose statements not established by execution are labeled apparent or inferred.

## C. Correctness Review

Python parsed successfully with the standard-library AST parser.

Boundary conditions, malformed input, error propagation, resource cleanup, path handling, encoding, integer/size limits, and partial-operation behavior were assessed where applicable. Findings are listed in Section L; where no finding is listed, the audit did not establish a defect rather than proving none exists.

## D. Documentation and Docstring Review

Module docstring present: yes. Documented definitions: 16/16. No docstring matched the five generic-pattern families used by the expanded audit.

Documentation was judged proportionally: public/non-obvious behavior requires specific contracts, while trivial fixtures and data files do not require artificial prose.

## E. Code Quality and Maintainability

Highest structural complexity: parse_pe64 (branches=13, AST nodes=883), PE64Image.to_dict (branches=9, AST nodes=316), _parse_delay_imports64 (branches=8, AST nodes=344), _parse_imports64 (branches=7, AST nodes=274), inspect_pe_kind (branches=4, AST nodes=145). 11 line(s) exceed 140 characters; this is a maintainability signal, not by itself a defect.

Broad exception handlers recorded by the scanner: 0. Global/nonlocal declarations: 0. Pass statements: 0. Each was treated as a review lead, not automatically as a defect.

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

Static search found direct symbol references in tests: PE64Image(2), RuntimeFunction(1), TLS64Info(3), entry_va(3), inspect_pe_kind(1), parse_pe(8), parse_pe64(1), to_dict(104). The exact 258-test inventory passed; this is evidence of use, not a line-coverage claim.

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
- **Test confidence:** Static search found direct symbol references in tests: PE64Image(2), RuntimeFunction(1), TLS64Info(3), entry_va(3), inspect_pe_kind(1), parse_pe(8), parse_pe64(1), to_dict(104). The exact 258-test inventory passed; this is evidence of use, not a line-coverage claim.
- **Security assessment:** No unqualified security guarantee; file-specific risk evidence is described above.
- **Recommended priority:** Routine
- **Open questions:** None specific; untested behavior remains subject to normal verification.
- **Related follow-up:** Cross-file architecture, documentation, and duplication reports.
- **Final audit status:** **Audited — complete**
