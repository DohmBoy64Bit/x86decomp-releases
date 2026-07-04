---
title: x86decomp.pe32
description: Strict, dependency-free parser for native x86 PE32 images.
---

# `x86decomp.pe32`

Strict, dependency-free parser for native x86 PE32 images.

The parser intentionally supports the first toolkit scope only: little-endian
Windows PE32 images for IMAGE_FILE_MACHINE_I386. It never executes the input.

**Area:** Toolkit  
**Source:** `src/x86decomp/pe32.py`  
**SHA-256:** `746651d78b0b8401565dd22e99f73c8c902b13400fd80094d4675ab52c8c4be5`  
**Functions/methods:** 32

> Module names, signatures, line numbers, and docstrings are extracted directly from the source AST. No behavior is inferred when a docstring is absent.

## Functions and methods

<a id="function-datadirectory-to-dict"></a>

### `DataDirectory.to_dict`

No function or method docstring is declared in the 0.7.5 source.

```python
def DataDirectory.to_dict(self) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.pe32:DataDirectory.to_dict`  
**Visibility:** public  
**Source line:** 47

<a id="function-section-mapped-size"></a>

### `Section.mapped_size`

No function or method docstring is declared in the 0.7.5 source.

```python
def Section.mapped_size(self) -> int
```

**Catalog symbol:** `x86decomp.pe32:Section.mapped_size`  
**Visibility:** public  
**Source line:** 62

<a id="function-section-to-dict"></a>

### `Section.to_dict`

No function or method docstring is declared in the 0.7.5 source.

```python
def Section.to_dict(self) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.pe32:Section.to_dict`  
**Visibility:** public  
**Source line:** 65

<a id="function-importsymbol-to-dict"></a>

### `ImportSymbol.to_dict`

No function or method docstring is declared in the 0.7.5 source.

```python
def ImportSymbol.to_dict(self) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.pe32:ImportSymbol.to_dict`  
**Visibility:** public  
**Source line:** 87

<a id="function-importlibrary-to-dict"></a>

### `ImportLibrary.to_dict`

No function or method docstring is declared in the 0.7.5 source.

```python
def ImportLibrary.to_dict(self) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.pe32:ImportLibrary.to_dict`  
**Visibility:** public  
**Source line:** 102

<a id="function-exportsymbol-to-dict"></a>

### `ExportSymbol.to_dict`

No function or method docstring is declared in the 0.7.5 source.

```python
def ExportSymbol.to_dict(self) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.pe32:ExportSymbol.to_dict`  
**Visibility:** public  
**Source line:** 113

<a id="function-baserelocation-to-dict"></a>

### `BaseRelocation.to_dict`

No function or method docstring is declared in the 0.7.5 source.

```python
def BaseRelocation.to_dict(self) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.pe32:BaseRelocation.to_dict`  
**Visibility:** public  
**Source line:** 128

<a id="function-debugrecord-to-dict"></a>

### `DebugRecord.to_dict`

No function or method docstring is declared in the 0.7.5 source.

```python
def DebugRecord.to_dict(self) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.pe32:DebugRecord.to_dict`  
**Visibility:** public  
**Source line:** 143

<a id="function-tlsinfo-to-dict"></a>

### `TLSInfo.to_dict`

No function or method docstring is declared in the 0.7.5 source.

```python
def TLSInfo.to_dict(self) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.pe32:TLSInfo.to_dict`  
**Visibility:** public  
**Source line:** 166

<a id="function-resourceleaf-to-dict"></a>

### `ResourceLeaf.to_dict`

No function or method docstring is declared in the 0.7.5 source.

```python
def ResourceLeaf.to_dict(self) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.pe32:ResourceLeaf.to_dict`  
**Visibility:** public  
**Source line:** 188

<a id="function-delayimportlibrary-to-dict"></a>

### `DelayImportLibrary.to_dict`

No function or method docstring is declared in the 0.7.5 source.

```python
def DelayImportLibrary.to_dict(self) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.pe32:DelayImportLibrary.to_dict`  
**Visibility:** public  
**Source line:** 206

