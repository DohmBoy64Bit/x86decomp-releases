---
title: x86decomp.pe32
description: Strict, dependency-free parser for native x86 PE32 images.
original_path: features/x86decomp-pe32.html
---

<a id="function-datadirectory-to-dict"></a>
<a id="function-section-mapped-size"></a>
<a id="function-section-to-dict"></a>
<a id="function-importsymbol-to-dict"></a>
<a id="function-importlibrary-to-dict"></a>
<a id="function-exportsymbol-to-dict"></a>
<a id="function-baserelocation-to-dict"></a>
<a id="function-debugrecord-to-dict"></a>
<a id="function-tlsinfo-to-dict"></a>
<a id="function-resourceleaf-to-dict"></a>
<a id="function-delayimportlibrary-to-dict"></a>
<a id="function-loadconfiginfo-to-dict"></a>
<a id="function-pe32image-entry-va"></a>
<a id="function-pe32image-to-dict"></a>
<a id="function-reader-init"></a>
<a id="function-reader-require"></a>
<a id="function-reader-unpack"></a>
<a id="function-reader-u16"></a>
<a id="function-reader-u32"></a>
<a id="function-reader-u64"></a>
<a id="function-reader-c-string"></a>
<a id="function-rva-to-offset"></a>
<a id="function-directory"></a>
<a id="function-parse-imports"></a>
<a id="function-parse-exports"></a>
<a id="function-parse-relocations"></a>
<a id="function-parse-debug-records"></a>
<a id="function-parse-tls"></a>
<a id="function-parse-resources"></a>
<a id="function-parse-delay-imports"></a>
<a id="function-parse-load-config"></a>
<a id="function-parse-pe32"></a>

Section: Source-derived feature and function reference

# x86decomp.pe32

Strict, dependency-free parser for native x86 PE32 images.

Metadata: core · current · 32 functions/methods

**Source:** `src/x86decomp/pe32.py`

> **Truth basis.** Module and symbol names, signatures, line numbers, docstrings, and SHA-256 are read directly from the sealed source. When source docstrings are absent, this page says so instead of inferring behavior. Source SHA-256: `746651d78b0b8401565dd22e99f73c8c902b13400fd80094d4675ab52c8c4be5`.

## Functions and methods

Metadata: public · line 47

### DataDirectory.to_dict

No function or method docstring is declared in the v0.7.4 source.

```
def to_dict(self) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.pe32:DataDirectory.to_dict`

Metadata: public · line 62

### Section.mapped_size

No function or method docstring is declared in the v0.7.4 source.

```
def mapped_size(self) -> int
```

**Catalog symbol:** `x86decomp.pe32:Section.mapped_size`

Metadata: public · line 65

### Section.to_dict

No function or method docstring is declared in the v0.7.4 source.

```
def to_dict(self) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.pe32:Section.to_dict`

Metadata: public · line 87

### ImportSymbol.to_dict

No function or method docstring is declared in the v0.7.4 source.

```
def to_dict(self) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.pe32:ImportSymbol.to_dict`

Metadata: public · line 102

### ImportLibrary.to_dict

No function or method docstring is declared in the v0.7.4 source.

```
def to_dict(self) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.pe32:ImportLibrary.to_dict`

Metadata: public · line 113

### ExportSymbol.to_dict

No function or method docstring is declared in the v0.7.4 source.

```
def to_dict(self) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.pe32:ExportSymbol.to_dict`

Metadata: public · line 128

### BaseRelocation.to_dict

No function or method docstring is declared in the v0.7.4 source.

```
def to_dict(self) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.pe32:BaseRelocation.to_dict`

Metadata: public · line 143

### DebugRecord.to_dict

No function or method docstring is declared in the v0.7.4 source.

```
def to_dict(self) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.pe32:DebugRecord.to_dict`

Metadata: public · line 166

### TLSInfo.to_dict

No function or method docstring is declared in the v0.7.4 source.

```
def to_dict(self) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.pe32:TLSInfo.to_dict`

Metadata: public · line 188

### ResourceLeaf.to_dict

No function or method docstring is declared in the v0.7.4 source.

```
def to_dict(self) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.pe32:ResourceLeaf.to_dict`

Metadata: public · line 206

### DelayImportLibrary.to_dict

No function or method docstring is declared in the v0.7.4 source.

```
def to_dict(self) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.pe32:DelayImportLibrary.to_dict`

Metadata: public · line 232

### LoadConfigInfo.to_dict

No function or method docstring is declared in the v0.7.4 source.

```
def to_dict(self) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.pe32:LoadConfigInfo.to_dict`

Metadata: public · line 280

### PE32Image.entry_va

No function or method docstring is declared in the v0.7.4 source.

```
def entry_va(self) -> int
```

**Catalog symbol:** `x86decomp.pe32:PE32Image.entry_va`

Metadata: public · line 283

### PE32Image.to_dict

No function or method docstring is declared in the v0.7.4 source.

```
def to_dict(self) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.pe32:PE32Image.to_dict`

Metadata: internal · line 323

### _Reader.__init__

No function or method docstring is declared in the v0.7.4 source.

```
def __init__(self, data: bytes)
```

**Catalog symbol:** `x86decomp.pe32:_Reader.__init__`

Metadata: internal · line 326

### _Reader.require

