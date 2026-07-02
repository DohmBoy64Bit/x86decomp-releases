---
title: x86decomp_testkit.adapters.installation
description: No module docstring is declared in the v0.7.4 source.
original_path: features/x86decomp-testkit-adapters-installation.html
---

<a id="function-yes"></a>
<a id="function-find-package-manager"></a>
<a id="function-run-checked"></a>
<a id="function-install-python-adapter"></a>
<a id="function-install-github-release"></a>
<a id="function-install-package-manager-adapter"></a>
<a id="function-validate-custom-path"></a>
<a id="function-automatic-install-available"></a>
<a id="function-install-adapter"></a>
<a id="function-resolve-missing-adapters"></a>

Section: Source-derived feature and function reference

# x86decomp_testkit.adapters.installation

No module docstring is declared in the v0.7.4 source.

Metadata: verification harness · current · 10 functions/methods

**Source:** `test-suite/src/x86decomp_testkit/adapters/installation.py`

> **Truth basis.** Module and symbol names, signatures, line numbers, docstrings, and SHA-256 are read directly from the sealed source. When source docstrings are absent, this page says so instead of inferring behavior. Source SHA-256: `44488c89ba434c7bc704118ebc1bb86329eb1a9cfadde5237bcd3b19130266d1`.

## Functions and methods

Metadata: internal · line 82

### _yes

No function or method docstring is declared in the v0.7.4 source.

```
def _yes(value: str) -> bool
```

**Catalog symbol:** `x86decomp_testkit.adapters.installation:_yes`

Metadata: internal · line 86

### _find_package_manager

No function or method docstring is declared in the v0.7.4 source.

```
def _find_package_manager() -> str | None
```

**Catalog symbol:** `x86decomp_testkit.adapters.installation:_find_package_manager`

Metadata: internal · line 93

### _run_checked

No function or method docstring is declared in the v0.7.4 source.

```
def _run_checked(command: list[str], event_logger: JsonlEventLogger | None = None) -> None
```

**Catalog symbol:** `x86decomp_testkit.adapters.installation:_run_checked`

Metadata: public · line 101

### install_python_adapter

No function or method docstring is declared in the v0.7.4 source.

```
def install_python_adapter(spec: AdapterSpec, config: TestConfig, event_logger: JsonlEventLogger | None = None) -> None
```

**Catalog symbol:** `x86decomp_testkit.adapters.installation:install_python_adapter`

Metadata: public · line 108

### install_github_release

No function or method docstring is declared in the v0.7.4 source.

```
def install_github_release(spec: AdapterSpec, config: TestConfig, event_logger: JsonlEventLogger | None = None) -> Path
```

**Catalog symbol:** `x86decomp_testkit.adapters.installation:install_github_release`

Metadata: public · line 157

### install_package_manager_adapter

No function or method docstring is declared in the v0.7.4 source.

```
def install_package_manager_adapter(spec: AdapterSpec, event_logger: JsonlEventLogger | None = None) -> None
```

**Catalog symbol:** `x86decomp_testkit.adapters.installation:install_package_manager_adapter`

Metadata: internal · line 182

### _validate_custom_path

No function or method docstring is declared in the v0.7.4 source.

```
def _validate_custom_path(spec: AdapterSpec, value: str, config: TestConfig) -> ProbeResult
```

**Catalog symbol:** `x86decomp_testkit.adapters.installation:_validate_custom_path`

Metadata: internal · line 205

### _automatic_install_available

No function or method docstring is declared in the v0.7.4 source.

```
def _automatic_install_available(spec: AdapterSpec) -> bool
```

**Catalog symbol:** `x86decomp_testkit.adapters.installation:_automatic_install_available`

Metadata: public · line 214

### install_adapter

No function or method docstring is declared in the v0.7.4 source.

```
def install_adapter(spec: AdapterSpec, config: TestConfig, event_logger: JsonlEventLogger | None = None) -> None
```

**Catalog symbol:** `x86decomp_testkit.adapters.installation:install_adapter`

Metadata: public · line 223

### resolve_missing_adapters

Detect first, then prompt only for missing adapters.

```
def resolve_missing_adapters(catalog: dict[str, AdapterSpec], config: TestConfig, config_path: Path | None = None, adapter_ids: list[str] | None = None, prompt: Prompt = input, assume_yes: bool = False, event_logger: JsonlEventLogger | None = None) -> list[ProbeResult]
```

**Catalog symbol:** `x86decomp_testkit.adapters.installation:resolve_missing_adapters`