<a id="function-loadconfiginfo-to-dict"></a>

### `LoadConfigInfo.to_dict`

No function or method docstring is declared in the 0.7.5 source.

```python
def LoadConfigInfo.to_dict(self) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.pe32:LoadConfigInfo.to_dict`  
**Visibility:** public  
**Source line:** 232

<a id="function-pe32image-entry-va"></a>

### `PE32Image.entry_va`

No function or method docstring is declared in the 0.7.5 source.

```python
def PE32Image.entry_va(self) -> int
```

**Catalog symbol:** `x86decomp.pe32:PE32Image.entry_va`  
**Visibility:** public  
**Source line:** 280

<a id="function-pe32image-to-dict"></a>

### `PE32Image.to_dict`

No function or method docstring is declared in the 0.7.5 source.

```python
def PE32Image.to_dict(self) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.pe32:PE32Image.to_dict`  
**Visibility:** public  
**Source line:** 283

<a id="function-reader-init"></a>

### `_Reader.__init__`

No function or method docstring is declared in the 0.7.5 source.

```python
def _Reader.__init__(self, data: bytes)
```

**Catalog symbol:** `x86decomp.pe32:_Reader.__init__`  
**Visibility:** internal  
**Source line:** 323

<a id="function-reader-require"></a>

### `_Reader.require`

No function or method docstring is declared in the 0.7.5 source.

```python
def _Reader.require(self, offset: int, size: int, context: str) -> None
```

**Catalog symbol:** `x86decomp.pe32:_Reader.require`  
**Visibility:** public  
**Source line:** 326

<a id="function-reader-unpack"></a>

### `_Reader.unpack`

No function or method docstring is declared in the 0.7.5 source.

```python
def _Reader.unpack(self, fmt: str, offset: int, context: str) -> tuple[Any, ...]
```

**Catalog symbol:** `x86decomp.pe32:_Reader.unpack`  
**Visibility:** public  
**Source line:** 332

<a id="function-reader-u16"></a>

### `_Reader.u16`

No function or method docstring is declared in the 0.7.5 source.

```python
def _Reader.u16(self, offset: int, context: str) -> int
```

**Catalog symbol:** `x86decomp.pe32:_Reader.u16`  
**Visibility:** public  
**Source line:** 337

<a id="function-reader-u32"></a>

### `_Reader.u32`

No function or method docstring is declared in the 0.7.5 source.

```python
def _Reader.u32(self, offset: int, context: str) -> int
```

**Catalog symbol:** `x86decomp.pe32:_Reader.u32`  
**Visibility:** public  
**Source line:** 340

<a id="function-reader-u64"></a>

### `_Reader.u64`

No function or method docstring is declared in the 0.7.5 source.

```python
def _Reader.u64(self, offset: int, context: str) -> int
```

**Catalog symbol:** `x86decomp.pe32:_Reader.u64`  
**Visibility:** public  
**Source line:** 343

<a id="function-reader-c-string"></a>

### `_Reader.c_string`

No function or method docstring is declared in the 0.7.5 source.

```python
def _Reader.c_string(self, offset: int, context: str, max_length: int=4096) -> str
```

**Catalog symbol:** `x86decomp.pe32:_Reader.c_string`  
**Visibility:** public  
**Source line:** 346

<a id="function-rva-to-offset"></a>

### `_rva_to_offset`

No function or method docstring is declared in the 0.7.5 source.

```python
def _rva_to_offset(rva: int, sections: tuple[Section, ...], size_of_headers: int, file_size: int) -> int
```

**Catalog symbol:** `x86decomp.pe32:_rva_to_offset`  
**Visibility:** internal  
**Source line:** 355

<a id="function-directory"></a>

### `_directory`

No function or method docstring is declared in the 0.7.5 source.

```python
def _directory(directories: tuple[DataDirectory, ...], name: str) -> DataDirectory
```

**Catalog symbol:** `x86decomp.pe32:_directory`  
**Visibility:** internal  
**Source line:** 376

