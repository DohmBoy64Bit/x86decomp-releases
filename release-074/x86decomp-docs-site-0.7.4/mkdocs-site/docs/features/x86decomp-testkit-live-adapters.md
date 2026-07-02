---
title: x86decomp_testkit.live_adapters
description: No module docstring is declared in the v0.7.4 source.
original_path: features/x86decomp-testkit-live-adapters.html
---

<a id="function-path-for"></a>
<a id="function-python-adapter-test"></a>
<a id="function-generic-executable-test"></a>
<a id="function-compiler-test"></a>
<a id="function-lld-link-test"></a>
<a id="function-ghidra-test"></a>
<a id="function-dynamorio-test"></a>
<a id="function-objdiff-test"></a>
<a id="function-run-live-adapter-tests"></a>

Section: Source-derived feature and function reference

# x86decomp_testkit.live_adapters

No module docstring is declared in the v0.7.4 source.

Metadata: verification harness · current · 9 functions/methods

**Source:** `test-suite/src/x86decomp_testkit/live_adapters.py`

> **Truth basis.** Module and symbol names, signatures, line numbers, docstrings, and SHA-256 are read directly from the sealed source. When source docstrings are absent, this page says so instead of inferring behavior. Source SHA-256: `49ee078112933e69aa34dd86330f6ddaa35b59c224388206db5600fbd13c9cb5`.

## Functions and methods

Metadata: internal · line 21

### _path_for

No function or method docstring is declared in the v0.7.4 source.

```
def _path_for(result: ProbeResult, spec: AdapterSpec) -> Path | None
```

**Catalog symbol:** `x86decomp_testkit.live_adapters:_path_for`

Metadata: internal · line 43

### _python_adapter_test

No function or method docstring is declared in the v0.7.4 source.

```
def _python_adapter_test(spec: AdapterSpec, result: ProbeResult) -> TestResult
```

**Catalog symbol:** `x86decomp_testkit.live_adapters:_python_adapter_test`

Metadata: internal · line 69

### _generic_executable_test

No function or method docstring is declared in the v0.7.4 source.

```
def _generic_executable_test(spec: AdapterSpec, result: ProbeResult, config: TestConfig, output_directory: Path, event_logger: JsonlEventLogger) -> TestResult
```

**Catalog symbol:** `x86decomp_testkit.live_adapters:_generic_executable_test`

Metadata: internal · line 93

### _compiler_test

No function or method docstring is declared in the v0.7.4 source.

```
def _compiler_test(spec: AdapterSpec, result: ProbeResult, config: TestConfig, output_directory: Path, event_logger: JsonlEventLogger) -> TestResult
```

**Catalog symbol:** `x86decomp_testkit.live_adapters:_compiler_test`

Metadata: internal · line 125

### _lld_link_test

No function or method docstring is declared in the v0.7.4 source.

```
def _lld_link_test(spec: AdapterSpec, result: ProbeResult, config: TestConfig, output_directory: Path, event_logger: JsonlEventLogger, adapter_results: dict[str, ProbeResult], catalog: dict[str, AdapterSpec]) -> TestResult
```

**Catalog symbol:** `x86decomp_testkit.live_adapters:_lld_link_test`

Metadata: internal · line 162

### _ghidra_test

No function or method docstring is declared in the v0.7.4 source.

```
def _ghidra_test(spec: AdapterSpec, result: ProbeResult, config: TestConfig, output_directory: Path, event_logger: JsonlEventLogger) -> TestResult
```

**Catalog symbol:** `x86decomp_testkit.live_adapters:_ghidra_test`

Metadata: internal · line 196

### _dynamorio_test

No function or method docstring is declared in the v0.7.4 source.

```
def _dynamorio_test(spec: AdapterSpec, result: ProbeResult, config: TestConfig, output_directory: Path, event_logger: JsonlEventLogger) -> TestResult
```

**Catalog symbol:** `x86decomp_testkit.live_adapters:_dynamorio_test`

Metadata: internal · line 224

### _objdiff_test

No function or method docstring is declared in the v0.7.4 source.

```
def _objdiff_test(spec: AdapterSpec, result: ProbeResult, config: TestConfig, output_directory: Path, event_logger: JsonlEventLogger) -> TestResult
```

**Catalog symbol:** `x86decomp_testkit.live_adapters:_objdiff_test`

Metadata: public · line 247

### run_live_adapter_tests

No function or method docstring is declared in the v0.7.4 source.

```
def run_live_adapter_tests(catalog: dict[str, AdapterSpec], probe_results: list[ProbeResult], config: TestConfig, output_directory: Path, event_logger: JsonlEventLogger) -> list[TestResult]
```

**Catalog symbol:** `x86decomp_testkit.live_adapters:run_live_adapter_tests`
