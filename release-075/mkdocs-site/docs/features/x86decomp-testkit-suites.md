---
title: x86decomp_testkit.suites
description: No module docstring is declared in the 0.7.5 source.
---

# `x86decomp_testkit.suites`

No module docstring is declared in the 0.7.5 source.

**Area:** Verification harness  
**Source:** `test-suite/src/x86decomp_testkit/suites.py`  
**SHA-256:** `54f93a39c0fb752a58b31348949dcde6e7037ac905c6c1c5ce9e029700a19a35`  
**Functions/methods:** 12

> Module names, signatures, line numbers, and docstrings are extracted directly from the source AST. No behavior is inferred when a docstring is absent.

## Functions and methods

<a id="function-missing"></a>

### `_missing`

No function or method docstring is declared in the 0.7.5 source.

```python
def _missing(adapter_results: list[ProbeResult], required: tuple[str, ...]) -> list[str]
```

**Catalog symbol:** `x86decomp_testkit.suites:_missing`  
**Visibility:** internal  
**Source line:** 25

<a id="function-result"></a>

### `_result`

No function or method docstring is declared in the 0.7.5 source.

```python
def _result(test_id: str, suite: str, passed: bool, summary: str, *, details: dict[str, Any] | None=None) -> TestResult
```

**Catalog symbol:** `x86decomp_testkit.suites:_result`  
**Visibility:** internal  
**Source line:** 29

<a id="function-run-inventory-tests"></a>

### `run_inventory_tests`

No function or method docstring is declared in the 0.7.5 source.

```python
def run_inventory_tests(config: TestConfig, output_directory: Path, feature_catalog_path: Path) -> tuple[dict[str, Any], list[TestResult]]
```

**Catalog symbol:** `x86decomp_testkit.suites:run_inventory_tests`  
**Visibility:** public  
**Source line:** 43

<a id="function-run-cli-surface-tests"></a>

### `run_cli_surface_tests`

No function or method docstring is declared in the 0.7.5 source.

```python
def run_cli_surface_tests(config: TestConfig, inventory: dict[str, Any], output_directory: Path, event_logger: JsonlEventLogger) -> list[TestResult]
```

**Catalog symbol:** `x86decomp_testkit.suites:run_cli_surface_tests`  
**Visibility:** public  
**Source line:** 87

<a id="function-verify-manifest"></a>

### `_verify_manifest`

No function or method docstring is declared in the 0.7.5 source.

```python
def _verify_manifest(toolkit_root: Path) -> tuple[bool, dict[str, Any]]
```

**Catalog symbol:** `x86decomp_testkit.suites:_verify_manifest`  
**Visibility:** internal  
**Source line:** 111

<a id="function-validate-schemas"></a>

### `_validate_schemas`

No function or method docstring is declared in the 0.7.5 source.

```python
def _validate_schemas(toolkit_root: Path) -> tuple[bool, dict[str, Any]]
```

**Catalog symbol:** `x86decomp_testkit.suites:_validate_schemas`  
**Visibility:** internal  
**Source line:** 139

<a id="function-validate-java"></a>

### `_validate_java`

No function or method docstring is declared in the 0.7.5 source.

```python
def _validate_java(toolkit_root: Path) -> tuple[bool, dict[str, Any]]
```

**Catalog symbol:** `x86decomp_testkit.suites:_validate_java`  
**Visibility:** internal  
**Source line:** 156

<a id="function-validate-skill"></a>

### `_validate_skill`

No function or method docstring is declared in the 0.7.5 source.

```python
def _validate_skill(toolkit_root: Path) -> tuple[bool, dict[str, Any]]
```

**Catalog symbol:** `x86decomp_testkit.suites:_validate_skill`  
**Visibility:** internal  
**Source line:** 172

<a id="function-run-structural-tests"></a>

### `run_structural_tests`

No function or method docstring is declared in the 0.7.5 source.

```python
def run_structural_tests(config: TestConfig, suite_root: Path, output_directory: Path, event_logger: JsonlEventLogger, adapter_results: list[ProbeResult]) -> list[TestResult]
```

**Catalog symbol:** `x86decomp_testkit.suites:run_structural_tests`  
**Visibility:** public  
**Source line:** 192

<a id="function-run-harness-self-tests"></a>

### `run_harness_self_tests`

No function or method docstring is declared in the 0.7.5 source.

```python
def run_harness_self_tests(config: TestConfig, suite_root: Path, output_directory: Path, event_logger: JsonlEventLogger, adapter_results: list[ProbeResult]) -> list[TestResult]
```

**Catalog symbol:** `x86decomp_testkit.suites:run_harness_self_tests`  
**Visibility:** public  
**Source line:** 260

<a id="function-run-pytest-and-coverage"></a>

### `run_pytest_and_coverage`

No function or method docstring is declared in the 0.7.5 source.

```python
def run_pytest_and_coverage(config: TestConfig, package_root: Path, output_directory: Path, event_logger: JsonlEventLogger, adapter_results: list[ProbeResult]) -> list[TestResult]
```

**Catalog symbol:** `x86decomp_testkit.suites:run_pytest_and_coverage`  
**Visibility:** public  
**Source line:** 302

<a id="function-run-packaging-tests"></a>

### `run_packaging_tests`

No function or method docstring is declared in the 0.7.5 source.

```python
def run_packaging_tests(config: TestConfig, output_directory: Path, event_logger: JsonlEventLogger, adapter_results: list[ProbeResult]) -> list[TestResult]
```

**Catalog symbol:** `x86decomp_testkit.suites:run_packaging_tests`  
**Visibility:** public  
**Source line:** 386
