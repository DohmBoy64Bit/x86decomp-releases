---
title: x86decomp.patching
description: Patch-image backend with integrity checks and PE checksum refresh.
original_path: features/x86decomp-patching.html
---

<a id="function-checksum-offset"></a>
<a id="function-calculate-pe-checksum"></a>
<a id="function-patch-pe-function"></a>

Section: Source-derived feature and function reference

# x86decomp.patching

Patch-image backend with integrity checks and PE checksum refresh.

Metadata: core · current · 3 functions/methods

**Source:** `src/x86decomp/patching.py`

> **Truth basis.** Module and symbol names, signatures, line numbers, docstrings, and SHA-256 are read directly from the sealed source. When source docstrings are absent, this page says so instead of inferring behavior. Source SHA-256: `61b9d802fc2c9c89f06877876f72efb7fc16d3a1fb283dddfd561dfd4fe61741`.

## Functions and methods

Metadata: internal · line 15

### _checksum_offset

No function or method docstring is declared in the v0.7.4 source.

```
def _checksum_offset(data: bytes) -> int
```

**Catalog symbol:** `x86decomp.patching:_checksum_offset`

Metadata: public · line 24

### calculate_pe_checksum

No function or method docstring is declared in the v0.7.4 source.

```
def calculate_pe_checksum(data: bytes, checksum_offset: int) -> int
```

**Catalog symbol:** `x86decomp.patching:calculate_pe_checksum`

Metadata: public · line 39

### patch_pe_function

No function or method docstring is declared in the v0.7.4 source.

```
def patch_pe_function(original_path: Path, candidate_path: Path, output_path: Path, *, function_rva: int, expected_original_sha256: str | None = None, expected_function_sha256: str | None = None, report_path: Path | None = None) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.patching:patch_pe_function`
