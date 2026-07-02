---
title: x86decomp.cpp_recovery
description: Bounded C++ relationship recovery from MSVC metadata and code patterns.
original_path: features/x86decomp-cpp-recovery.html
---

<a id="function-function-prefix"></a>
<a id="function-adjustor-thunk-candidate"></a>
<a id="function-recover-cpp-model"></a>

Section: Source-derived feature and function reference

# x86decomp.cpp_recovery

Bounded C++ relationship recovery from MSVC metadata and code patterns.

Metadata: core · current · 3 functions/methods

**Source:** `src/x86decomp/cpp_recovery.py`

> **Truth basis.** Module and symbol names, signatures, line numbers, docstrings, and SHA-256 are read directly from the sealed source. When source docstrings are absent, this page says so instead of inferring behavior. Source SHA-256: `c1f07b15f8649be4235cb56bb2e8f953ed31211b98311633d6beccde38dce8fa`.

## Functions and methods

Metadata: internal · line 19

### _function_prefix

No function or method docstring is declared in the v0.7.4 source.

```
def _function_prefix(view: PEView, rva: int, size: int = 24) -> bytes
```

**Catalog symbol:** `x86decomp.cpp_recovery:_function_prefix`

Metadata: internal · line 28

### _adjustor_thunk_candidate

No function or method docstring is declared in the v0.7.4 source.

```
def _adjustor_thunk_candidate(view: PEView, rva: int) -> dict[str, Any] | None
```

**Catalog symbol:** `x86decomp.cpp_recovery:_adjustor_thunk_candidate`

Metadata: public · line 55

### recover_cpp_model

No function or method docstring is declared in the v0.7.4 source.

```
def recover_cpp_model(pe_path: Path, *, metadata_report: Path | None = None, object_paths: list[Path] | None = None, map_path: Path | None = None, report_path: Path | None = None) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.cpp_recovery:recover_cpp_model`
