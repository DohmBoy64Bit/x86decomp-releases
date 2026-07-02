---
title: x86decomp.native.matching
description: No module docstring is declared in the v0.7.4 source.
original_path: features/x86decomp-native-matching.html
---

<a id="function-rva-to-file-offset"></a>
<a id="function-extract-candidate"></a>
<a id="function-compare-function-bytes"></a>
<a id="function-functionmatching-init"></a>
<a id="function-functionmatching-batch"></a>
<a id="function-functionmatching-report"></a>
<a id="function-functionmatching-mismatches"></a>

Section: Source-derived feature and function reference

# x86decomp.native.matching

No module docstring is declared in the v0.7.4 source.

Metadata: native · current · 7 functions/methods

**Source:** `src/x86decomp/native/matching.py`

> **Truth basis.** Module and symbol names, signatures, line numbers, docstrings, and SHA-256 are read directly from the sealed source. When source docstrings are absent, this page says so instead of inferring behavior. Source SHA-256: `3d2d67bc09fd863ffb366310883c6869b10c04545e48edc75089b7317927478a`.

## Functions and methods

Metadata: public · line 16

### rva_to_file_offset

No function or method docstring is declared in the v0.7.4 source.

```
def rva_to_file_offset(image: Any, rva: int) -> int
```

**Catalog symbol:** `x86decomp.native.matching:rva_to_file_offset`

Metadata: public · line 26

### extract_candidate

No function or method docstring is declared in the v0.7.4 source.

```
def extract_candidate(path: Path, *, symbol: str | None = None, size: int | None = None) -> bytes
```

**Catalog symbol:** `x86decomp.native.matching:extract_candidate`

Metadata: public · line 34

### compare_function_bytes

No function or method docstring is declared in the v0.7.4 source.

```
def compare_function_bytes(original: bytes, candidate: bytes, *, policy: str = 'exact', pad_bytes: Iterable[int] = DEFAULT_PAD_BYTES, protected_offsets: Iterable[int] = ()) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.native.matching:compare_function_bytes`

Metadata: internal · line 79

### FunctionMatching.__init__

No function or method docstring is declared in the v0.7.4 source.

```
def __init__(self, store: NativeStore)
```

**Catalog symbol:** `x86decomp.native.matching:FunctionMatching.__init__`

Metadata: public · line 82

### FunctionMatching.batch

No function or method docstring is declared in the v0.7.4 source.

```
def batch(self, original_path: Path, candidates: Iterable[dict[str, Any]], *, policy: str = 'trailing-padding', pad_bytes: Iterable[int] = DEFAULT_PAD_BYTES, actor: str = 'analyst') -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.native.matching:FunctionMatching.batch`

Metadata: public · line 147

### FunctionMatching.report

No function or method docstring is declared in the v0.7.4 source.

```
def report(self, run_id: str) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.native.matching:FunctionMatching.report`

Metadata: public · line 157

### FunctionMatching.mismatches

No function or method docstring is declared in the v0.7.4 source.

```
def mismatches(self, run_id: str) -> list[dict[str, Any]]
```

**Catalog symbol:** `x86decomp.native.matching:FunctionMatching.mismatches`
