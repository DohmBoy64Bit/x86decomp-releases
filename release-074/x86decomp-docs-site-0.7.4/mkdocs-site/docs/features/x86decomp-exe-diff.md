---
title: x86decomp.exe_diff
description: Executable-function versus COFF-symbol comparison for matching mode.
original_path: features/x86decomp-exe-diff.html
---

<a id="function-rva-to-file-offset"></a>
<a id="function-extract-pe-bytes"></a>
<a id="function-masked-copy"></a>
<a id="function-candidate-relocation-masks"></a>
<a id="function-pe-base-relocation-masks"></a>
<a id="function-compare-pe-function-to-coff-symbol"></a>

Section: Source-derived feature and function reference

# x86decomp.exe_diff

Executable-function versus COFF-symbol comparison for matching mode.

Metadata: core · current · 6 functions/methods

**Source:** `src/x86decomp/exe_diff.py`

> **Truth basis.** Module and symbol names, signatures, line numbers, docstrings, and SHA-256 are read directly from the sealed source. When source docstrings are absent, this page says so instead of inferring behavior. Source SHA-256: `997ffacbd833a3bb4c0545d1fb1981469e1d575680f4b39b7e6f34a4796abdf0`.

## Functions and methods

Metadata: public · line 16

### rva_to_file_offset

No function or method docstring is declared in the v0.7.4 source.

```
def rva_to_file_offset(image: Any, rva: int) -> int
```

**Catalog symbol:** `x86decomp.exe_diff:rva_to_file_offset`

Metadata: public · line 32

### extract_pe_bytes

No function or method docstring is declared in the v0.7.4 source.

```
def extract_pe_bytes(path: Path, *, rva: int, size: int) -> tuple[Any, bytes]
```

**Catalog symbol:** `x86decomp.exe_diff:extract_pe_bytes`

Metadata: internal · line 49

### _masked_copy

No function or method docstring is declared in the v0.7.4 source.

```
def _masked_copy(data: bytes, masks: list[tuple[int, int, str]]) -> bytes
```

**Catalog symbol:** `x86decomp.exe_diff:_masked_copy`

Metadata: internal · line 58

### _candidate_relocation_masks

No function or method docstring is declared in the v0.7.4 source.

```
def _candidate_relocation_masks(relocations: tuple[CoffRelocation, ...], machine: int) -> list[tuple[int, int, str]]
```

**Catalog symbol:** `x86decomp.exe_diff:_candidate_relocation_masks`

Metadata: internal · line 74

### _pe_base_relocation_masks

No function or method docstring is declared in the v0.7.4 source.

```
def _pe_base_relocation_masks(image: Any, *, function_rva: int, size: int) -> list[tuple[int, int, str]]
```

**Catalog symbol:** `x86decomp.exe_diff:_pe_base_relocation_masks`

Metadata: public · line 84

### compare_pe_function_to_coff_symbol

No function or method docstring is declared in the v0.7.4 source.

```
def compare_pe_function_to_coff_symbol(*, pe_path: Path, function_rva: int, function_size: int, coff_path: Path, symbol_name: str, report_path: Path | None = None) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.exe_diff:compare_pe_function_to_coff_symbol`
