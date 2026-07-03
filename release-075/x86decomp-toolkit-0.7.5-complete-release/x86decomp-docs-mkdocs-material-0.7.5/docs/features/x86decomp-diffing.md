---
title: x86decomp.diffing
description: Exact byte comparison and transparent similarity reporting.
---

# `x86decomp.diffing`

Exact byte comparison and transparent similarity reporting.

**Area:** Toolkit  
**Source:** `src/x86decomp/diffing.py`  
**SHA-256:** `e981a093051ff6a0be9462256f6ea50c2784693c15b32df5144a1ca0374814e3`  
**Functions/methods:** 2

> Module names, signatures, line numbers, and docstrings are extracted directly from the source AST. No behavior is inferred when a docstring is absent.

## Functions and methods

<a id="function-compare-bytes"></a>

### `compare_bytes`

No function or method docstring is declared in the 0.7.5 source.

```python
def compare_bytes(target: bytes, candidate: bytes, *, max_mismatches: int=64) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.diffing:compare_bytes`  
**Visibility:** public  
**Source line:** 13

<a id="function-compare-files"></a>

### `compare_files`

No function or method docstring is declared in the 0.7.5 source.

```python
def compare_files(target_path: Path, candidate_path: Path, *, max_mismatches: int=64, report_path: Path | None=None) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.diffing:compare_files`  
**Visibility:** public  
**Source line:** 60
