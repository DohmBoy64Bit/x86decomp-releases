# Per-file audit: `scripts/source_hashes.py`

## A. File Identity

- **Inventory ID:** `F0280`
- **Relative path:** `scripts/source_hashes.py`
- **SHA-256:** `cca3bc735681faf6af2e9491a2b159365572f5ff505edded0f59c85efd5fbc3f`
- **File size:** 11290 bytes
- **Language/format:** Python source
- **Classification:** Build, verification, or automation
- **Apparent responsibility:** Repository python source asset.
- **Provenance:** First-party or repository-maintained text
- **Review applicability:** Complete-content text/source review
- **Related files / static consumers:** No direct relationship established beyond directory and manifest context.
- **Key imports/dependencies:** `__future__`, `argparse`, `hashlib`, `json`, `pathlib`, `tomllib`, `typing`

## B. Functional Summary

Repository python source asset. Major symbols: source_files, all_release_files, manifest_text, write_manifest, all_file_payload, write_all_file_manifest, verify_manifest, verify_all_file_manifest, generate_all, verify_all, main. Static analysis recorded 2 filesystem, process, database, network, or other side-effect-relevant call(s).

- **Inputs:** Python arguments, project files, structured records, or external-tool outputs as indicated by the symbols and call sites.
- **Outputs:** Return values, written artifacts, process output, or database state as indicated by the implementation.
- **Side effects / external interactions:** 2 scanner-identified relevant call(s); see Section H for the bounded interpretation.
- **Verified versus inferred:** File bytes, structure, hashes, syntax/format validity, symbols, and logged executions are verified. Purpose statements not established by execution are labeled apparent or inferred.

## C. Correctness Review

Python parsed successfully with the standard-library AST parser. Side-effect/trust-sensitive calls reviewed: manifest.write_text×2.

Boundary conditions, malformed input, error propagation, resource cleanup, path handling, encoding, integer/size limits, and partial-operation behavior were assessed where applicable. Findings are listed in Section L; where no finding is listed, the audit did not establish a defect rather than proving none exists.

## D. Documentation and Docstring Review

Module docstring present: yes. Documented definitions: 17/17. No docstring matched the five generic-pattern families used by the expanded audit.

Documentation was judged proportionally: public/non-obvious behavior requires specific contracts, while trivial fixtures and data files do not require artificial prose.

## E. Code Quality and Maintainability

Highest structural complexity: verify_all_file_manifest (branches=19, AST nodes=566), verify_manifest (branches=6, AST nodes=241), _read_manifest (branches=6, AST nodes=181), main (branches=2, AST nodes=190), _release_version (branches=2, AST nodes=70).

Broad exception handlers recorded by the scanner: 0. Global/nonlocal declarations: 0. Pass statements: 0. Each was treated as a review lead, not automatically as a defect.

## F. Potential AI-Generated-Code Indicators

No file-specific AI-like quality indicator was raised. The audit makes no authorship attribution.

No claim about authorship is made without provenance evidence. Alternative explanations include manual boilerplate, generated consistency work, compatibility layers, or repeated domain contracts.

## G. Optimization and Performance

No confirmed performance problem was established for this file. Optimization should be driven by profiling or demonstrated scale limits.

Confirmed performance defects require measured impact; no micro-optimization recommendation is made solely from line count or syntax shape.

## H. Security and Robustness

2 trust-sensitive/side-effect call(s) were inspected. shell=True findings: 0.

Targeted checks included subprocess shell use, path/archive handling, database calls, network calls, deserialization-adjacent behavior, file writes, resource limits, and malformed-input behavior where relevant. Suspicious binaries were not executed.

## I. Testing Review

No executable file-specific test relationship applies or was established; repository-wide checks are recorded in RUN_LOG.md.

The exact non-duplicated inventory executed 258 tests in 86 reconciled partitions with zero failures, errors, or skips. The packaged duplicate self-test tree executed separately with 21 passes. A passing suite does not establish exhaustive semantic correctness.

## J. Missing Elements

Remediation and verification work is defined by: REL-001.

## K. Redundancy and Consolidation Opportunities

No exact normalized-function duplicate involving this file was identified by the AST scan.

## L. File-Level Findings

| Finding ID | Severity | Confidence | Symbol or line range | Summary | Evidence | Impact | Recommendation | Verification status |
|---|---|---|---|---|---|---|---|---|
| REL-001 | High | Verified | Makefile verify/docstrings/verify-hashes; audit-docstrings.main; source_hashes.verify_all | Documented verification sequence rewrites sealed reports before hash verification | Makefile line 3 orders docstrings before verify-hashes. scripts/audit-docstrings.py lines 85-86 generate a current timestamp and lines 138-143 overwrite the two root reports by default. A disposable-clone replay changed both report hashes; the immediately following source_hashes.py verify returned exit 2 with exactly those two hash mismatches. | The documented release gate cannot complete against an otherwise pristine release without an intentional manifest regeneration. | Add a check-only mode that writes to a temporary location or compares generated content while excluding volatile timestamps; make verify should use that mode. Keep report regeneration as an explicit release action. | Open |

## M. File-Level Verdict

- **Overall quality:** Material issue(s) require remediation.
- **Documentation quality:** Proportionate to file type, subject to repository-wide documentation findings.
- **Correctness confidence:** Reduced by an open verified finding.
- **Maintainability assessment:** No file-specific maintainability finding beyond cross-repository observations.
- **Test confidence:** No executable file-specific test relationship applies or was established; repository-wide checks are recorded in RUN_LOG.md.
- **Security assessment:** No unqualified security guarantee; file-specific risk evidence is described above.
- **Recommended priority:** High
- **Open questions:** After remediation, run make verify in a fresh extracted archive and prove all original file hashes remain unchanged.
- **Related follow-up:** REL-001
- **Final audit status:** **Audited — complete**
