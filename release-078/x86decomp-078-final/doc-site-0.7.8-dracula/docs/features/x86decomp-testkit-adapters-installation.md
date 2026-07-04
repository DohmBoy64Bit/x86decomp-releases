---
title: x86decomp_testkit.adapters.installation
description: No module docstring is declared in the 0.7.8 source.
---

# `x86decomp_testkit.adapters.installation`

No module docstring is declared in the 0.7.8 source.

**Area:** Verification harness  
**Source:** `test-suite/src/x86decomp_testkit/adapters/installation.py`  
**SHA-256:** `543de6cae816ebe32be9762b84e33676f143fd497f3d57aea34c6b24223f0cb7`  
**Functions/methods:** 10

> Module names, signatures, line numbers, and docstrings are extracted directly from the source AST. No behavior is inferred when a docstring is absent.

## Functions and methods

<a id="function-yes"></a>

### `_yes`

No function or method docstring is declared in the 0.7.8 source.

```python
def _yes(value: str) -> bool
```

**Catalog symbol:** `x86decomp_testkit.adapters.installation:_yes`  
**Visibility:** internal  
**Source line:** 82

<a id="function-find-package-manager"></a>

### `_find_package_manager`

No function or method docstring is declared in the 0.7.8 source.

```python
def _find_package_manager() -> str | None
```

**Catalog symbol:** `x86decomp_testkit.adapters.installation:_find_package_manager`  
**Visibility:** internal  
**Source line:** 86

<a id="function-run-checked"></a>

### `_run_checked`

No function or method docstring is declared in the 0.7.8 source.

```python
def _run_checked(command: list[str], event_logger: JsonlEventLogger | None=None) -> None
```

**Catalog symbol:** `x86decomp_testkit.adapters.installation:_run_checked`  
**Visibility:** internal  
**Source line:** 93

<a id="function-install-python-adapter"></a>

### `install_python_adapter`

No function or method docstring is declared in the 0.7.8 source.

```python
def install_python_adapter(spec: AdapterSpec, config: TestConfig, event_logger: JsonlEventLogger | None=None) -> None
```

**Catalog symbol:** `x86decomp_testkit.adapters.installation:install_python_adapter`  
**Visibility:** public  
**Source line:** 101

<a id="function-install-github-release"></a>

### `install_github_release`

No function or method docstring is declared in the 0.7.8 source.

```python
def install_github_release(spec: AdapterSpec, config: TestConfig, event_logger: JsonlEventLogger | None=None) -> Path
```

**Catalog symbol:** `x86decomp_testkit.adapters.installation:install_github_release`  
**Visibility:** public  
**Source line:** 108

<a id="function-install-package-manager-adapter"></a>

### `install_package_manager_adapter`

No function or method docstring is declared in the 0.7.8 source.

```python
def install_package_manager_adapter(spec: AdapterSpec, event_logger: JsonlEventLogger | None=None) -> None
```

**Catalog symbol:** `x86decomp_testkit.adapters.installation:install_package_manager_adapter`  
**Visibility:** public  
**Source line:** 162

<a id="function-validate-custom-path"></a>

### `_validate_custom_path`

No function or method docstring is declared in the 0.7.8 source.

```python
def _validate_custom_path(spec: AdapterSpec, value: str, config: TestConfig) -> ProbeResult
```

**Catalog symbol:** `x86decomp_testkit.adapters.installation:_validate_custom_path`  
**Visibility:** internal  
**Source line:** 187

<a id="function-automatic-install-available"></a>

### `_automatic_install_available`

No function or method docstring is declared in the 0.7.8 source.

```python
def _automatic_install_available(spec: AdapterSpec) -> bool
```

**Catalog symbol:** `x86decomp_testkit.adapters.installation:_automatic_install_available`  
**Visibility:** internal  
**Source line:** 210

<a id="function-install-adapter"></a>

### `install_adapter`

No function or method docstring is declared in the 0.7.8 source.

```python
def install_adapter(spec: AdapterSpec, config: TestConfig, event_logger: JsonlEventLogger | None=None) -> None
```

**Catalog symbol:** `x86decomp_testkit.adapters.installation:install_adapter`  
**Visibility:** public  
**Source line:** 219

<a id="function-resolve-missing-adapters"></a>

### `resolve_missing_adapters`

Detect first, then prompt only for missing adapters.

No installed adapter produces an interactive question. A missing adapter is never
silently skipped: it ends installed or remains an explicit unresolved ProbeResult.

```python
def resolve_missing_adapters(catalog: dict[str, AdapterSpec], config: TestConfig, config_path: Path | None=None, adapter_ids: list[str] | None=None, prompt: Prompt=input, assume_yes: bool=False, event_logger: JsonlEventLogger | None=None) -> list[ProbeResult]
```

**Catalog symbol:** `x86decomp_testkit.adapters.installation:resolve_missing_adapters`  
**Visibility:** public  
**Source line:** 228
