---
title: x86decomp_testkit.live_adapters
description: No module docstring is declared in the 0.7.8 source.
---

# `x86decomp_testkit.live_adapters`

No module docstring is declared in the 0.7.8 source.

**Area:** Verification harness  
**Source:** `test-suite/src/x86decomp_testkit/live_adapters.py`  
**SHA-256:** `fc5d0245f96eb7e22836fbb54a324921e023eb32a59a75936127e583bf16dc52`  
**Functions/methods:** 9

> Module names, signatures, line numbers, and docstrings are extracted directly from the source AST. No behavior is inferred when a docstring is absent.

## Functions and methods

<a id="function-path-for"></a>

### `_path_for`

No function or method docstring is declared in the 0.7.8 source.

```python
def _path_for(result: ProbeResult, spec: AdapterSpec) -> Path | None
```

**Catalog symbol:** `x86decomp_testkit.live_adapters:_path_for`  
**Visibility:** internal  
**Source line:** 21

<a id="function-python-adapter-test"></a>

### `_python_adapter_test`

No function or method docstring is declared in the 0.7.8 source.

```python
def _python_adapter_test(spec: AdapterSpec, result: ProbeResult) -> TestResult
```

**Catalog symbol:** `x86decomp_testkit.live_adapters:_python_adapter_test`  
**Visibility:** internal  
**Source line:** 48

<a id="function-generic-executable-test"></a>

### `_generic_executable_test`

No function or method docstring is declared in the 0.7.8 source.

```python
def _generic_executable_test(spec: AdapterSpec, result: ProbeResult, config: TestConfig, output_directory: Path, event_logger: JsonlEventLogger) -> TestResult
```

**Catalog symbol:** `x86decomp_testkit.live_adapters:_generic_executable_test`  
**Visibility:** internal  
**Source line:** 74

<a id="function-compiler-test"></a>

### `_compiler_test`

No function or method docstring is declared in the 0.7.8 source.

```python
def _compiler_test(spec: AdapterSpec, result: ProbeResult, config: TestConfig, output_directory: Path, event_logger: JsonlEventLogger) -> TestResult
```

**Catalog symbol:** `x86decomp_testkit.live_adapters:_compiler_test`  
**Visibility:** internal  
**Source line:** 98

<a id="function-lld-link-test"></a>

### `_lld_link_test`

No function or method docstring is declared in the 0.7.8 source.

```python
def _lld_link_test(spec: AdapterSpec, result: ProbeResult, config: TestConfig, output_directory: Path, event_logger: JsonlEventLogger, adapter_results: dict[str, ProbeResult], catalog: dict[str, AdapterSpec]) -> TestResult
```

**Catalog symbol:** `x86decomp_testkit.live_adapters:_lld_link_test`  
**Visibility:** internal  
**Source line:** 130

<a id="function-ghidra-test"></a>

### `_ghidra_test`

No function or method docstring is declared in the 0.7.8 source.

```python
def _ghidra_test(spec: AdapterSpec, result: ProbeResult, config: TestConfig, output_directory: Path, event_logger: JsonlEventLogger) -> TestResult
```

**Catalog symbol:** `x86decomp_testkit.live_adapters:_ghidra_test`  
**Visibility:** internal  
**Source line:** 167

<a id="function-dynamorio-test"></a>

### `_dynamorio_test`

No function or method docstring is declared in the 0.7.8 source.

```python
def _dynamorio_test(spec: AdapterSpec, result: ProbeResult, config: TestConfig, output_directory: Path, event_logger: JsonlEventLogger) -> TestResult
```

**Catalog symbol:** `x86decomp_testkit.live_adapters:_dynamorio_test`  
**Visibility:** internal  
**Source line:** 201

<a id="function-objdiff-test"></a>

### `_objdiff_test`

No function or method docstring is declared in the 0.7.8 source.

```python
def _objdiff_test(spec: AdapterSpec, result: ProbeResult, config: TestConfig, output_directory: Path, event_logger: JsonlEventLogger) -> TestResult
```

**Catalog symbol:** `x86decomp_testkit.live_adapters:_objdiff_test`  
**Visibility:** internal  
**Source line:** 229

<a id="function-run-live-adapter-tests"></a>

### `run_live_adapter_tests`

No function or method docstring is declared in the 0.7.8 source.

```python
def run_live_adapter_tests(catalog: dict[str, AdapterSpec], probe_results: list[ProbeResult], config: TestConfig, output_directory: Path, event_logger: JsonlEventLogger) -> list[TestResult]
```

**Catalog symbol:** `x86decomp_testkit.live_adapters:run_live_adapter_tests`  
**Visibility:** public  
**Source line:** 252
