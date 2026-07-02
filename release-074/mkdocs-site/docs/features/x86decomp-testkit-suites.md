---
title: x86decomp_testkit.suites
description: No module docstring is declared in the v0.7.4 source.
original_path: features/x86decomp-testkit-suites.html
---

<a id="function-missing"></a>
<a id="function-result"></a>
<a id="function-run-inventory-tests"></a>
<a id="function-run-cli-surface-tests"></a>
<a id="function-verify-manifest"></a>
<a id="function-validate-schemas"></a>
<a id="function-validate-java"></a>
<a id="function-validate-skill"></a>
<a id="function-run-structural-tests"></a>
<a id="function-run-harness-self-tests"></a>
<a id="function-run-pytest-and-coverage"></a>
<a id="function-run-packaging-tests"></a>

Section: Source-derived feature and function reference

# x86decomp_testkit.suites

No module docstring is declared in the v0.7.4 source.

Metadata: verification harness · current · 12 functions/methods

**Source:** `test-suite/src/x86decomp_testkit/suites.py`

> **Truth basis.** Module and symbol names, signatures, line numbers, docstrings, and SHA-256 are read directly from the sealed source. When source docstrings are absent, this page says so instead of inferring behavior. Source SHA-256: `8b08e944e5d2672abd926d90146ae7a8a7c4103c1c0ddbe3eb5496f8dcb6fc52`.

## Functions and methods

Metadata: internal · line 25

### _missing

No function or method docstring is declared in the v0.7.4 source.

```
def _missing(adapter_results: list[ProbeResult], required: tuple[str, ...]) -> list[str]
```

**Catalog symbol:** `x86decomp_testkit.suites:_missing`

Metadata: internal · line 29

### _result

No function or method docstring is declared in the v0.7.4 source.

```
def _result(test_id: str, suite: str, passed: bool, summary: str, *, details: dict[str, Any] | None = None) -> TestResult
```

**Catalog symbol:** `x86decomp_testkit.suites:_result`

Metadata: public · line 43

### run_inventory_tests

No function or method docstring is declared in the v0.7.4 source.

```
def run_inventory_tests(config: TestConfig, output_directory: Path, feature_catalog_path: Path) -> tuple[dict[str, Any], list[TestResult]]
```

**Catalog symbol:** `x86decomp_testkit.suites:run_inventory_tests`

Metadata: public · line 87

### run_cli_surface_tests

No function or method docstring is declared in the v0.7.4 source.

```
def run_cli_surface_tests(config: TestConfig, inventory: dict[str, Any], output_directory: Path, event_logger: JsonlEventLogger) -> list[TestResult]
```

**Catalog symbol:** `x86decomp_testkit.suites:run_cli_surface_tests`

Metadata: internal · line 111

### _verify_manifest

No function or method docstring is declared in the v0.7.4 source.

```
def _verify_manifest(toolkit_root: Path) -> tuple[bool, dict[str, Any]]
```

**Catalog symbol:** `x86decomp_testkit.suites:_verify_manifest`

Metadata: internal · line 137

### _validate_schemas

No function or method docstring is declared in the v0.7.4 source.

```
def _validate_schemas(toolkit_root: Path) -> tuple[bool, dict[str, Any]]
```

**Catalog symbol:** `x86decomp_testkit.suites:_validate_schemas`

Metadata: internal · line 154

### _validate_java

No function or method docstring is declared in the v0.7.4 source.

```
def _validate_java(toolkit_root: Path) -> tuple[bool, dict[str, Any]]
```

**Catalog symbol:** `x86decomp_testkit.suites:_validate_java`

Metadata: internal · line 170

### _validate_skill

No function or method docstring is declared in the v0.7.4 source.

```
def _validate_skill(toolkit_root: Path) -> tuple[bool, dict[str, Any]]
```

**Catalog symbol:** `x86decomp_testkit.suites:_validate_skill`

Metadata: public · line 190

### run_structural_tests

No function or method docstring is declared in the v0.7.4 source.

```
def run_structural_tests(config: TestConfig, suite_root: Path, output_directory: Path, event_logger: JsonlEventLogger, adapter_results: list[ProbeResult]) -> list[TestResult]
```

**Catalog symbol:** `x86decomp_testkit.suites:run_structural_tests`

Metadata: public · line 258

### run_harness_self_tests

No function or method docstring is declared in the v0.7.4 source.

```
def run_harness_self_tests(config: TestConfig, suite_root: Path, output_directory: Path, event_logger: JsonlEventLogger, adapter_results: list[ProbeResult]) -> list[TestResult]
```

**Catalog symbol:** `x86decomp_testkit.suites:run_harness_self_tests`

Metadata: public · line 300

### run_pytest_and_coverage

No function or method docstring is declared in the v0.7.4 source.

```
def run_pytest_and_coverage(config: TestConfig, package_root: Path, output_directory: Path, event_logger: JsonlEventLogger, adapter_results: list[ProbeResult]) -> list[TestResult]
```

**Catalog symbol:** `x86decomp_testkit.suites:run_pytest_and_coverage`

Metadata: public · line 384

### run_packaging_tests

No function or method docstring is declared in the v0.7.4 source.

```
def run_packaging_tests(config: TestConfig, output_directory: Path, event_logger: JsonlEventLogger, adapter_results: list[ProbeResult]) -> list[TestResult]
```

**Catalog symbol:** `x86decomp_testkit.suites:run_packaging_tests`
