---
title: tests/native/test_staging_loop_runtime_windows.py
description: 4 exact current test nodes
original_path: tests/tests-native-test-staging-loop-runtime-windows.html
---

<a id="test-test-staging-context-resolution-and-compile-check"></a>
<a id="test-test-closed-loop-requires-consent-and-records-verified-result"></a>
<a id="test-test-runtime-static-validation-and-crash-mapping"></a>
<a id="test-test-windows-launcher-prefers-batch-on-windows-and-response-files"></a>

Section: Source-derived test reference

# `tests/native/test_staging_loop_runtime_windows.py`

4 current test nodes in the Toolkit behavior inventory.

> **Truth basis.** Node IDs, line numbers, docstrings, and direct call names are extracted from the AST. No behavior is inferred when a test lacks a docstring. Source SHA-256: `da1cf374737a7615578374f772b1d100e2756affcf6abf90c4e56941f4c82fe8`.

Metadata: Toolkit behavior · line 17

### `test_staging_context_resolution_and_compile_check`

No test docstring is declared. The node identifier and direct call names are shown without inferring additional behavior.

**Direct call names in source:** `source.write_text`, `StagingBridge`, `api.generate_context`, `mapping.write_text`, `NativeStore`, `read_text`, `len`, `json.dumps`, `api.compile_check`, `api.unresolved`, `api.resolve`, `json.loads`, `mapping.read_text`

**Node ID:** `tests/native/test_staging_loop_runtime_windows.py::test_staging_context_resolution_and_compile_check`

Metadata: Toolkit behavior · line 27

### `test_closed_loop_requires_consent_and_records_verified_result`

No test docstring is declared. The node identifier and direct call names are shown without inferring additional behavior.

**Direct call names in source:** `build_minimal_pe32`, `source.write_text`, `ClosedLoop`, `api.run`, `NativeStore`, `pytest.raises`, `api.show`

**Node ID:** `tests/native/test_staging_loop_runtime_windows.py::test_closed_loop_requires_consent_and_records_verified_result`

Metadata: Toolkit behavior · line 37

### `test_runtime_static_validation_and_crash_mapping`

No test docstring is declared. The node identifier and direct call names are shown without inferring additional behavior.

**Direct call names in source:** `build_minimal_pe32`, `NativeStore`, `audit`, `RuntimeValidation`, `api.validate_image`, `pytest.raises`, `api.launch`, `FunctionSlots`, `api.map_crash`

**Node ID:** `tests/native/test_staging_loop_runtime_windows.py::test_runtime_static_validation_and_crash_mapping`

Metadata: Toolkit behavior · line 47

### `test_windows_launcher_prefers_batch_on_windows_and_response_files`

No test docstring is declared. The node identifier and direct call names are shown without inferring additional behavior.

**Direct call names in source:** `support.mkdir`, `write_text`, `write_response_file`, `discover_ghidra_launcher`, `read_text`

**Node ID:** `tests/native/test_staging_loop_runtime_windows.py::test_windows_launcher_prefers_batch_on_windows_and_response_files`
