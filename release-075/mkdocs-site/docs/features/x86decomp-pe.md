---
title: x86decomp.pe
description: Architecture-dispatching PE parser with PE32+ x86-64 support.
---

# `x86decomp.pe`

Architecture-dispatching PE parser with PE32+ x86-64 support.

**Area:** Toolkit  
**Source:** `src/x86decomp/pe.py`  
**SHA-256:** `39a5dd1b26da8d0ef84e8ff247183068eb4943ab38211df3c56c43ca9a6911c0`  
**Functions/methods:** 12

> Module names, signatures, line numbers, and docstrings are extracted directly from the source AST. No behavior is inferred when a docstring is absent.

## Functions and methods

<a id="function-tls64info-to-dict"></a>

### `TLS64Info.to_dict`

No function or method docstring is declared in the 0.7.5 source.

```python
def TLS64Info.to_dict(self) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.pe:TLS64Info.to_dict`  
**Visibility:** public  
**Source line:** 52

<a id="function-runtimefunction-to-dict"></a>

### `RuntimeFunction.to_dict`

No function or method docstring is declared in the 0.7.5 source.

```python
def RuntimeFunction.to_dict(self) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.pe:RuntimeFunction.to_dict`  
**Visibility:** public  
**Source line:** 70

<a id="function-pe64image-entry-va"></a>

### `PE64Image.entry_va`

No function or method docstring is declared in the 0.7.5 source.

```python
def PE64Image.entry_va(self) -> int
```

**Catalog symbol:** `x86decomp.pe:PE64Image.entry_va`  
**Visibility:** public  
**Source line:** 108

<a id="function-pe64image-to-dict"></a>

### `PE64Image.to_dict`

No function or method docstring is declared in the 0.7.5 source.

```python
def PE64Image.to_dict(self) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.pe:PE64Image.to_dict`  
**Visibility:** public  
**Source line:** 111

<a id="function-parse-imports64"></a>

### `_parse_imports64`

No function or method docstring is declared in the 0.7.5 source.

```python
def _parse_imports64(reader: _Reader, directories: tuple[DataDirectory, ...], sections: tuple[Section, ...], size_of_headers: int) -> tuple[ImportLibrary, ...]
```

**Catalog symbol:** `x86decomp.pe:_parse_imports64`  
**Visibility:** internal  
**Source line:** 151

<a id="function-parse-tls64"></a>

### `_parse_tls64`

No function or method docstring is declared in the 0.7.5 source.

```python
def _parse_tls64(reader: _Reader, directories: tuple[DataDirectory, ...], sections: tuple[Section, ...], size_of_headers: int, image_base: int) -> TLS64Info | None
```

**Catalog symbol:** `x86decomp.pe:_parse_tls64`  
**Visibility:** internal  
**Source line:** 184

<a id="function-parse-delay-imports64"></a>

### `_parse_delay_imports64`

No function or method docstring is declared in the 0.7.5 source.

```python
def _parse_delay_imports64(reader: _Reader, directories: tuple[DataDirectory, ...], sections: tuple[Section, ...], size_of_headers: int, image_base: int) -> tuple[DelayImportLibrary, ...]
```

**Catalog symbol:** `x86decomp.pe:_parse_delay_imports64`  
**Visibility:** internal  
**Source line:** 205

<a id="function-parse-load-config64"></a>

### `_parse_load_config64`

No function or method docstring is declared in the 0.7.5 source.

```python
def _parse_load_config64(reader: _Reader, directories: tuple[DataDirectory, ...], sections: tuple[Section, ...], size_of_headers: int) -> LoadConfigInfo | None
```

**Catalog symbol:** `x86decomp.pe:_parse_load_config64`  
**Visibility:** internal  
**Source line:** 247

<a id="function-parse-runtime-functions"></a>

### `_parse_runtime_functions`

No function or method docstring is declared in the 0.7.5 source.

```python
def _parse_runtime_functions(reader: _Reader, directories: tuple[DataDirectory, ...], sections: tuple[Section, ...], size_of_headers: int) -> tuple[RuntimeFunction, ...]
```

**Catalog symbol:** `x86decomp.pe:_parse_runtime_functions`  
**Visibility:** internal  
**Source line:** 268

<a id="function-parse-pe64"></a>

### `parse_pe64`

No function or method docstring is declared in the 0.7.5 source.

```python
def parse_pe64(path: Path) -> PE64Image
```

**Catalog symbol:** `x86decomp.pe:parse_pe64`  
**Visibility:** public  
**Source line:** 278

<a id="function-inspect-pe-kind"></a>

### `inspect_pe_kind`

No function or method docstring is declared in the 0.7.5 source.

```python
def inspect_pe_kind(path: Path) -> tuple[int, int]
```

**Catalog symbol:** `x86decomp.pe:inspect_pe_kind`  
**Visibility:** public  
**Source line:** 353

<a id="function-parse-pe"></a>

### `parse_pe`

No function or method docstring is declared in the 0.7.5 source.

```python
def parse_pe(path: Path) -> Any
```

**Catalog symbol:** `x86decomp.pe:parse_pe`  
**Visibility:** public  
**Source line:** 365