No function or method docstring is declared in the v0.7.4 source.

```
def require(self, offset: int, size: int, context: str) -> None
```

**Catalog symbol:** `x86decomp.pe32:_Reader.require`

Metadata: internal · line 332

### _Reader.unpack

No function or method docstring is declared in the v0.7.4 source.

```
def unpack(self, fmt: str, offset: int, context: str) -> tuple[Any, ...]
```

**Catalog symbol:** `x86decomp.pe32:_Reader.unpack`

Metadata: internal · line 337

### _Reader.u16

No function or method docstring is declared in the v0.7.4 source.

```
def u16(self, offset: int, context: str) -> int
```

**Catalog symbol:** `x86decomp.pe32:_Reader.u16`

Metadata: internal · line 340

### _Reader.u32

No function or method docstring is declared in the v0.7.4 source.

```
def u32(self, offset: int, context: str) -> int
```

**Catalog symbol:** `x86decomp.pe32:_Reader.u32`

Metadata: internal · line 343

### _Reader.u64

No function or method docstring is declared in the v0.7.4 source.

```
def u64(self, offset: int, context: str) -> int
```

**Catalog symbol:** `x86decomp.pe32:_Reader.u64`

Metadata: internal · line 346

### _Reader.c_string

No function or method docstring is declared in the v0.7.4 source.

```
def c_string(self, offset: int, context: str, max_length: int = 4096) -> str
```

**Catalog symbol:** `x86decomp.pe32:_Reader.c_string`

Metadata: internal · line 355

### _rva_to_offset

No function or method docstring is declared in the v0.7.4 source.

```
def _rva_to_offset(rva: int, sections: tuple[Section, ...], size_of_headers: int, file_size: int) -> int
```

**Catalog symbol:** `x86decomp.pe32:_rva_to_offset`

Metadata: internal · line 376

### _directory

No function or method docstring is declared in the v0.7.4 source.

```
def _directory(directories: tuple[DataDirectory, ...], name: str) -> DataDirectory
```

**Catalog symbol:** `x86decomp.pe32:_directory`

Metadata: internal · line 383

### _parse_imports

No function or method docstring is declared in the v0.7.4 source.

```
def _parse_imports(reader: _Reader, directories: tuple[DataDirectory, ...], sections: tuple[Section, ...], size_of_headers: int) -> tuple[ImportLibrary, ...]
```

**Catalog symbol:** `x86decomp.pe32:_parse_imports`

Metadata: internal · line 455

### _parse_exports

No function or method docstring is declared in the v0.7.4 source.

```
def _parse_exports(reader: _Reader, directories: tuple[DataDirectory, ...], sections: tuple[Section, ...], size_of_headers: int) -> tuple[ExportSymbol, ...]
```

**Catalog symbol:** `x86decomp.pe32:_parse_exports`

Metadata: internal · line 521

### _parse_relocations

No function or method docstring is declared in the v0.7.4 source.

```
def _parse_relocations(reader: _Reader, directories: tuple[DataDirectory, ...], sections: tuple[Section, ...], size_of_headers: int) -> tuple[BaseRelocation, ...]
```

**Catalog symbol:** `x86decomp.pe32:_parse_relocations`

Metadata: internal · line 554

### _parse_debug_records

No function or method docstring is declared in the v0.7.4 source.

```
def _parse_debug_records(reader: _Reader, directories: tuple[DataDirectory, ...], sections: tuple[Section, ...], size_of_headers: int) -> tuple[DebugRecord, ...]
```

**Catalog symbol:** `x86decomp.pe32:_parse_debug_records`

Metadata: internal · line 615

### _parse_tls

No function or method docstring is declared in the v0.7.4 source.

```
def _parse_tls(reader: _Reader, directories: tuple[DataDirectory, ...], sections: tuple[Section, ...], size_of_headers: int, image_base: int) -> TLSInfo | None
```

**Catalog symbol:** `x86decomp.pe32:_parse_tls`

Metadata: internal · line 661

### _parse_resources

No function or method docstring is declared in the v0.7.4 source.

```
def _parse_resources(reader: _Reader, directories: tuple[DataDirectory, ...], sections: tuple[Section, ...], size_of_headers: int) -> tuple[ResourceLeaf, ...]
```

**Catalog symbol:** `x86decomp.pe32:_parse_resources`

Metadata: internal · line 726

### _parse_delay_imports

No function or method docstring is declared in the v0.7.4 source.

```
def _parse_delay_imports(reader: _Reader, directories: tuple[DataDirectory, ...], sections: tuple[Section, ...], size_of_headers: int, image_base: int) -> tuple[DelayImportLibrary, ...]
```

**Catalog symbol:** `x86decomp.pe32:_parse_delay_imports`

Metadata: internal · line 785

### _parse_load_config

No function or method docstring is declared in the v0.7.4 source.

```
def _parse_load_config(reader: _Reader, directories: tuple[DataDirectory, ...], sections: tuple[Section, ...], size_of_headers: int) -> LoadConfigInfo | None
```

**Catalog symbol:** `x86decomp.pe32:_parse_load_config`

Metadata: public · line 823

### parse_pe32

No function or method docstring is declared in the v0.7.4 source.

```
def parse_pe32(path: Path) -> PE32Image
```

**Catalog symbol:** `x86decomp.pe32:parse_pe32`
