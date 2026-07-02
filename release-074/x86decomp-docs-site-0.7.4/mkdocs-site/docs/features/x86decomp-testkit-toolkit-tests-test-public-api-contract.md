---
title: x86decomp_testkit.toolkit_tests.test_public_api_contract
description: No module docstring is declared in the v0.7.4 source.
original_path: features/x86decomp-testkit-toolkit-tests-test-public-api-contract.html
---

<a id="function-test-unified-canonical-entry-point"></a>
<a id="function-test-abi-contract-loading"></a>
<a id="function-test-analysis-database-complete-public-surface"></a>
<a id="function-test-angr-public-file-wrappers"></a>
<a id="function-test-benchmark-metrics-and-runner"></a>
<a id="function-test-coff-remaining-value-objects-and-writer"></a>
<a id="function-test-compiler-lab-with-deterministic-fake-compiler"></a>
<a id="function-test-diff-disassembly-and-crosscheck"></a>
<a id="function-test-dynamic-file-wrapper-and-spec-loader"></a>
<a id="function-test-dynamorio-runner-with-fake-subprocess"></a>
<a id="function-verified-store"></a>
<a id="function-test-evidence-contradiction-require-verified-and-project-memory"></a>
<a id="function-test-exe-diff-extract-and-compare"></a>
<a id="function-test-ghidra-run-export-success"></a>
<a id="function-test-remaining-value-objects-and-peview"></a>
<a id="function-test-service-create-and-run"></a>
<a id="function-test-symbolic-clone-and-file-wrapper"></a>
<a id="function-test-toolchain-snapshot-util-contract-and-workqueue"></a>
<a id="function-test-cli-main-executes-public-entrypoint"></a>
<a id="function-test-streamable-http-mcp-public-methods"></a>
<a id="function-test-private-function-surface-regression"></a>
<a id="function-test-remaining-current-function-surface"></a>

Section: Source-derived feature and function reference

# x86decomp_testkit.toolkit_tests.test_public_api_contract

No module docstring is declared in the v0.7.4 source.

Metadata: verification harness · current · 22 functions/methods

**Source:** `test-suite/src/x86decomp_testkit/toolkit_tests/test_public_api_contract.py`

> **Truth basis.** Module and symbol names, signatures, line numbers, docstrings, and SHA-256 are read directly from the sealed source. When source docstrings are absent, this page says so instead of inferring behavior. Source SHA-256: `0db55c2047f507a231d9738d8dc5710114a13726768e81aa0160c3fa5b3ff3eb`.

## Functions and methods

Metadata: public · line 75

### test_unified_canonical_entry_point

No function or method docstring is declared in the v0.7.4 source.

```
def test_unified_canonical_entry_point(capsys: pytest.CaptureFixture[str]) -> None
```

**Catalog symbol:** `x86decomp_testkit.toolkit_tests.test_public_api_contract:test_unified_canonical_entry_point`

Metadata: public · line 88

### test_abi_contract_loading

No function or method docstring is declared in the v0.7.4 source.

```
def test_abi_contract_loading(tmp_path: Path) -> None
```

**Catalog symbol:** `x86decomp_testkit.toolkit_tests.test_public_api_contract:test_abi_contract_loading`

Metadata: public · line 107

### test_analysis_database_complete_public_surface

No function or method docstring is declared in the v0.7.4 source.

```
def test_analysis_database_complete_public_surface(tmp_path: Path) -> None
```

**Catalog symbol:** `x86decomp_testkit.toolkit_tests.test_public_api_contract:test_analysis_database_complete_public_surface`

Metadata: public · line 135

### test_angr_public_file_wrappers

No function or method docstring is declared in the v0.7.4 source.

```
def test_angr_public_file_wrappers(tmp_path: Path) -> None
```

**Catalog symbol:** `x86decomp_testkit.toolkit_tests.test_public_api_contract:test_angr_public_file_wrappers`

Metadata: public · line 157

### test_benchmark_metrics_and_runner

No function or method docstring is declared in the v0.7.4 source.

```
def test_benchmark_metrics_and_runner(tmp_path: Path) -> None
```

**Catalog symbol:** `x86decomp_testkit.toolkit_tests.test_public_api_contract:test_benchmark_metrics_and_runner`

Metadata: public · line 172

### test_coff_remaining_value_objects_and_writer

No function or method docstring is declared in the v0.7.4 source.

```
def test_coff_remaining_value_objects_and_writer(tmp_path: Path) -> None
```

**Catalog symbol:** `x86decomp_testkit.toolkit_tests.test_public_api_contract:test_coff_remaining_value_objects_and_writer`

Metadata: public · line 190

### test_compiler_lab_with_deterministic_fake_compiler

No function or method docstring is declared in the v0.7.4 source.

```
def test_compiler_lab_with_deterministic_fake_compiler(tmp_path: Path) -> None
```

**Catalog symbol:** `x86decomp_testkit.toolkit_tests.test_public_api_contract:test_compiler_lab_with_deterministic_fake_compiler`

Metadata: public · line 225

### test_diff_disassembly_and_crosscheck

No function or method docstring is declared in the v0.7.4 source.

