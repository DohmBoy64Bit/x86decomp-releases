---
title: x86decomp.relink
description: Manifest-driven full-image relink backend.
---

# `x86decomp.relink`

Manifest-driven full-image relink backend.

The backend performs a real linker invocation using user-supplied objects and a
linker profile. It does not claim to infer the original linker script or object
partitioning automatically.

**Area:** Toolkit  
**Source:** `src/x86decomp/relink.py`  
**SHA-256:** `d401db042d4cc8300ccd4babd28cea400dca824d187a7caf0a1f3ead407fb296`  
**Functions/methods:** 1

> Module names, signatures, line numbers, and docstrings are extracted directly from the source AST. No behavior is inferred when a docstring is absent.

## Functions and methods

<a id="function-run-full-relink"></a>

### `run_full_relink`

No function or method docstring is declared in the 0.7.5 source.

```python
def run_full_relink(manifest_path: Path, *, report_path: Path | None=None) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.relink:run_full_relink`  
**Visibility:** public  
**Source line:** 23