<a id="function-parse-imports"></a>

### `_parse_imports`

No function or method docstring is declared in the 0.7.5 source.

```python
def _parse_imports(reader: _Reader, directories: tuple[DataDirectory, ...], sections: tuple[Section, ...], size_of_headers: int) -> tuple[ImportLibrary, ...]
```

**Catalog symbol:** `x86decomp.pe32:_parse_imports`  
**Visibility:** internal  
**Source line:** 383

<a id="function-parse-exports"></a>

### `_parse_exports`

No function or method docstring is declared in the 0.7.5 source.

```python
def _parse_exports(reader: _Reader, directories: tuple[DataDirectory, ...], sections: tuple[Section, ...], size_of_headers: int) -> tuple[ExportSymbol, ...]
```

**Catalog symbol:** `x86decomp.pe32:_parse_exports`  
**Visibility:** internal  
**Source line:** 455

<a id="function-parse-relocations"></a>

### `_parse_relocations`

No function or method docstring is declared in the 0.7.5 source.

```python
def _parse_relocations(reader: _Reader, directories: tuple[DataDirectory, ...], sections: tuple[Section, ...], size_of_headers: int) -> tuple[BaseRelocation, ...]
```

**Catalog symbol:** `x86decomp.pe32:_parse_relocations`  
**Visibility:** internal  
**Source line:** 521

<a id="function-parse-debug-records"></a>

### `_parse_debug_records`

No function or method docstring is declared in the 0.7.5 source.

```python
def _parse_debug_records(reader: _Reader, directories: tuple[DataDirectory, ...], sections: tuple[Section, ...], size_of_headers: int) -> tuple[DebugRecord, ...]
```

**Catalog symbol:** `x86decomp.pe32:_parse_debug_records`  
**Visibility:** internal  
**Source line:** 554

<a id="function-parse-tls"></a>

### `_parse_tls`

No function or method docstring is declared in the 0.7.5 source.

```python
def _parse_tls(reader: _Reader, directories: tuple[DataDirectory, ...], sections: tuple[Section, ...], size_of_headers: int, image_base: int) -> TLSInfo | None
```

**Catalog symbol:** `x86decomp.pe32:_parse_tls`  
**Visibility:** internal  
**Source line:** 615

<a id="function-parse-resources"></a>

### `_parse_resources`

No function or method docstring is declared in the 0.7.5 source.

```python
def _parse_resources(reader: _Reader, directories: tuple[DataDirectory, ...], sections: tuple[Section, ...], size_of_headers: int) -> tuple[ResourceLeaf, ...]
```

**Catalog symbol:** `x86decomp.pe32:_parse_resources`  
**Visibility:** internal  
**Source line:** 661

<a id="function-parse-delay-imports"></a>

### `_parse_delay_imports`

No function or method docstring is declared in the 0.7.5 source.

```python
def _parse_delay_imports(reader: _Reader, directories: tuple[DataDirectory, ...], sections: tuple[Section, ...], size_of_headers: int, image_base: int) -> tuple[DelayImportLibrary, ...]
```

**Catalog symbol:** `x86decomp.pe32:_parse_delay_imports`  
**Visibility:** internal  
**Source line:** 726

<a id="function-parse-load-config"></a>

### `_parse_load_config`

No function or method docstring is declared in the 0.7.5 source.

```python
def _parse_load_config(reader: _Reader, directories: tuple[DataDirectory, ...], sections: tuple[Section, ...], size_of_headers: int) -> LoadConfigInfo | None
```

**Catalog symbol:** `x86decomp.pe32:_parse_load_config`  
**Visibility:** internal  
**Source line:** 785

<a id="function-parse-pe32"></a>

### `parse_pe32`

No function or method docstring is declared in the 0.7.5 source.

```python
def parse_pe32(path: Path) -> PE32Image
```

**Catalog symbol:** `x86decomp.pe32:parse_pe32`  
**Visibility:** public  
**Source line:** 823
