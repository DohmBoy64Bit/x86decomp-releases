---
title: x86decomp.exe_diff
description: Executable-function versus COFF-symbol comparison for matching mode.
---

# `x86decomp.exe_diff`

Executable-function versus COFF-symbol comparison for matching mode.

**Area:** Toolkit  
**Source:** `src/x86decomp/exe_diff.py`  
**SHA-256:** `997ffacbd833a3bb4c0545d1fb1981469e1d575680f4b39b7e6f34a4796abdf0`  
**Functions/methods:** 6

> Module names, signatures, line numbers, and docstrings are extracted directly from the source AST. No behavior is inferred when a docstring is absent.

## Functions and methods

<a id="function-rva-to-file-offset"></a>

### `rva_to_file_offset`

No function or method docstring is declared in the 0.7.5 source.

```python
def rva_to_file_offset(image: Any, rva: int) -> int
```

**Catalog symbol:** `x86decomp.exe_diff:rva_to_file_offset`  
**Visibility:** public  
**Source line:** 16

<a id="function-extract-pe-bytes"></a>

### `extract_pe_bytes`

No function or method docstring is declared in the 0.7.5 source.

```python
def extract_pe_bytes(path: Path, *, rva: int, size: int) -> tuple[Any, bytes]
```

**Catalog symbol:** `x86decomp.exe_diff:extract_pe_bytes`  
**Visibility:** public  
**Source line:** 32

<a id="function-masked-copy"></a>

### `_masked_copy`

No function or method docstring is declared in the 0.7.5 source.

```python
def _masked_copy(data: bytes, masks: list[tuple[int, int, str]]) -> bytes
```

**Catalog symbol:** `x86decomp.exe_diff:_masked_copy`  
**Visibility:** internal  
**Source line:** 49

<a id="function-candidate-relocation-masks"></a>

### `_candidate_relocation_masks`

No function or method docstring is declared in the 0.7.5 source.

```python
def _candidate_relocation_masks(relocations: tuple[CoffRelocation, ...], machine: int) -> list[tuple[int, int, str]]
```

**Catalog symbol:** `x86decomp.exe_diff:_candidate_relocation_masks`  
**Visibility:** internal  
**Source line:** 58

<a id="function-pe-base-relocation-masks"></a>

### `_pe_base_relocation_masks`

No function or method docstring is declared in the 0.7.5 source.

```python
def _pe_base_relocation_masks(image: Any, *, function_rva: int, size: int) -> list[tuple[int, int, str]]
```

**Catalog symbol:** `x86decomp.exe_diff:_pe_base_relocation_masks`  
**Visibility:** internal  
**Source line:** 74

<a id="function-compare-pe-function-to-coff-symbol"></a>

### `compare_pe_function_to_coff_symbol`

No function or method docstring is declared in the 0.7.5 source.

```python
def compare_pe_function_to_coff_symbol(*, pe_path: Path, function_rva: int, function_size: int, coff_path: Path, symbol_name: str, report_path: Path | None=None) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.exe_diff:compare_pe_function_to_coff_symbol`  
**Visibility:** public  
**Source line:** 84
