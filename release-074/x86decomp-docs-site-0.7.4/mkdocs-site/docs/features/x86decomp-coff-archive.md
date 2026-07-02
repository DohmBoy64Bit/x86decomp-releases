---
title: x86decomp.coff_archive
description: Bounded Microsoft/Unix COFF archive (``.lib``/``.a``) inspection.
original_path: features/x86decomp-coff-archive.html
---

<a id="function-archivemember-to-dict"></a>
<a id="function-coffarchive-to-dict"></a>
<a id="function-decimal"></a>
<a id="function-octal"></a>
<a id="function-long-name"></a>
<a id="function-parse-import-object"></a>
<a id="function-cstring-sequence"></a>
<a id="function-first-linker-symbols"></a>
<a id="function-second-linker-symbols"></a>
<a id="function-parse-coff-archive-bytes"></a>
<a id="function-parse-coff-archive"></a>

Section: Source-derived feature and function reference

# x86decomp.coff_archive

Bounded Microsoft/Unix COFF archive (``.lib``/``.a``) inspection.

Metadata: core · current · 11 functions/methods

**Source:** `src/x86decomp/coff_archive.py`

> **Truth basis.** Module and symbol names, signatures, line numbers, docstrings, and SHA-256 are read directly from the sealed source. When source docstrings are absent, this page says so instead of inferring behavior. Source SHA-256: `51cdfa71d8876054203d3f487c37ee12ece57e831abc8bca35e57112d4089584`.

## Functions and methods

Metadata: public · line 42

### ArchiveMember.to_dict

No function or method docstring is declared in the v0.7.4 source.

```
def to_dict(self) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.coff_archive:ArchiveMember.to_dict`

Metadata: public · line 70

### CoffArchive.to_dict

No function or method docstring is declared in the v0.7.4 source.

```
def to_dict(self) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.coff_archive:CoffArchive.to_dict`

Metadata: internal · line 82

### _decimal

No function or method docstring is declared in the v0.7.4 source.

```
def _decimal(field: bytes, context: str, *, optional: bool = True) -> int | None
```

**Catalog symbol:** `x86decomp.coff_archive:_decimal`

Metadata: internal · line 92

### _octal

No function or method docstring is declared in the v0.7.4 source.

```
def _octal(field: bytes, context: str) -> int | None
```

**Catalog symbol:** `x86decomp.coff_archive:_octal`

Metadata: internal · line 102

### _long_name

No function or method docstring is declared in the v0.7.4 source.

```
def _long_name(table: bytes, offset: int) -> str
```

**Catalog symbol:** `x86decomp.coff_archive:_long_name`

Metadata: internal · line 110

### _parse_import_object

No function or method docstring is declared in the v0.7.4 source.

```
def _parse_import_object(data: bytes) -> dict[str, Any] | None
```

**Catalog symbol:** `x86decomp.coff_archive:_parse_import_object`

Metadata: internal · line 147

### _cstring_sequence

No function or method docstring is declared in the v0.7.4 source.

```
def _cstring_sequence(data: bytes, offset: int, count: int) -> tuple[list[str], int]
```

**Catalog symbol:** `x86decomp.coff_archive:_cstring_sequence`

Metadata: internal · line 161

### _first_linker_symbols

No function or method docstring is declared in the v0.7.4 source.

```
def _first_linker_symbols(data: bytes) -> list[tuple[str, int]] | None
```

**Catalog symbol:** `x86decomp.coff_archive:_first_linker_symbols`

Metadata: internal · line 175

### _second_linker_symbols

No function or method docstring is declared in the v0.7.4 source.

```
def _second_linker_symbols(data: bytes) -> list[tuple[str, int]] | None
```

**Catalog symbol:** `x86decomp.coff_archive:_second_linker_symbols`

Metadata: public · line 202

### parse_coff_archive_bytes

No function or method docstring is declared in the v0.7.4 source.

```
def parse_coff_archive_bytes(data: bytes, *, path: Path | None = None) -> CoffArchive
```

**Catalog symbol:** `x86decomp.coff_archive:parse_coff_archive_bytes`

Metadata: public · line 314

### parse_coff_archive

No function or method docstring is declared in the v0.7.4 source.

```
def parse_coff_archive(path: Path) -> CoffArchive
```

**Catalog symbol:** `x86decomp.coff_archive:parse_coff_archive`
