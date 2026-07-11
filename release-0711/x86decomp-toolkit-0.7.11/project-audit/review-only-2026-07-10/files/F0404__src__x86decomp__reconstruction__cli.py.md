# Per-file audit: `src/x86decomp/reconstruction/cli.py`

## A. File Identity

- **Inventory ID:** `F0404`
- **Relative path:** `src/x86decomp/reconstruction/cli.py`
- **SHA-256:** `0b591c69d07287206a84bc9ca1d8ddca3dc69461dff67ad3d6436b1454eff731`
- **File size:** 45198 bytes
- **Language/format:** Python source
- **Classification:** First-party source code
- **Apparent responsibility:** Provide the current runtime implementation for the `x86decomp.reconstruction.cli` module.
- **Provenance:** First-party or repository-maintained text
- **Review applicability:** Complete-content text/source review
- **Related files / static consumers:** `scripts/sync-release-contracts.py`, `src/x86decomp/__main__.py`, `src/x86decomp/canonical.py`, `test-suite/src/x86decomp_testkit/__main__.py`, `test-suite/src/x86decomp_testkit/toolkit_tests/test_public_api_contract.py`, `tests/assembly/test_pipeline_cli_schemas.py`, `tests/governance/test_governance_cli_schemas.py`, `tests/native/test_cli_schemas.py`
- **Key imports/dependencies:** `.abi_contracts`, `.acceleration`, `.builds`, `.capsules`, `.generated_tests`, `.headers`, `.libraries`, `.project_layout`, `.provenance`, `.security`, `.semantic_changesets`, `.store`, `__future__`, `argparse`, `pathlib`, `typing`, `x86decomp.cli_utils`, `x86decomp.contracts`, `x86decomp.local_llm`, `x86decomp.local_llm.profiles`, `x86decomp.util`

## B. Functional Summary

Provide the current runtime implementation for the `x86decomp.reconstruction.cli` module. Major symbols: build_parser, dispatch, main. No side-effect-relevant call matched the audit scanner’s rule set.

- **Inputs:** Python arguments, project files, structured records, or external-tool outputs as indicated by the symbols and call sites.
- **Outputs:** Return values, written artifacts, process output, or database state as indicated by the implementation.
- **Side effects / external interactions:** 0 scanner-identified relevant call(s); see Section H for the bounded interpretation.
- **Verified versus inferred:** File bytes, structure, hashes, syntax/format validity, symbols, and logged executions are verified. Purpose statements not established by execution are labeled apparent or inferred.

## C. Correctness Review

Python parsed successfully with the standard-library AST parser.

Boundary conditions, malformed input, error propagation, resource cleanup, path handling, encoding, integer/size limits, and partial-operation behavior were assessed where applicable. Findings are listed in Section L; where no finding is listed, the audit did not establish a defect rather than proving none exists.

## D. Documentation and Docstring Review

Module docstring present: yes. Documented definitions: 4/4. 1 generic low-information docstring pattern hit(s) are enumerated in evidence/generic-docstrings.json and tracked by DOC-001.

Documentation was judged proportionally: public/non-obvious behavior requires specific contracts, while trivial fixtures and data files do not require artificial prose.

## E. Code Quality and Maintainability

Highest structural complexity: dispatch (branches=135, AST nodes=4698), build_parser (branches=2, AST nodes=4945), main (branches=0, AST nodes=27), _store (branches=0, AST nodes=19). 93 line(s) exceed 140 characters; this is a maintainability signal, not by itself a defect.

Broad exception handlers recorded by the scanner: 0. Global/nonlocal declarations: 0. Pass statements: 0. Each was treated as a review lead, not automatically as a defect.

## F. Potential AI-Generated-Code Indicators

Low-authorship-quality indicator: generic docstring wording. This is evidence about text quality only and is not evidence of AI authorship. Boilerplate/duplication indicator: 1 normalized-AST duplicate group(s); behavioral differences and context are documented in the cross-file matrix.

No claim about authorship is made without provenance evidence. Alternative explanations include manual boilerplate, generated consistency work, compatibility layers, or repeated domain contracts.

## G. Optimization and Performance

dispatch has 135 branch/compound nodes; treat this as a profiling and maintainability target, not a confirmed performance defect.

Confirmed performance defects require measured impact; no micro-optimization recommendation is made solely from line count or syntax shape.

## H. Security and Robustness

No call matched the targeted process/network/database/file-write risk scanner; this is not a proof of security.

Targeted checks included subprocess shell use, path/archive handling, database calls, network calls, deserialization-adjacent behavior, file writes, resource limits, and malformed-input behavior where relevant. Suspicious binaries were not executed.

## I. Testing Review

Static search found direct symbol references in tests: build_parser(19), dispatch(6), main(57). The exact 258-test inventory passed; this is evidence of use, not a line-coverage claim.

The exact non-duplicated inventory executed 258 tests in 86 reconciled partitions with zero failures, errors, or skips. The packaged duplicate self-test tree executed separately with 21 passes. A passing suite does not establish exhaustive semantic correctness.

## J. Missing Elements

Remediation and verification work is defined by: DOC-001.

## K. Redundancy and Consolidation Opportunities

Normalized-AST duplicate group 8: src/x86decomp/governance/cli.py:main, src/x86decomp/reconstruction/cli.py:main. Consolidation safety is assessed in CROSS_FILE_ANALYSIS.md.

## L. File-Level Findings

| Finding ID | Severity | Confidence | Symbol or line range | Summary | Evidence | Impact | Recommendation | Verification status |
|---|---|---|---|---|---|---|---|---|
| DOC-001 | Medium | Verified | 364 modules, classes, functions, and methods listed in evidence/generic-docstrings.json | Docstring quality gate passes 364 generic low-information docstrings | A full AST scan inspected 1,853 documented symbols and identified 364 (19.6%) matching five generic forms: 231 “Perform the … operation”, 60 module-level “Provide the current runtime implementation …”, 43 generic constructor statements, 28 “Represent … data and behavior”, and 2 “Run the requested operation”. | API readers receive little information about contracts, side effects, failure modes, or domain purpose; the release gate overstates documentation quality. | Replace generic docstrings with behavior-specific contracts and expand the quality gate using an allowlisted semantic-pattern policy plus reviewable exceptions. | Open |

## M. File-Level Verdict

- **Overall quality:** Material issue(s) require remediation.
- **Documentation quality:** See DOC-001/DOC-002 where applicable.
- **Correctness confidence:** Moderate; complete static review plus repository tests, without exhaustive state-space proof.
- **Maintainability assessment:** No file-specific maintainability finding beyond cross-repository observations.
- **Test confidence:** Static search found direct symbol references in tests: build_parser(19), dispatch(6), main(57). The exact 258-test inventory passed; this is evidence of use, not a line-coverage claim.
- **Security assessment:** No unqualified security guarantee; file-specific risk evidence is described above.
- **Recommended priority:** Medium
- **Open questions:** Repeat the full AST scan and manually sample each pattern family after remediation.
- **Related follow-up:** DOC-001
- **Final audit status:** **Audited — complete**
