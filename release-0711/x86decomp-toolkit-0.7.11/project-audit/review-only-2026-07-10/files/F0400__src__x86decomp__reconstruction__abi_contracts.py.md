# Per-file audit: `src/x86decomp/reconstruction/abi_contracts.py`

## A. File Identity

- **Inventory ID:** `F0400`
- **Relative path:** `src/x86decomp/reconstruction/abi_contracts.py`
- **SHA-256:** `9a8e4ff2d7065219bcb06e65e0d075d3d0acdda4774bd97f2789b1f209eb2e3d`
- **File size:** 5436 bytes
- **Language/format:** Python source
- **Classification:** First-party source code
- **Apparent responsibility:** Provide the current runtime implementation for the `x86decomp.reconstruction.abi_contracts` module.
- **Provenance:** First-party or repository-maintained text
- **Review applicability:** Complete-content text/source review
- **Related files / static consumers:** `src/x86decomp/reconstruction/cli.py`, `tests/reconstruction/test_provenance_abi_tests.py`
- **Key imports/dependencies:** `.store`, `__future__`, `json`, `pathlib`, `typing`, `x86decomp.contracts`

## B. Functional Summary

Provide the current runtime implementation for the `x86decomp.reconstruction.abi_contracts` module. Major symbols: ABIContracts, ABIContracts.recover, ABIContracts.get, ABIContracts.verify, ABIContracts.compare, ABIContracts.export, ABIContracts.shim. Static analysis recorded 8 filesystem, process, database, network, or other side-effect-relevant call(s).

- **Inputs:** Python arguments, project files, structured records, or external-tool outputs as indicated by the symbols and call sites.
- **Outputs:** Return values, written artifacts, process output, or database state as indicated by the implementation.
- **Side effects / external interactions:** 8 scanner-identified relevant call(s); see Section H for the bounded interpretation.
- **Verified versus inferred:** File bytes, structure, hashes, syntax/format validity, symbols, and logged executions are verified. Purpose statements not established by execution are labeled apparent or inferred.

## C. Correctness Review

Python parsed successfully with the standard-library AST parser. Side-effect/trust-sensitive calls reviewed: c.execute×6, out.parent.mkdir×1, out.write_text×1.

Boundary conditions, malformed input, error propagation, resource cleanup, path handling, encoding, integer/size limits, and partial-operation behavior were assessed where applicable. Findings are listed in Section L; where no finding is listed, the audit did not establish a defect rather than proving none exists.

## D. Documentation and Docstring Review

Module docstring present: yes. Documented definitions: 8/8. 4 generic low-information docstring pattern hit(s) are enumerated in evidence/generic-docstrings.json and tracked by DOC-001.

Documentation was judged proportionally: public/non-obvious behavior requires specific contracts, while trivial fixtures and data files do not require artificial prose.

## E. Code Quality and Maintainability

Highest structural complexity: ABIContracts.recover (branches=5, AST nodes=281), ABIContracts.verify (branches=1, AST nodes=166), ABIContracts.shim (branches=1, AST nodes=164), ABIContracts.compare (branches=1, AST nodes=153), ABIContracts.get (branches=1, AST nodes=68). 16 line(s) exceed 140 characters; this is a maintainability signal, not by itself a defect.

Broad exception handlers recorded by the scanner: 0. Global/nonlocal declarations: 0. Pass statements: 0. Each was treated as a review lead, not automatically as a defect.

## F. Potential AI-Generated-Code Indicators

Low-authorship-quality indicator: generic docstring wording. This is evidence about text quality only and is not evidence of AI authorship. Boilerplate/duplication indicator: 1 normalized-AST duplicate group(s); behavioral differences and context are documented in the cross-file matrix.

No claim about authorship is made without provenance evidence. Alternative explanations include manual boilerplate, generated consistency work, compatibility layers, or repeated domain contracts.

## G. Optimization and Performance

No confirmed performance problem was established for this file. Optimization should be driven by profiling or demonstrated scale limits.

Confirmed performance defects require measured impact; no micro-optimization recommendation is made solely from line count or syntax shape.

## H. Security and Robustness

8 trust-sensitive/side-effect call(s) were inspected. shell=True findings: 0.

Targeted checks included subprocess shell use, path/archive handling, database calls, network calls, deserialization-adjacent behavior, file writes, resource limits, and malformed-input behavior where relevant. Suspicious binaries were not executed.

## I. Testing Review

Static search found direct symbol references in tests: ABIContracts(9), compare(15), export(33), get(100), recover(12), shim(9), verify(45). The exact 258-test inventory passed; this is evidence of use, not a line-coverage claim.

The exact non-duplicated inventory executed 258 tests in 86 reconciled partitions with zero failures, errors, or skips. The packaged duplicate self-test tree executed separately with 21 passes. A passing suite does not establish exhaustive semantic correctness.

## J. Missing Elements

Remediation and verification work is defined by: DOC-001.

## K. Redundancy and Consolidation Opportunities

Normalized-AST duplicate group 16: src/x86decomp/reconstruction/abi_contracts.py:ABIContracts.__init__, src/x86decomp/reconstruction/builds.py:BuildManager.__init__, src/x86decomp/reconstruction/capsules.py:Capsules.__init__, src/x86decomp/reconstruction/generated_tests.py:GeneratedTests.__init__, src/x86decomp/reconstruction/headers.py:HeaderManager.__init__, src/x86decomp/reconstruction/libraries.py:LibraryRecognition.__init__, src/x86decomp/reconstruction/project_layout.py:ProjectLayout.__init__, src/x86decomp/reconstruction/provenance.py:ProvenanceLedger.__init__, src/x86decomp/reconstruction/security.py:SecurityReview.__init__, src/x86decomp/reconstruction/semantic_changesets.py:SemanticChangeSets.__init__. Consolidation safety is assessed in CROSS_FILE_ANALYSIS.md.

## L. File-Level Findings

| Finding ID | Severity | Confidence | Symbol or line range | Summary | Evidence | Impact | Recommendation | Verification status |
|---|---|---|---|---|---|---|---|---|
| DOC-001 | Medium | Verified | 364 modules, classes, functions, and methods listed in evidence/generic-docstrings.json | Docstring quality gate passes 364 generic low-information docstrings | A full AST scan inspected 1,853 documented symbols and identified 364 (19.6%) matching five generic forms: 231 “Perform the … operation”, 60 module-level “Provide the current runtime implementation …”, 43 generic constructor statements, 28 “Represent … data and behavior”, and 2 “Run the requested operation”. | API readers receive little information about contracts, side effects, failure modes, or domain purpose; the release gate overstates documentation quality. | Replace generic docstrings with behavior-specific contracts and expand the quality gate using an allowlisted semantic-pattern policy plus reviewable exceptions. | Open |

## M. File-Level Verdict

- **Overall quality:** Material issue(s) require remediation.
- **Documentation quality:** See DOC-001/DOC-002 where applicable.
- **Correctness confidence:** Moderate; complete static review plus repository tests, without exhaustive state-space proof.
- **Maintainability assessment:** No file-specific maintainability finding beyond cross-repository observations.
- **Test confidence:** Static search found direct symbol references in tests: ABIContracts(9), compare(15), export(33), get(100), recover(12), shim(9), verify(45). The exact 258-test inventory passed; this is evidence of use, not a line-coverage claim.
- **Security assessment:** No unqualified security guarantee; file-specific risk evidence is described above.
- **Recommended priority:** Medium
- **Open questions:** Repeat the full AST scan and manually sample each pattern family after remediation.
- **Related follow-up:** DOC-001
- **Final audit status:** **Audited — complete**