```
def test_diff_disassembly_and_crosscheck(tmp_path: Path) -> None
```

**Catalog symbol:** `x86decomp_testkit.toolkit_tests.test_public_api_contract:test_diff_disassembly_and_crosscheck`

Metadata: public · line 241

### test_dynamic_file_wrapper_and_spec_loader

No function or method docstring is declared in the v0.7.4 source.

```
def test_dynamic_file_wrapper_and_spec_loader(tmp_path: Path) -> None
```

**Catalog symbol:** `x86decomp_testkit.toolkit_tests.test_public_api_contract:test_dynamic_file_wrapper_and_spec_loader`

Metadata: public · line 260

### test_dynamorio_runner_with_fake_subprocess

No function or method docstring is declared in the v0.7.4 source.

```
def test_dynamorio_runner_with_fake_subprocess(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None
```

**Catalog symbol:** `x86decomp_testkit.toolkit_tests.test_public_api_contract:test_dynamorio_runner_with_fake_subprocess`

Metadata: internal · line 283

### _verified_store

No function or method docstring is declared in the v0.7.4 source.

```
def _verified_store(project: Path) -> tuple[EvidenceStore, str, str]
```

**Catalog symbol:** `x86decomp_testkit.toolkit_tests.test_public_api_contract:_verified_store`

Metadata: public · line 296

### test_evidence_contradiction_require_verified_and_project_memory

No function or method docstring is declared in the v0.7.4 source.

```
def test_evidence_contradiction_require_verified_and_project_memory(tmp_path: Path) -> None
```

**Catalog symbol:** `x86decomp_testkit.toolkit_tests.test_public_api_contract:test_evidence_contradiction_require_verified_and_project_memory`

Metadata: public · line 307

### test_exe_diff_extract_and_compare

No function or method docstring is declared in the v0.7.4 source.

```
def test_exe_diff_extract_and_compare(tmp_path: Path) -> None
```

**Catalog symbol:** `x86decomp_testkit.toolkit_tests.test_public_api_contract:test_exe_diff_extract_and_compare`

Metadata: public · line 318

### test_ghidra_run_export_success

No function or method docstring is declared in the v0.7.4 source.

```
def test_ghidra_run_export_success(monkeypatch: pytest.MonkeyPatch) -> None
```

**Catalog symbol:** `x86decomp_testkit.toolkit_tests.test_public_api_contract:test_ghidra_run_export_success`

Metadata: public · line 326

### test_remaining_value_objects_and_peview

No function or method docstring is declared in the v0.7.4 source.

```
def test_remaining_value_objects_and_peview(tmp_path: Path) -> None
```

**Catalog symbol:** `x86decomp_testkit.toolkit_tests.test_public_api_contract:test_remaining_value_objects_and_peview`

Metadata: public · line 343

### test_service_create_and_run

No function or method docstring is declared in the v0.7.4 source.

```
def test_service_create_and_run(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None
```

**Catalog symbol:** `x86decomp_testkit.toolkit_tests.test_public_api_contract:test_service_create_and_run`

Metadata: public · line 354

### test_symbolic_clone_and_file_wrapper

No function or method docstring is declared in the v0.7.4 source.

```
def test_symbolic_clone_and_file_wrapper(tmp_path: Path) -> None
```

**Catalog symbol:** `x86decomp_testkit.toolkit_tests.test_public_api_contract:test_symbolic_clone_and_file_wrapper`

Metadata: public · line 369

### test_toolchain_snapshot_util_contract_and_workqueue

No function or method docstring is declared in the v0.7.4 source.

```
def test_toolchain_snapshot_util_contract_and_workqueue(tmp_path: Path) -> None
```

**Catalog symbol:** `x86decomp_testkit.toolkit_tests.test_public_api_contract:test_toolchain_snapshot_util_contract_and_workqueue`

Metadata: public · line 391

### test_cli_main_executes_public_entrypoint

No function or method docstring is declared in the v0.7.4 source.

```
def test_cli_main_executes_public_entrypoint(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None
```

**Catalog symbol:** `x86decomp_testkit.toolkit_tests.test_public_api_contract:test_cli_main_executes_public_entrypoint`

Metadata: public · line 400

### test_streamable_http_mcp_public_methods

No function or method docstring is declared in the v0.7.4 source.

```
def test_streamable_http_mcp_public_methods(monkeypatch: pytest.MonkeyPatch) -> None
```

**Catalog symbol:** `x86decomp_testkit.toolkit_tests.test_public_api_contract:test_streamable_http_mcp_public_methods`

Metadata: public · line 446

### test_private_function_surface_regression

Exercise the remaining internal function bodies so no defined function is omitted.

```
def test_private_function_surface_regression(monkeypatch: pytest.MonkeyPatch) -> None
```

**Catalog symbol:** `x86decomp_testkit.toolkit_tests.test_public_api_contract:test_private_function_surface_regression`

Metadata: public · line 485

### test_remaining_current_function_surface

No function or method docstring is declared in the v0.7.4 source.

```
def test_remaining_current_function_surface(tmp_path: Path) -> None
```

**Catalog symbol:** `x86decomp_testkit.toolkit_tests.test_public_api_contract:test_remaining_current_function_surface`
