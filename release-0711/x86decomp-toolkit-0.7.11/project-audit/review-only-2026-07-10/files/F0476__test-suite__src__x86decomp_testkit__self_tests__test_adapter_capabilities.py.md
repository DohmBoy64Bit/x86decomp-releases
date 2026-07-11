# Per-file audit: `test-suite/src/x86decomp_testkit/self_tests/test_adapter_capabilities.py`

## A. File Identity

- **Inventory ID:** `F0476`
- **Relative path:** `test-suite/src/x86decomp_testkit/self_tests/test_adapter_capabilities.py`
- **SHA-256:** `aef940d89f5de3c9395b64b0d0f2b5af1c50ee923f8f81ccd3fa44d86ceca4cc`
- **File size:** 3662 bytes
- **Language/format:** Python source
- **Classification:** Packaged test code
- **Apparent responsibility:** Provide the installed test-suite implementation for the `x86decomp_testkit.self_tests.test_adapter_capabilities` module.
- **Provenance:** First-party or repository-maintained text
- **Review applicability:** Complete-content text/source review
- **Related files / static consumers:** `test-suite/tests/test_adapter_capabilities.py`
- **Key imports/dependencies:** `__future__`, `http.server`, `json`, `pathlib`, `threading`, `x86decomp_testkit.adapters.capabilities`, `x86decomp_testkit.adapters.catalog`, `x86decomp_testkit.adapters.detection`, `x86decomp_testkit.config`, `x86decomp_testkit.models`

## B. Functional Summary

Provide the installed test-suite implementation for the `x86decomp_testkit.self_tests.test_adapter_capabilities` module. Major symbols: test_lm_studio_http_satisfies_openai_capability_without_product_aliasing, test_non_loopback_http_endpoint_requires_network_opt_in, test_loopback_host_classifier_is_strict, _ModelsHandler.do_GET, _ModelsHandler.log_message. No side-effect-relevant call matched the audit scanner’s rule set.

- **Inputs:** Python arguments, project files, structured records, or external-tool outputs as indicated by the symbols and call sites.
- **Outputs:** Return values, written artifacts, process output, or database state as indicated by the implementation.
- **Side effects / external interactions:** 0 scanner-identified relevant call(s); see Section H for the bounded interpretation.
- **Verified versus inferred:** File bytes, structure, hashes, syntax/format validity, symbols, and logged executions are verified. Purpose statements not established by execution are labeled apparent or inferred.

## C. Correctness Review

Python parsed successfully with the standard-library AST parser.

Boundary conditions, malformed input, error propagation, resource cleanup, path handling, encoding, integer/size limits, and partial-operation behavior were assessed where applicable. Findings are listed in Section L; where no finding is listed, the audit did not establish a defect rather than proving none exists.

## D. Documentation and Docstring Review

Module docstring present: yes. Documented definitions: 7/7. 5 generic low-information docstring pattern hit(s) are enumerated in evidence/generic-docstrings.json and tracked by DOC-001.

Documentation was judged proportionally: public/non-obvious behavior requires specific contracts, while trivial fixtures and data files do not require artificial prose.

## E. Code Quality and Maintainability

Highest structural complexity: test_lm_studio_http_satisfies_openai_capability_without_product_aliasing (branches=3, AST nodes=222), _ModelsHandler.do_GET (branches=1, AST nodes=94), test_non_loopback_http_endpoint_requires_network_opt_in (branches=0, AST nodes=38), _config (branches=0, AST nodes=26), test_loopback_host_classifier_is_strict (branches=0, AST nodes=22).

Broad exception handlers recorded by the scanner: 0. Global/nonlocal declarations: 0. Pass statements: 0. Each was treated as a review lead, not automatically as a defect.

## F. Potential AI-Generated-Code Indicators

Low-authorship-quality indicator: generic docstring wording. This is evidence about text quality only and is not evidence of AI authorship. Boilerplate/duplication indicator: 5 normalized-AST duplicate group(s); behavioral differences and context are documented in the cross-file matrix.

No claim about authorship is made without provenance evidence. Alternative explanations include manual boilerplate, generated consistency work, compatibility layers, or repeated domain contracts.

## G. Optimization and Performance

No confirmed performance problem was established for this file. Optimization should be driven by profiling or demonstrated scale limits.

Confirmed performance defects require measured impact; no micro-optimization recommendation is made solely from line count or syntax shape.

## H. Security and Robustness

No call matched the targeted process/network/database/file-write risk scanner; this is not a proof of security.

Targeted checks included subprocess shell use, path/archive handling, database calls, network calls, deserialization-adjacent behavior, file writes, resource limits, and malformed-input behavior where relevant. Suspicious binaries were not executed.

