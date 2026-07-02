---
title: x86decomp.assembly.relocations
description: No module docstring is declared in the v0.7.4 source.
original_path: features/x86decomp-assembly-relocations.html
---

<a id="function-symboladdress-safe-name"></a>
<a id="function-symboladdress-to-dict"></a>
<a id="function-normalize-symbol-map"></a>
<a id="function-supported-relocations"></a>
<a id="function-read-addend"></a>
<a id="function-write-value"></a>
<a id="function-object-symbol-target"></a>
<a id="function-resolve-target"></a>
<a id="function-compute-value"></a>
<a id="function-relocationresolver-inspect"></a>
<a id="function-relocationresolver-resolve"></a>

Section: Source-derived feature and function reference

# x86decomp.assembly.relocations

No module docstring is declared in the v0.7.4 source.

Metadata: assembly · current · 11 functions/methods

**Source:** `src/x86decomp/assembly/relocations.py`

> **Truth basis.** Module and symbol names, signatures, line numbers, docstrings, and SHA-256 are read directly from the sealed source. When source docstrings are absent, this page says so instead of inferring behavior. Source SHA-256: `d9c90ac5d66b3a36560ef8d9539bbef0d2e184574912609d27c7848d4f40666d`.

## Functions and methods

Metadata: public · line 32

### SymbolAddress.safe_name

No function or method docstring is declared in the v0.7.4 source.

```
def safe_name(self) -> str
```

**Catalog symbol:** `x86decomp.assembly.relocations:SymbolAddress.safe_name`

Metadata: public · line 35

### SymbolAddress.to_dict

No function or method docstring is declared in the v0.7.4 source.

```
def to_dict(self) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.assembly.relocations:SymbolAddress.to_dict`

Metadata: public · line 45

### normalize_symbol_map

No function or method docstring is declared in the v0.7.4 source.

```
def normalize_symbol_map(raw: Mapping[str, Any] | list[Mapping[str, Any]]) -> dict[str, SymbolAddress]
```

**Catalog symbol:** `x86decomp.assembly.relocations:normalize_symbol_map`

Metadata: public · line 95

### supported_relocations

No function or method docstring is declared in the v0.7.4 source.

```
def supported_relocations() -> dict[str, list[str]]
```

**Catalog symbol:** `x86decomp.assembly.relocations:supported_relocations`

Metadata: internal · line 115

### _read_addend

No function or method docstring is declared in the v0.7.4 source.

```
def _read_addend(data: bytes, offset: int, width: int, *, signed: bool) -> int
```

**Catalog symbol:** `x86decomp.assembly.relocations:_read_addend`

Metadata: internal · line 121

### _write_value

No function or method docstring is declared in the v0.7.4 source.

```
def _write_value(buffer: bytearray, offset: int, width: int, value: int, *, signed: bool) -> None
```

**Catalog symbol:** `x86decomp.assembly.relocations:_write_value`

Metadata: internal · line 131

### _object_symbol_target

No function or method docstring is declared in the v0.7.4 source.

```
def _object_symbol_target(obj: CoffObject, symbol: CoffSymbol | None, *, extracted: ExtractedSymbol, base_rva: int, placements: Mapping[int | str, int]) -> tuple[int, int | None, int | None] | None
```

**Catalog symbol:** `x86decomp.assembly.relocations:_object_symbol_target`

Metadata: internal · line 152

### _resolve_target

No function or method docstring is declared in the v0.7.4 source.

```
def _resolve_target(obj: CoffObject, relocation: CoffRelocation, *, extracted: ExtractedSymbol, base_rva: int, symbol_map: Mapping[str, SymbolAddress], placements: Mapping[int | str, int]) -> tuple[str | None, int | None, int | None, int | None]
```

**Catalog symbol:** `x86decomp.assembly.relocations:_resolve_target`

Metadata: internal · line 177

### _compute_value

No function or method docstring is declared in the v0.7.4 source.

```
def _compute_value(*, machine: int, relocation_type: int, target_rva: int, field_rva: int, addend: int, image_base: int, target_section_rva: int | None, target_section_index: int | None) -> tuple[int, bool]
```

**Catalog symbol:** `x86decomp.assembly.relocations:_compute_value`

Metadata: public · line 237

### RelocationResolver.inspect

No function or method docstring is declared in the v0.7.4 source.

```
def inspect(self, object_path: Path, *, symbol: str | None = None) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.assembly.relocations:RelocationResolver.inspect`

Metadata: public · line 257

### RelocationResolver.resolve

No function or method docstring is declared in the v0.7.4 source.

```
def resolve(self, object_path: Path, *, symbol: str, base_rva: int, symbol_map: Mapping[str, Any] | list[Mapping[str, Any]], image_base: int = 0, section_placements: Mapping[int | str, int] | None = None, output_path: Path | None = None, expected_bytes: bytes | None = None) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.assembly.relocations:RelocationResolver.resolve`
