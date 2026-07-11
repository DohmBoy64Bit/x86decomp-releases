# Per-file audit: `test-suite/tests/test_adapter_capabilities.py`

## A. File Identity

- **Inventory ID:** `F0486`
- **Relative path:** `test-suite/tests/test_adapter_capabilities.py`
- **SHA-256:** `47dde51aa511486350597ec6a786e4be9ed9bc229b02e9cd8d12baff0874f133`
- **File size:** 4413 bytes
- **Language/format:** Python source
- **Classification:** Test code
- **Apparent responsibility:** Executable regression tests for the behavior indicated by the filename and test symbols.
- **Provenance:** First-party or repository-maintained text
- **Review applicability:** Complete-content text/source review
- **Related files / static consumers:** `test-suite/src/x86decomp_testkit/self_tests/test_adapter_capabilities.py`
- **Key imports/dependencies:** `__future__`, `http.server`, `json`, `pathlib`, `threading`, `x86decomp_testkit.adapters.capabilities`, `x86decomp_testkit.adapters.catalog`, `x86decomp_testkit.adapters.detection`, `x86decomp_testkit.config`, `x86decomp_testkit.models`

## B. Functional Summary

Executable regression tests for the behavior indicated by the filename and test symbols. Major symbols: test_lm_studio_http_satisfies_openai_capability_without_product_aliasing, test_non_loopback_http_endpoint_requires_network_opt_in, test_loopback_host_classifier_is_strict, _ModelsHandler.do_GET, _ModelsHandler.log_message. No side-effect-relevant call matched the audit scanner’s rule set.

- **Inputs:** Python arguments, project files, structured records, or external-tool outputs as indicated by the symbols and call sites.
- **Outputs:** Return values, written artifacts, process output, or database state as indicated by the implementation.
- **Side effects / external interactions:** 0 scanner-identified relevant call(s); see Section H for the bounded interpretation.
- **Verified versus inferred:** File bytes, structure, hashes, syntax/format validity, symbols, and logged executions are verified. Purpose statements not established by execution are labeled apparent or inferred.

## C. Correctness Review

Python parsed successfully with the standard-library AST parser.

Boundary conditions, malformed input, error propagation, resource cleanup, path handling, encoding, integer/size limits, and partial-operation behavior were assessed where applicable. Findings are listed in Section L; where no finding is listed, the audit did not establish a defect rather than proving none exists.

## D. Documentation and Docstring Review

Module docstring present: yes. Documented definitions: 7/7. No docstring matched the five generic-pattern families used by the expanded audit.

Documentation was judged proportionally: public/non-obvious behavior requires specific contracts, while trivial fixtures and data files do not require artificial prose.

## E. Code Quality and Maintainability

Highest structural complexity: test_lm_studio_http_satisfies_openai_capability_without_product_aliasing (branches=3, AST nodes=222), _ModelsHandler.do_GET (branches=1, AST nodes=94), test_non_loopback_http_endpoint_requires_network_opt_in (branches=0, AST nodes=38), _config (branches=0, AST nodes=26), test_loopback_host_classifier_is_strict (branches=0, AST nodes=22). Trailing whitespace occurs at line(s): 21, 26, 42, 50, 58, 92, 103.

Broad exception handlers recorded by the scanner: 0. Global/nonlocal declarations: 0. Pass statements: 0. Each was treated as a review lead, not automatically as a defect.

## F. Potential AI-Generated-Code Indicators

Boilerplate/duplication indicator: 5 normalized-AST duplicate group(s); behavioral differences and context are documented in the cross-file matrix.

No claim about authorship is made without provenance evidence. Alternative explanations include manual boilerplate, generated consistency work, compatibility layers, or repeated domain contracts.

## G. Optimization and Performance

No confirmed performance problem was established for this file. Optimization should be driven by profiling or demonstrated scale limits.

Confirmed performance defects require measured impact; no micro-optimization recommendation is made solely from line count or syntax shape.

## H. Security and Robustness

No call matched the targeted process/network/database/file-write risk scanner; this is not a proof of security.

Targeted checks included subprocess shell use, path/archive handling, database calls, network calls, deserialization-adjacent behavior, file writes, resource limits, and malformed-input behavior where relevant. Suspicious binaries were not executed.

