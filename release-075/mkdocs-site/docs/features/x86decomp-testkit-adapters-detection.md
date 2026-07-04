---
title: x86decomp_testkit.adapters.detection
description: No module docstring is declared in the 0.7.5 source.
---

# `x86decomp_testkit.adapters.detection`

No module docstring is declared in the 0.7.5 source.

**Area:** Verification harness  
**Source:** `test-suite/src/x86decomp_testkit/adapters/detection.py`  
**SHA-256:** `442ec5437067e4ccb91fdc56f7a3dcf9d5d8c09327e98897bd9858cfacd6715a`  
**Functions/methods:** 9

> Module names, signatures, line numbers, and docstrings are extracted directly from the source AST. No behavior is inferred when a docstring is absent.

## Functions and methods

<a id="function-module-version"></a>

### `_module_version`

No function or method docstring is declared in the 0.7.5 source.

```python
def _module_version(module_name: str) -> str | None
```

**Catalog symbol:** `x86decomp_testkit.adapters.detection:_module_version`  
**Visibility:** internal  
**Source line:** 16

<a id="function-run-version"></a>

### `_run_version`

No function or method docstring is declared in the 0.7.5 source.

```python
def _run_version(executable: Path, args: tuple[str, ...], timeout: int=15) -> tuple[str | None, str | None]
```

**Catalog symbol:** `x86decomp_testkit.adapters.detection:_run_version`  
**Visibility:** internal  
**Source line:** 35

<a id="function-windows-executable-suffixes"></a>

### `_windows_executable_suffixes`

No function or method docstring is declared in the 0.7.5 source.

```python
def _windows_executable_suffixes() -> set[str]
```

**Catalog symbol:** `x86decomp_testkit.adapters.detection:_windows_executable_suffixes`  
**Visibility:** internal  
**Source line:** 52

<a id="function-prefer-windows-executable"></a>

### `_prefer_windows_executable`

No function or method docstring is declared in the 0.7.5 source.

```python
def _prefer_windows_executable(candidates: list[Path]) -> Path | None
```

**Catalog symbol:** `x86decomp_testkit.adapters.detection:_prefer_windows_executable`  
**Visibility:** internal  
**Source line:** 56

<a id="function-candidate-from-root"></a>

### `_candidate_from_root`

No function or method docstring is declared in the 0.7.5 source.

```python
def _candidate_from_root(root: Path, spec: AdapterSpec) -> Path | None
```

**Catalog symbol:** `x86decomp_testkit.adapters.detection:_candidate_from_root`  
**Visibility:** internal  
**Source line:** 67

<a id="function-known-windows-msvc-roots"></a>

### `_known_windows_msvc_roots`

No function or method docstring is declared in the 0.7.5 source.

```python
def _known_windows_msvc_roots() -> list[Path]
```

**Catalog symbol:** `x86decomp_testkit.adapters.detection:_known_windows_msvc_roots`  
**Visibility:** internal  
**Source line:** 90

<a id="function-find-recursive"></a>

### `_find_recursive`

No function or method docstring is declared in the 0.7.5 source.

```python
def _find_recursive(root: Path, names: Iterable[str], max_depth: int=6) -> Path | None
```

**Catalog symbol:** `x86decomp_testkit.adapters.detection:_find_recursive`  
**Visibility:** internal  
**Source line:** 117

<a id="function-detect-adapter"></a>

### `detect_adapter`

No function or method docstring is declared in the 0.7.5 source.

```python
def detect_adapter(spec: AdapterSpec, config: TestConfig) -> ProbeResult
```

**Catalog symbol:** `x86decomp_testkit.adapters.detection:detect_adapter`  
**Visibility:** public  
**Source line:** 131

<a id="function-detect-all"></a>

### `detect_all`

No function or method docstring is declared in the 0.7.5 source.

```python
def detect_all(catalog: dict[str, AdapterSpec], config: TestConfig) -> list[ProbeResult]
```

**Catalog symbol:** `x86decomp_testkit.adapters.detection:detect_all`  
**Visibility:** public  
**Source line:** 248
