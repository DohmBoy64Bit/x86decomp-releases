---
title: x86decomp.linker_layout
description: MSVC linker-map parsing and object contribution layout reconstruction.
---

# `x86decomp.linker_layout`

MSVC linker-map parsing and object contribution layout reconstruction.

The parser accepts the text format emitted by LINK.EXE ``/MAP`` and LLD's
MSVC-compatible map writer.  It records segment groups, public symbols, object
contributions, preferred load address, and entry point.  Reconstruction is
explicitly evidence driven: a map file and actual COFF objects are required for
claims about original object ordering.

**Area:** Toolkit  
**Source:** `src/x86decomp/linker_layout.py`  
**SHA-256:** `e212e73f09b9559f17e0251eba8260a50b52931091a4972a2deabc462cd68682`  
**Functions/methods:** 8

> Module names, signatures, line numbers, and docstrings are extracted directly from the source AST. No behavior is inferred when a docstring is absent.

## Functions and methods

<a id="function-mapsegment-to-dict"></a>

### `MapSegment.to_dict`

No function or method docstring is declared in the 0.7.5 source.

```python
def MapSegment.to_dict(self) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.linker_layout:MapSegment.to_dict`  
**Visibility:** public  
**Source line:** 42

<a id="function-mapcontribution-to-dict"></a>

### `MapContribution.to_dict`

No function or method docstring is declared in the 0.7.5 source.

```python
def MapContribution.to_dict(self) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.linker_layout:MapContribution.to_dict`  
**Visibility:** public  
**Source line:** 59

<a id="function-mappublic-to-dict"></a>

### `MapPublic.to_dict`

No function or method docstring is declared in the 0.7.5 source.

```python
def MapPublic.to_dict(self) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.linker_layout:MapPublic.to_dict`  
**Visibility:** public  
**Source line:** 77

<a id="function-linkermap-to-dict"></a>

### `LinkerMap.to_dict`

No function or method docstring is declared in the 0.7.5 source.

```python
def LinkerMap.to_dict(self) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.linker_layout:LinkerMap.to_dict`  
**Visibility:** public  
**Source line:** 100

<a id="function-parse-msvc-map-text"></a>

### `parse_msvc_map_text`

No function or method docstring is declared in the 0.7.5 source.

```python
def parse_msvc_map_text(text: str, *, path: Path | None=None) -> LinkerMap
```

**Catalog symbol:** `x86decomp.linker_layout:parse_msvc_map_text`  
**Visibility:** public  
**Source line:** 118

<a id="function-parse-msvc-map"></a>

### `parse_msvc_map`

No function or method docstring is declared in the 0.7.5 source.

```python
def parse_msvc_map(path: Path) -> LinkerMap
```

**Catalog symbol:** `x86decomp.linker_layout:parse_msvc_map`  
**Visibility:** public  
**Source line:** 215

<a id="function-normalize-object-key"></a>

### `_normalize_object_key`

No function or method docstring is declared in the 0.7.5 source.

```python
def _normalize_object_key(value: str) -> str
```

**Catalog symbol:** `x86decomp.linker_layout:_normalize_object_key`  
**Visibility:** internal  
**Source line:** 222

<a id="function-reconstruct-linker-layout"></a>

### `reconstruct_linker_layout`

No function or method docstring is declared in the 0.7.5 source.

```python
def reconstruct_linker_layout(pe_path: Path, map_path: Path, *, object_paths: Iterable[Path]=(), report_path: Path | None=None) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.linker_layout:reconstruct_linker_layout`  
**Visibility:** public  
**Source line:** 229
