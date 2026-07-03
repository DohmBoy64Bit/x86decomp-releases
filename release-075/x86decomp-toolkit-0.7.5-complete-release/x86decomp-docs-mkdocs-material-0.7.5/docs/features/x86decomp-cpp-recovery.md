---
title: x86decomp.cpp_recovery
description: Bounded C++ relationship recovery from MSVC metadata and code patterns.
---

# `x86decomp.cpp_recovery`

Bounded C++ relationship recovery from MSVC metadata and code patterns.

The output distinguishes directly parsed metadata from derived candidates.  It
never claims original source declarations, access modifiers, or method names.

**Area:** Toolkit  
**Source:** `src/x86decomp/cpp_recovery.py`  
**SHA-256:** `c1f07b15f8649be4235cb56bb2e8f953ed31211b98311633d6beccde38dce8fa`  
**Functions/methods:** 3

> Module names, signatures, line numbers, and docstrings are extracted directly from the source AST. No behavior is inferred when a docstring is absent.

## Functions and methods

<a id="function-function-prefix"></a>

### `_function_prefix`

No function or method docstring is declared in the 0.7.5 source.

```python
def _function_prefix(view: PEView, rva: int, size: int=24) -> bytes
```

**Catalog symbol:** `x86decomp.cpp_recovery:_function_prefix`  
**Visibility:** internal  
**Source line:** 19

<a id="function-adjustor-thunk-candidate"></a>

### `_adjustor_thunk_candidate`

No function or method docstring is declared in the 0.7.5 source.

```python
def _adjustor_thunk_candidate(view: PEView, rva: int) -> dict[str, Any] | None
```

**Catalog symbol:** `x86decomp.cpp_recovery:_adjustor_thunk_candidate`  
**Visibility:** internal  
**Source line:** 28

<a id="function-recover-cpp-model"></a>

### `recover_cpp_model`

No function or method docstring is declared in the 0.7.5 source.

```python
def recover_cpp_model(pe_path: Path, *, metadata_report: Path | None=None, object_paths: list[Path] | None=None, map_path: Path | None=None, report_path: Path | None=None) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.cpp_recovery:recover_cpp_model`  
**Visibility:** public  
**Source line:** 55
