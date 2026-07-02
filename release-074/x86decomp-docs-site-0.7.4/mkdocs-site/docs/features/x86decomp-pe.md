---
title: x86decomp.pe
description: Architecture-dispatching PE parser with PE32+ x86-64 support.
original_path: features/x86decomp-pe.html
---

<a id="function-tls64info-to-dict"></a>
<a id="function-runtimefunction-to-dict"></a>
<a id="function-pe64image-entry-va"></a>
<a id="function-pe64image-to-dict"></a>
<a id="function-parse-imports64"></a>
<a id="function-parse-tls64"></a>
<a id="function-parse-delay-imports64"></a>
<a id="function-parse-load-config64"></a>
<a id="function-parse-runtime-functions"></a>
<a id="function-parse-pe64"></a>
<a id="function-inspect-pe-kind"></a>
<a id="function-parse-pe"></a>

Section: Source-derived feature and function reference

# x86decomp.pe

Architecture-dispatching PE parser with PE32+ x86-64 support.

Metadata: core · current · 12 functions/methods

**Source:** `src/x86decomp/pe.py`

> **Truth basis.** Module and symbol names, signatures, line numbers, docstrings, and SHA-256 are read directly from the sealed source. When source docstrings are absent, this page says so instead of inferring behavior. Source SHA-256: `39a5dd1b26da8d0ef84e8ff247183068eb4943ab38211df3c56c43ca9a6911c0`.

## Functions and methods

Metadata: public · line 52

### TLS64Info.to_dict

No function or method docstring is declared in the v0.7.4 source.

```
def to_dict(self) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.pe:TLS64Info.to_dict`

Metadata: public · line 70

### RuntimeFunction.to_dict

No function or method docstring is declared in the v0.7.4 source.

```
def to_dict(self) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.pe:RuntimeFunction.to_dict`

Metadata: public · line 108

### PE64Image.entry_va

No function or method docstring is declared in the v0.7.4 source.

```
def entry_va(self) -> int
```

**Catalog symbol:** `x86decomp.pe:PE64Image.entry_va`

Metadata: public · line 111

### PE64Image.to_dict

No function or method docstring is declared in the v0.7.4 source.

```
def to_dict(self) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.pe:PE64Image.to_dict`

Metadata: internal · line 151

### _parse_imports64

No function or method docstring is declared in the v0.7.4 source.

```
def _parse_imports64(reader: _Reader, directories: tuple[DataDirectory, ...], sections: tuple[Section, ...], size_of_headers: int) -> tuple[ImportLibrary, ...]
```

**Catalog symbol:** `x86decomp.pe:_parse_imports64`

Metadata: internal · line 184

### _parse_tls64

No function or method docstring is declared in the v0.7.4 source.

```
def _parse_tls64(reader: _Reader, directories: tuple[DataDirectory, ...], sections: tuple[Section, ...], size_of_headers: int, image_base: int) -> TLS64Info | None
```

**Catalog symbol:** `x86decomp.pe:_parse_tls64`

Metadata: internal · line 205

### _parse_delay_imports64

No function or method docstring is declared in the v0.7.4 source.

```
def _parse_delay_imports64(reader: _Reader, directories: tuple[DataDirectory, ...], sections: tuple[Section, ...], size_of_headers: int, image_base: int) -> tuple[DelayImportLibrary, ...]
```

**Catalog symbol:** `x86decomp.pe:_parse_delay_imports64`

Metadata: internal · line 247

### _parse_load_config64

No function or method docstring is declared in the v0.7.4 source.

```
def _parse_load_config64(reader: _Reader, directories: tuple[DataDirectory, ...], sections: tuple[Section, ...], size_of_headers: int) -> LoadConfigInfo | None
```

**Catalog symbol:** `x86decomp.pe:_parse_load_config64`

Metadata: internal · line 268

### _parse_runtime_functions

No function or method docstring is declared in the v0.7.4 source.

```
def _parse_runtime_functions(reader: _Reader, directories: tuple[DataDirectory, ...], sections: tuple[Section, ...], size_of_headers: int) -> tuple[RuntimeFunction, ...]
```

**Catalog symbol:** `x86decomp.pe:_parse_runtime_functions`

Metadata: public · line 278

### parse_pe64

No function or method docstring is declared in the v0.7.4 source.

```
def parse_pe64(path: Path) -> PE64Image
```

**Catalog symbol:** `x86decomp.pe:parse_pe64`

Metadata: public · line 353

### inspect_pe_kind

No function or method docstring is declared in the v0.7.4 source.

```
def inspect_pe_kind(path: Path) -> tuple[int, int]
```

**Catalog symbol:** `x86decomp.pe:inspect_pe_kind`

Metadata: public · line 365

### parse_pe

No function or method docstring is declared in the v0.7.4 source.

```
def parse_pe(path: Path) -> Any
```

**Catalog symbol:** `x86decomp.pe:parse_pe`