## I. Testing Review

Executed in the exact inventory: 3 collected test(s), all passing.

The exact non-duplicated inventory executed 258 tests in 86 reconciled partitions with zero failures, errors, or skips. The packaged duplicate self-test tree executed separately with 21 passes. A passing suite does not establish exhaustive semantic correctness.

## J. Missing Elements

Remediation and verification work is defined by: TEST-001, REPO-001.

## K. Redundancy and Consolidation Opportunities

This file has a behaviorally equivalent packaged/source test counterpart; see TEST-001. Normalized-AST duplicate group 18: test-suite/src/x86decomp_testkit/self_tests/test_adapter_capabilities.py:_config, test-suite/tests/test_adapter_capabilities.py:_config. Consolidation safety is assessed in CROSS_FILE_ANALYSIS.md. Normalized-AST duplicate group 19: test-suite/src/x86decomp_testkit/self_tests/test_adapter_capabilities.py:test_lm_studio_http_satisfies_openai_capability_without_product_aliasing, test-suite/tests/test_adapter_capabilities.py:test_lm_studio_http_satisfies_openai_capability_without_product_aliasing. Consolidation safety is assessed in CROSS_FILE_ANALYSIS.md. Normalized-AST duplicate group 20: test-suite/src/x86decomp_testkit/self_tests/test_adapter_capabilities.py:test_non_loopback_http_endpoint_requires_network_opt_in, test-suite/tests/test_adapter_capabilities.py:test_non_loopback_http_endpoint_requires_network_opt_in. Consolidation safety is assessed in CROSS_FILE_ANALYSIS.md. Normalized-AST duplicate group 21: test-suite/src/x86decomp_testkit/self_tests/test_adapter_capabilities.py:test_loopback_host_classifier_is_strict, test-suite/tests/test_adapter_capabilities.py:test_loopback_host_classifier_is_strict. Consolidation safety is assessed in CROSS_FILE_ANALYSIS.md. Normalized-AST duplicate group 22: test-suite/src/x86decomp_testkit/self_tests/test_adapter_capabilities.py:_ModelsHandler.do_GET, test-suite/tests/test_adapter_capabilities.py:_ModelsHandler.do_GET. Consolidation safety is assessed in CROSS_FILE_ANALYSIS.md.

## L. File-Level Findings

| Finding ID | Severity | Confidence | Symbol or line range | Summary | Evidence | Impact | Recommendation | Verification status |
|---|---|---|---|---|---|---|---|---|
| TEST-001 | Low | Verified | Six test-suite/tests ↔ x86decomp_testkit/self_tests file pairs | Six packaged self-test files duplicate source tests without an explicit synchronization gate | Six pairs have different file hashes but identical AST behavior after docstrings are removed. The packaged copies are used when the source test tree is unavailable; the source copies are used in a checkout. | Future fixes may land in only one copy, producing checkout/package behavior differences. | Generate packaged self-tests from one canonical source or add a normalized-AST synchronization gate. | Open |
| REPO-001 | Informational | Verified | Exact lines listed in FILE_INVENTORY.csv notes and per-file reports | Forty-five trailing-whitespace lines remain in seventeen text files | A byte-preserving line scan found 45 lines ending in spaces or tabs across 17 files; no files were modified. | Minor diff noise and possible editor/linter churn. | Classify intentional Markdown hard breaks, then remove only unintended trailing whitespace in a separate reviewed change. | Open |

## M. File-Level Verdict

- **Overall quality:** Material issue(s) require remediation.
- **Documentation quality:** Proportionate to file type, subject to repository-wide documentation findings.
- **Correctness confidence:** Moderate; complete static review plus repository tests, without exhaustive state-space proof.
- **Maintainability assessment:** Open maintainability or duplication concern.
- **Test confidence:** Executed in the exact inventory: 3 collected test(s), all passing.
- **Security assessment:** No unqualified security guarantee; file-specific risk evidence is described above.
- **Recommended priority:** Low
- **Open questions:** Intentionally perturb one copy and prove the new gate fails.; Run a format-aware trailing-whitespace check after cleanup.
- **Related follow-up:** TEST-001, REPO-001
- **Final audit status:** **Audited — complete**
