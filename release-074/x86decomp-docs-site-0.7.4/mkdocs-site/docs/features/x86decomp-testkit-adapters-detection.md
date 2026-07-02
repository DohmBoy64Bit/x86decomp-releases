---
title: x86decomp_testkit.adapters.detection
description: No module docstring is declared in the v0.7.4 source.
original_path: features/x86decomp-testkit-adapters-detection.html
---

<a id="function-module-version"></a>
<a id="function-run-version"></a>
<a id="function-windows-executable-suffixes"></a>
<a id="function-prefer-windows-executable"></a>
<a id="function-candidate-from-root"></a>
<a id="function-known-windows-msvc-roots"></a>
<a id="function-find-recursive"></a>
<a id="function-detect-adapter"></a>
<a id="function-detect-all"></a>

Section: Source-derived feature and function reference

# x86decomp_testkit.adapters.detection

No module docstring is declared in the v0.7.4 source.

Metadata: verification harness · current · 9 functions/methods

**Source:** `test-suite/src/x86decomp_testkit/adapters/detection.py`

> **Truth basis.** Module and symbol names, signatures, line numbers, docstrings, and SHA-256 are read directly from the sealed source. When source docstrings are absent, this page says so instead of inferring behavior. Source SHA-256: `31500b9b25721c7bf1e53eb59fa082003db73ca68315ab787e8f24df48e180aa`.

## Functions and methods

Metadata: internal · line 16

### _module_version

No function or method docstring is declared in the v0.7.4 source.

```
def _module_version(module_name: str) -> str | None
```

**Catalog symbol:** `x86decomp_testkit.adapters.detection:_module_version`

Metadata: internal · line 35

### _run_version

No function or method docstring is declared in the v0.7.4 source.

```
def _run_version(executable: Path, args: tuple[str, ...], timeout: int = 15) -> tuple[str | None, str | None]
```

**Catalog symbol:** `x86decomp_testkit.adapters.detection:_run_version`

Metadata: internal · line 52

### _windows_executable_suffixes

No function or method docstring is declared in the v0.7.4 source.

```
def _windows_executable_suffixes() -> set[str]
```

**Catalog symbol:** `x86decomp_testkit.adapters.detection:_windows_executable_suffixes`

Metadata: internal · line 56

### _prefer_windows_executable

No function or method docstring is declared in the v0.7.4 source.

```
def _prefer_windows_executable(candidates: list[Path]) -> Path | None
```

**Catalog symbol:** `x86decomp_testkit.adapters.detection:_prefer_windows_executable`

Metadata: internal · line 67

### _candidate_from_root

No function or method docstring is declared in the v0.7.4 source.

```
def _candidate_from_root(root: Path, spec: AdapterSpec) -> Path | None
```

**Catalog symbol:** `x86decomp_testkit.adapters.detection:_candidate_from_root`

Metadata: internal · line 88

### _known_windows_msvc_roots

No function or method docstring is declared in the v0.7.4 source.

```
def _known_windows_msvc_roots() -> list[Path]
```

**Catalog symbol:** `x86decomp_testkit.adapters.detection:_known_windows_msvc_roots`

Metadata: internal · line 115

### _find_recursive

No function or method docstring is declared in the v0.7.4 source.

```
def _find_recursive(root: Path, names: Iterable[str], max_depth: int = 6) -> Path | None
```

**Catalog symbol:** `x86decomp_testkit.adapters.detection:_find_recursive`

Metadata: public · line 129

### detect_adapter

No function or method docstring is declared in the v0.7.4 source.

```
def detect_adapter(spec: AdapterSpec, config: TestConfig) -> ProbeResult
```

**Catalog symbol:** `x86decomp_testkit.adapters.detection:detect_adapter`

Metadata: public · line 246

### detect_all

No function or method docstring is declared in the v0.7.4 source.

```
def detect_all(catalog: dict[str, AdapterSpec], config: TestConfig) -> list[ProbeResult]
```

**Catalog symbol:** `x86decomp_testkit.adapters.detection:detect_all`
