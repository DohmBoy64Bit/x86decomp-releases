---
title: x86decomp.coff_archive
description: Bounded Microsoft/Unix COFF archive (``.lib``/``.a``) inspection.
---

# `x86decomp.coff_archive`

Bounded Microsoft/Unix COFF archive (``.lib``/``.a``) inspection.

The archive container format is shared with ``ar``. Microsoft libraries additionally
use linker members and import-object records. This module inventories members, resolves
long names, parses linker symbol indexes when structurally valid, recognizes import
objects, and invokes the normal COFF parser for embedded object members.

**Area:** Toolkit  
**Source:** `src/x86decomp/coff_archive.py`  
**SHA-256:** `51cdfa71d8876054203d3f487c37ee12ece57e831abc8bca35e57112d4089584`  
**Functions/methods:** 11

> Module names, signatures, line numbers, and docstrings are extracted directly from the source AST. No behavior is inferred when a docstring is absent.

## Functions and methods

<a id="function-archivemember-to-dict"></a>

### `ArchiveMember.to_dict`

No function or method docstring is declared in the 0.7.5 source.

```python
def ArchiveMember.to_dict(self) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.coff_archive:ArchiveMember.to_dict`  
**Visibility:** public  
**Source line:** 42

<a id="function-coffarchive-to-dict"></a>

### `CoffArchive.to_dict`

No function or method docstring is declared in the 0.7.5 source.

```python
def CoffArchive.to_dict(self) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.coff_archive:CoffArchive.to_dict`  
**Visibility:** public  
**Source line:** 70

<a id="function-decimal"></a>

### `_decimal`

No function or method docstring is declared in the 0.7.5 source.

```python
def _decimal(field: bytes, context: str, *, optional: bool=True) -> int | None
```

**Catalog symbol:** `x86decomp.coff_archive:_decimal`  
**Visibility:** internal  
**Source line:** 82

<a id="function-octal"></a>

### `_octal`

No function or method docstring is declared in the 0.7.5 source.

```python
def _octal(field: bytes, context: str) -> int | None
```

**Catalog symbol:** `x86decomp.coff_archive:_octal`  
**Visibility:** internal  
**Source line:** 92

<a id="function-long-name"></a>

### `_long_name`

No function or method docstring is declared in the 0.7.5 source.

```python
def _long_name(table: bytes, offset: int) -> str
```

**Catalog symbol:** `x86decomp.coff_archive:_long_name`  
**Visibility:** internal  
**Source line:** 102

<a id="function-parse-import-object"></a>

### `_parse_import_object`

No function or method docstring is declared in the 0.7.5 source.

```python
def _parse_import_object(data: bytes) -> dict[str, Any] | None
```

**Catalog symbol:** `x86decomp.coff_archive:_parse_import_object`  
**Visibility:** internal  
**Source line:** 110

<a id="function-cstring-sequence"></a>

### `_cstring_sequence`

No function or method docstring is declared in the 0.7.5 source.

```python
def _cstring_sequence(data: bytes, offset: int, count: int) -> tuple[list[str], int]
```

**Catalog symbol:** `x86decomp.coff_archive:_cstring_sequence`  
**Visibility:** internal  
**Source line:** 147

<a id="function-first-linker-symbols"></a>

### `_first_linker_symbols`

No function or method docstring is declared in the 0.7.5 source.

```python
def _first_linker_symbols(data: bytes) -> list[tuple[str, int]] | None
```

**Catalog symbol:** `x86decomp.coff_archive:_first_linker_symbols`  
**Visibility:** internal  
**Source line:** 161

<a id="function-second-linker-symbols"></a>

### `_second_linker_symbols`

No function or method docstring is declared in the 0.7.5 source.

```python
def _second_linker_symbols(data: bytes) -> list[tuple[str, int]] | None
```

**Catalog symbol:** `x86decomp.coff_archive:_second_linker_symbols`  
**Visibility:** internal  
**Source line:** 175

<a id="function-parse-coff-archive-bytes"></a>

### `parse_coff_archive_bytes`

No function or method docstring is declared in the 0.7.5 source.

```python
def parse_coff_archive_bytes(data: bytes, *, path: Path | None=None) -> CoffArchive
```

**Catalog symbol:** `x86decomp.coff_archive:parse_coff_archive_bytes`  
**Visibility:** public  
**Source line:** 202

<a id="function-parse-coff-archive"></a>

### `parse_coff_archive`

No function or method docstring is declared in the 0.7.5 source.

```python
def parse_coff_archive(path: Path) -> CoffArchive
```

**Catalog symbol:** `x86decomp.coff_archive:parse_coff_archive`  
**Visibility:** public  
**Source line:** 314