## I. Testing Review

Executed in the separate packaged-self-test replay: 3 test function(s); the 21-test package replay passed.

The exact non-duplicated inventory executed 258 tests in 86 reconciled partitions with zero failures, errors, or skips. The packaged duplicate self-test tree executed separately with 21 passes. A passing suite does not establish exhaustive semantic correctness.

## J. Missing Elements

Remediation and verification work is defined by: DOC-001, TEST-001.

## K. Redundancy and Consolidation Opportunities

This file has a behaviorally equivalent packaged/source test counterpart; see TEST-001. Normalized-AST duplicate group 18: test-suite/src/x86decomp_testkit/self_tests/test_adapter_capabilities.py:_config, test-suite/tests/test_adapter_capabilities.py:_config. Consolidation safety is assessed in CROSS_FILE_ANALYSIS.md. Normalized-AST duplicate group 19: test-suite/src/x86decomp_testkit/self_tests/test_adapter_capabilities.py:test_lm_studio_http_satisfies_openai_capability_without_product_aliasing, test-suite/tests/test_adapter_capabilities.py:test_lm_studio_http_satisfies_openai_capability_without_product_aliasing. Consolidation safety is assessed in CROSS_FILE_ANALYSIS.md. Normalized-AST duplicate group 20: test-suite/src/x86decomp_testkit/self_tests/test_adapter_capabilities.py:test_non_loopback_http_endpoint_requires_network_opt_in, test-suite/tests/test_adapter_capabilities.py:test_non_loopback_http_endpoint_requires_network_opt_in. Consolidation safety is assessed in CROSS_FILE_ANALYSIS.md. Normalized-AST duplicate group 21: test-suite/src/x86decomp_testkit/self_tests/test_adapter_capabilities.py:test_loopback_host_classifier_is_strict, test-suite/tests/test_adapter_capabilities.py:test_loopback_host_classifier_is_strict. Consolidation safety is assessed in CROSS_FILE_ANALYSIS.md. Normalized-AST duplicate group 22: test-suite/src/x86decomp_testkit/self_tests/test_adapter_capabilities.py:_ModelsHandler.do_GET, test-suite/tests/test_adapter_capabilities.py:_ModelsHandler.do_GET. Consolidation safety is assessed in CROSS_FILE_ANALYSIS.md.

## L. File-Level Findings

| Finding ID | Severity | Confidence | Symbol or line range | Summary | Evidence | Impact | Recommendation | Verification status |
|---|---|---|---|---|---|---|---|---|
| DOC-001 | Medium | Verified | 364 modules, classes, functions, and methods listed in evidence/generic-docstrings.json | Docstring quality gate passes 364 generic low-information docstrings | A full AST scan inspected 1,853 documented symbols and identified 364 (19.6%) matching five generic forms: 231 “Perform the … operation”, 60 module-level “Provide the current runtime implementation …”, 43 generic constructor statements, 28 “Represent … data and behavior”, and 2 “Run the requested operation”. | API readers receive little information about contracts, side effects, failure modes, or domain purpose; the release gate overstates documentation quality. | Replace generic docstrings with behavior-specific contracts and expand the quality gate using an allowlisted semantic-pattern policy plus reviewable exceptions. | Open |
| TEST-001 | Low | Verified | Six test-suite/tests ↔ x86decomp_testkit/self_tests file pairs | Six packaged self-test files duplicate source tests without an explicit synchronization gate | Six pairs have different file hashes but identical AST behavior after docstrings are removed. The packaged copies are used when the source test tree is unavailable; the source copies are used in a checkout. | Future fixes may land in only one copy, producing checkout/package behavior differences. | Generate packaged self-tests from one canonical source or add a normalized-AST synchronization gate. | Open |

## M. File-Level Verdict

- **Overall quality:** Material issue(s) require remediation.
- **Documentation quality:** See DOC-001/DOC-002 where applicable.
- **Correctness confidence:** Moderate; complete static review plus repository tests, without exhaustive state-space proof.
- **Maintainability assessment:** Open maintainability or duplication concern.
- **Test confidence:** Executed in the separate packaged-self-test replay: 3 test function(s); the 21-test package replay passed.
- **Security assessment:** No unqualified security guarantee; file-specific risk evidence is described above.
- **Recommended priority:** Medium
- **Open questions:** Repeat the full AST scan and manually sample each pattern family after remediation.; Intentionally perturb one copy and prove the new gate fails.
- **Related follow-up:** DOC-001, TEST-001
- **Final audit status:** **Audited — complete**
