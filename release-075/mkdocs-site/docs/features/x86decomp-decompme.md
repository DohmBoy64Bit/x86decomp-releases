---
title: x86decomp.decompme
description: Create local decomp.me-style function packets without uploading data.
---

# `x86decomp.decompme`

Create local decomp.me-style function packets without uploading data.

**Area:** Toolkit  
**Source:** `src/x86decomp/decompme.py`  
**SHA-256:** `440f011b1a60d6a9549cd558927a158ce34f1377f699a58b922c696619172fe2`  
**Functions/methods:** 2

> Module names, signatures, line numbers, and docstrings are extracted directly from the source AST. No behavior is inferred when a docstring is absent.

## Functions and methods

<a id="function-copy-required"></a>

### `_copy_required`

No function or method docstring is declared in the 0.7.5 source.

```python
def _copy_required(source: Path, destination: Path, name: str) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.decompme:_copy_required`  
**Visibility:** internal  
**Source line:** 14

<a id="function-create-decompme-packet"></a>

### `create_decompme_packet`

Build a local, reviewable function packet.

The packet intentionally does not contact decomp.me. Ghidra's human-readable
listing is retained as source material and is labeled non-canonical because
decomp.me/compiler syntax may require target-specific conversion.

```python
def create_decompme_packet(function_artifact: Path, output_directory: Path, *, overwrite: bool=False) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.decompme:create_decompme_packet`  
**Visibility:** public  
**Source line:** 23
