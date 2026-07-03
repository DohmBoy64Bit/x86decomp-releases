---
title: tests/native/test_staging_loop_runtime_windows.py
description: Source-derived reference for 4 collected test nodes.
---

# `tests/native/test_staging_loop_runtime_windows.py`

**Collected nodes:** 4  
**Source SHA-256:** `da1cf374737a7615578374f772b1d100e2756affcf6abf90c4e56941f4c82fe8`

> Node identifiers, source lines, docstrings, and direct call names are extracted from pytest collection and the source AST. No behavior is inferred when a test has no docstring.

## `test_staging_context_resolution_and_compile_check`

No test docstring is declared.

**Direct call names in source:** `(tmp_path / 'context.h').read_text`, `NativeStore`, `StagingBridge`, `api.compile_check`, `api.generate_context`, `api.resolve`, `api.unresolved`, `json.dumps`, `json.loads`, `len`, `mapping.read_text`, `mapping.write_text`, `source.write_text`  
**Node ID:** `tests/native/test_staging_loop_runtime_windows.py::test_staging_context_resolution_and_compile_check`  
**Area:** Toolkit behavior  
**Source line:** 17

## `test_closed_loop_requires_consent_and_records_verified_result`

No test docstring is declared.

**Direct call names in source:** `ClosedLoop`, `NativeStore`, `api.run`, `api.show`, `build_minimal_pe32`, `pytest.raises`, `source.write_text`  
**Node ID:** `tests/native/test_staging_loop_runtime_windows.py::test_closed_loop_requires_consent_and_records_verified_result`  
**Area:** Toolkit behavior  
**Source line:** 27

## `test_runtime_static_validation_and_crash_mapping`

No test docstring is declared.

**Direct call names in source:** `FunctionSlots`, `FunctionSlots(store).audit`, `NativeStore`, `RuntimeValidation`, `api.launch`, `api.map_crash`, `api.validate_image`, `build_minimal_pe32`, `pytest.raises`  
**Node ID:** `tests/native/test_staging_loop_runtime_windows.py::test_runtime_static_validation_and_crash_mapping`  
**Area:** Toolkit behavior  
**Source line:** 37

## `test_windows_launcher_prefers_batch_on_windows_and_response_files`

No test docstring is declared.

**Direct call names in source:** `(support / 'analyzeHeadless').write_text`, `(support / 'analyzeHeadless.bat').write_text`, `(tmp_path / 'args.rsp').read_text`, `discover_ghidra_launcher`, `support.mkdir`, `write_response_file`  
**Node ID:** `tests/native/test_staging_loop_runtime_windows.py::test_windows_launcher_prefers_batch_on_windows_and_response_files`  
**Area:** Toolkit behavior  
**Source line:** 47
