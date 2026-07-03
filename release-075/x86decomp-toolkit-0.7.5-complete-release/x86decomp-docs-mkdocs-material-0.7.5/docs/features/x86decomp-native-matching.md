---
title: x86decomp.native.matching
description: No module docstring is declared in the 0.7.5 source.
---

# `x86decomp.native.matching`

No module docstring is declared in the 0.7.5 source.

**Area:** Toolkit  
**Source:** `src/x86decomp/native/matching.py`  
**SHA-256:** `3d2d67bc09fd863ffb366310883c6869b10c04545e48edc75089b7317927478a`  
**Functions/methods:** 7

> Module names, signatures, line numbers, and docstrings are extracted directly from the source AST. No behavior is inferred when a docstring is absent.

## Functions and methods

<a id="function-rva-to-file-offset"></a>

### `rva_to_file_offset`

No function or method docstring is declared in the 0.7.5 source.

```python
def rva_to_file_offset(image: Any, rva: int) -> int
```

**Catalog symbol:** `x86decomp.native.matching:rva_to_file_offset`  
**Visibility:** public  
**Source line:** 16

<a id="function-extract-candidate"></a>

### `extract_candidate`

No function or method docstring is declared in the 0.7.5 source.

```python
def extract_candidate(path: Path, *, symbol: str | None=None, size: int | None=None) -> bytes
```

**Catalog symbol:** `x86decomp.native.matching:extract_candidate`  
**Visibility:** public  
**Source line:** 26

<a id="function-compare-function-bytes"></a>

### `compare_function_bytes`

No function or method docstring is declared in the 0.7.5 source.

```python
def compare_function_bytes(original: bytes, candidate: bytes, *, policy: str='exact', pad_bytes: Iterable[int]=DEFAULT_PAD_BYTES, protected_offsets: Iterable[int]=()) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.native.matching:compare_function_bytes`  
**Visibility:** public  
**Source line:** 34

<a id="function-functionmatching-init"></a>

### `FunctionMatching.__init__`

No function or method docstring is declared in the 0.7.5 source.

```python
def FunctionMatching.__init__(self, store: NativeStore)
```

**Catalog symbol:** `x86decomp.native.matching:FunctionMatching.__init__`  
**Visibility:** internal  
**Source line:** 79

<a id="function-functionmatching-batch"></a>

### `FunctionMatching.batch`

No function or method docstring is declared in the 0.7.5 source.

```python
def FunctionMatching.batch(self, original_path: Path, candidates: Iterable[dict[str, Any]], *, policy: str='trailing-padding', pad_bytes: Iterable[int]=DEFAULT_PAD_BYTES, actor: str='analyst') -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.native.matching:FunctionMatching.batch`  
**Visibility:** public  
**Source line:** 82

<a id="function-functionmatching-report"></a>

### `FunctionMatching.report`

No function or method docstring is declared in the 0.7.5 source.

```python
def FunctionMatching.report(self, run_id: str) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.native.matching:FunctionMatching.report`  
**Visibility:** public  
**Source line:** 147

<a id="function-functionmatching-mismatches"></a>

### `FunctionMatching.mismatches`

No function or method docstring is declared in the 0.7.5 source.

```python
def FunctionMatching.mismatches(self, run_id: str) -> list[dict[str, Any]]
```

**Catalog symbol:** `x86decomp.native.matching:FunctionMatching.mismatches`  
**Visibility:** public  
**Source line:** 157
