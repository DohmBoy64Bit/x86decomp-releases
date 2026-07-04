---
title: x86decomp.patching
description: Patch-image backend with integrity checks and PE checksum refresh.
---

# `x86decomp.patching`

Patch-image backend with integrity checks and PE checksum refresh.

**Area:** Toolkit  
**Source:** `src/x86decomp/patching.py`  
**SHA-256:** `61b9d802fc2c9c89f06877876f72efb7fc16d3a1fb283dddfd561dfd4fe61741`  
**Functions/methods:** 3

> Module names, signatures, line numbers, and docstrings are extracted directly from the source AST. No behavior is inferred when a docstring is absent.

## Functions and methods

<a id="function-checksum-offset"></a>

### `_checksum_offset`

No function or method docstring is declared in the 0.7.5 source.

```python
def _checksum_offset(data: bytes) -> int
```

**Catalog symbol:** `x86decomp.patching:_checksum_offset`  
**Visibility:** internal  
**Source line:** 15

<a id="function-calculate-pe-checksum"></a>

### `calculate_pe_checksum`

No function or method docstring is declared in the 0.7.5 source.

```python
def calculate_pe_checksum(data: bytes, checksum_offset: int) -> int
```

**Catalog symbol:** `x86decomp.patching:calculate_pe_checksum`  
**Visibility:** public  
**Source line:** 24

<a id="function-patch-pe-function"></a>

### `patch_pe_function`

No function or method docstring is declared in the 0.7.5 source.

```python
def patch_pe_function(original_path: Path, candidate_path: Path, output_path: Path, *, function_rva: int, expected_original_sha256: str | None=None, expected_function_sha256: str | None=None, report_path: Path | None=None) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.patching:patch_pe_function`  
**Visibility:** public  
**Source line:** 39
