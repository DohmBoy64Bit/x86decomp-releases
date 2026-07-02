---
title: x86decomp.diffing
description: Exact byte comparison and transparent similarity reporting.
original_path: features/x86decomp-diffing.html
---

<a id="function-compare-bytes"></a>
<a id="function-compare-files"></a>

Section: Source-derived feature and function reference

# x86decomp.diffing

Exact byte comparison and transparent similarity reporting.

Metadata: core · current · 2 functions/methods

**Source:** `src/x86decomp/diffing.py`

> **Truth basis.** Module and symbol names, signatures, line numbers, docstrings, and SHA-256 are read directly from the sealed source. When source docstrings are absent, this page says so instead of inferring behavior. Source SHA-256: `e981a093051ff6a0be9462256f6ea50c2784693c15b32df5144a1ca0374814e3`.

## Functions and methods

Metadata: public · line 13

### compare_bytes

No function or method docstring is declared in the v0.7.4 source.

```
def compare_bytes(target: bytes, candidate: bytes, *, max_mismatches: int = 64) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.diffing:compare_bytes`

Metadata: public · line 60

### compare_files

No function or method docstring is declared in the v0.7.4 source.

```
def compare_files(target_path: Path, candidate_path: Path, *, max_mismatches: int = 64, report_path: Path | None = None) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.diffing:compare_files`
