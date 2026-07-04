---
title: x86decomp.assembly.relocations
description: No module docstring is declared in the 0.7.5 source.
---

# `x86decomp.assembly.relocations`

No module docstring is declared in the 0.7.5 source.

**Area:** Toolkit  
**Source:** `src/x86decomp/assembly/relocations.py`  
**SHA-256:** `d9c90ac5d66b3a36560ef8d9539bbef0d2e184574912609d27c7848d4f40666d`  
**Functions/methods:** 11

> Module names, signatures, line numbers, and docstrings are extracted directly from the source AST. No behavior is inferred when a docstring is absent.

## Functions and methods

<a id="function-symboladdress-safe-name"></a>

### `SymbolAddress.safe_name`

No function or method docstring is declared in the 0.7.5 source.

```python
def SymbolAddress.safe_name(self) -> str
```

**Catalog symbol:** `x86decomp.assembly.relocations:SymbolAddress.safe_name`  
**Visibility:** public  
**Source line:** 32

<a id="function-symboladdress-to-dict"></a>

### `SymbolAddress.to_dict`

No function or method docstring is declared in the 0.7.5 source.

```python
def SymbolAddress.to_dict(self) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.assembly.relocations:SymbolAddress.to_dict`  
**Visibility:** public  
**Source line:** 35

<a id="function-normalize-symbol-map"></a>

### `normalize_symbol_map`

No function or method docstring is declared in the 0.7.5 source.

```python
def normalize_symbol_map(raw: Mapping[str, Any] | list[Mapping[str, Any]]) -> dict[str, SymbolAddress]
```

**Catalog symbol:** `x86decomp.assembly.relocations:normalize_symbol_map`  
**Visibility:** public  
**Source line:** 45

<a id="function-supported-relocations"></a>

### `supported_relocations`

No function or method docstring is declared in the 0.7.5 source.

```python
def supported_relocations() -> dict[str, list[str]]
```

**Catalog symbol:** `x86decomp.assembly.relocations:supported_relocations`  
**Visibility:** public  
**Source line:** 95

<a id="function-read-addend"></a>

### `_read_addend`

No function or method docstring is declared in the 0.7.5 source.

```python
def _read_addend(data: bytes, offset: int, width: int, *, signed: bool) -> int
```

**Catalog symbol:** `x86decomp.assembly.relocations:_read_addend`  
**Visibility:** internal  
**Source line:** 115

<a id="function-write-value"></a>

### `_write_value`

No function or method docstring is declared in the 0.7.5 source.

```python
def _write_value(buffer: bytearray, offset: int, width: int, value: int, *, signed: bool) -> None
```

**Catalog symbol:** `x86decomp.assembly.relocations:_write_value`  
**Visibility:** internal  
**Source line:** 121

<a id="function-object-symbol-target"></a>

### `_object_symbol_target`

No function or method docstring is declared in the 0.7.5 source.

```python
def _object_symbol_target(obj: CoffObject, symbol: CoffSymbol | None, *, extracted: ExtractedSymbol, base_rva: int, placements: Mapping[int | str, int]) -> tuple[int, int | None, int | None] | None
```

**Catalog symbol:** `x86decomp.assembly.relocations:_object_symbol_target`  
**Visibility:** internal  
**Source line:** 131

<a id="function-resolve-target"></a>

### `_resolve_target`

No function or method docstring is declared in the 0.7.5 source.

```python
def _resolve_target(obj: CoffObject, relocation: CoffRelocation, *, extracted: ExtractedSymbol, base_rva: int, symbol_map: Mapping[str, SymbolAddress], placements: Mapping[int | str, int]) -> tuple[str | None, int | None, int | None, int | None]
```

**Catalog symbol:** `x86decomp.assembly.relocations:_resolve_target`  
**Visibility:** internal  
**Source line:** 152

<a id="function-compute-value"></a>

### `_compute_value`

No function or method docstring is declared in the 0.7.5 source.

```python
def _compute_value(*, machine: int, relocation_type: int, target_rva: int, field_rva: int, addend: int, image_base: int, target_section_rva: int | None, target_section_index: int | None) -> tuple[int, bool]
```

**Catalog symbol:** `x86decomp.assembly.relocations:_compute_value`  
**Visibility:** internal  
**Source line:** 177

<a id="function-relocationresolver-inspect"></a>

### `RelocationResolver.inspect`

No function or method docstring is declared in the 0.7.5 source.

```python
def RelocationResolver.inspect(self, object_path: Path, *, symbol: str | None=None) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.assembly.relocations:RelocationResolver.inspect`  
**Visibility:** public  
**Source line:** 237

<a id="function-relocationresolver-resolve"></a>

### `RelocationResolver.resolve`

No function or method docstring is declared in the 0.7.5 source.

```python
def RelocationResolver.resolve(self, object_path: Path, *, symbol: str, base_rva: int, symbol_map: Mapping[str, Any] | list[Mapping[str, Any]], image_base: int=0, section_placements: Mapping[int | str, int] | None=None, output_path: Path | None=None, expected_bytes: bytes | None=None) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.assembly.relocations:RelocationResolver.resolve`  
**Visibility:** public  
**Source line:** 257
