---
title: x86decomp.pdb
description: Bounded MSF 7.0 / PDB inventory and PE identity correlation.
original_path: features/x86decomp-pdb.html
---

<a id="function-require"></a>
<a id="function-u16"></a>
<a id="function-u32"></a>
<a id="function-cstring"></a>
<a id="function-align4"></a>
<a id="function-pdbstream-to-dict"></a>
<a id="function-pdbfile-to-dict"></a>
<a id="function-msf-init"></a>
<a id="function-msf-block"></a>
<a id="function-msf-parse-directory"></a>
<a id="function-msf-stream"></a>
<a id="function-parse-info"></a>
<a id="function-parse-tpi"></a>
<a id="function-parse-modules"></a>
<a id="function-parse-source-info"></a>
<a id="function-parse-section-contributions"></a>
<a id="function-parse-section-map"></a>
<a id="function-parse-dbi"></a>
<a id="function-correlate-pe"></a>
<a id="function-parse-pdb-bytes"></a>
<a id="function-parse-pdb"></a>

Section: Source-derived feature and function reference

# x86decomp.pdb

Bounded MSF 7.0 / PDB inventory and PE identity correlation.

Metadata: core · current · 21 functions/methods

**Source:** `src/x86decomp/pdb.py`

> **Truth basis.** Module and symbol names, signatures, line numbers, docstrings, and SHA-256 are read directly from the sealed source. When source docstrings are absent, this page says so instead of inferring behavior. Source SHA-256: `0ad9c99f6a1b232ce33268d35097ea6b44343d65052339c701588bf4efa79690`.

## Functions and methods

Metadata: internal · line 29

### _require

No function or method docstring is declared in the v0.7.4 source.

```
def _require(data: bytes, offset: int, size: int, context: str) -> None
```

**Catalog symbol:** `x86decomp.pdb:_require`

Metadata: internal · line 34

### _u16

No function or method docstring is declared in the v0.7.4 source.

```
def _u16(data: bytes, offset: int, context: str) -> int
```

**Catalog symbol:** `x86decomp.pdb:_u16`

Metadata: internal · line 39

### _u32

No function or method docstring is declared in the v0.7.4 source.

```
def _u32(data: bytes, offset: int, context: str) -> int
```

**Catalog symbol:** `x86decomp.pdb:_u32`

Metadata: internal · line 44

### _cstring

No function or method docstring is declared in the v0.7.4 source.

```
def _cstring(data: bytes, offset: int, limit: int, context: str) -> tuple[str, int]
```

**Catalog symbol:** `x86decomp.pdb:_cstring`

Metadata: internal · line 53

### _align4

No function or method docstring is declared in the v0.7.4 source.

```
def _align4(value: int) -> int
```

**Catalog symbol:** `x86decomp.pdb:_align4`

Metadata: public · line 64

### PDBStream.to_dict

No function or method docstring is declared in the v0.7.4 source.

```
def to_dict(self) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.pdb:PDBStream.to_dict`

Metadata: public · line 89

### PDBFile.to_dict

No function or method docstring is declared in the v0.7.4 source.

```
def to_dict(self) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.pdb:PDBFile.to_dict`

Metadata: internal · line 121

### _MSF.__init__

No function or method docstring is declared in the v0.7.4 source.

```
def __init__(self, data: bytes)
```

**Catalog symbol:** `x86decomp.pdb:_MSF.__init__`

Metadata: internal · line 148

### _MSF._block

No function or method docstring is declared in the v0.7.4 source.

```
def _block(self, index: int, context: str) -> bytes
```

**Catalog symbol:** `x86decomp.pdb:_MSF._block`

Metadata: internal · line 154

### _MSF._parse_directory

No function or method docstring is declared in the v0.7.4 source.

```
def _parse_directory(self) -> tuple[list[int | None], list[tuple[int, ...]]]
```

**Catalog symbol:** `x86decomp.pdb:_MSF._parse_directory`

Metadata: internal · line 186

### _MSF.stream

No function or method docstring is declared in the v0.7.4 source.

```
def stream(self, index: int) -> bytes | None
```

**Catalog symbol:** `x86decomp.pdb:_MSF.stream`

Metadata: internal · line 195

### _parse_info

No function or method docstring is declared in the v0.7.4 source.

```
def _parse_info(data: bytes | None) -> dict[str, Any] | None
```

**Catalog symbol:** `x86decomp.pdb:_parse_info`

Metadata: internal · line 213

### _parse_tpi

No function or method docstring is declared in the v0.7.4 source.

```
def _parse_tpi(data: bytes | None, name: str) -> dict[str, Any] | None
```

**Catalog symbol:** `x86decomp.pdb:_parse_tpi`

Metadata: internal · line 260

### _parse_modules

No function or method docstring is declared in the v0.7.4 source.

```
def _parse_modules(data: bytes) -> list[dict[str, Any]]
```

**Catalog symbol:** `x86decomp.pdb:_parse_modules`

Metadata: internal · line 324

### _parse_source_info

No function or method docstring is declared in the v0.7.4 source.

```
def _parse_source_info(data: bytes) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.pdb:_parse_source_info`

Metadata: internal · line 372

### _parse_section_contributions

No function or method docstring is declared in the v0.7.4 source.

```
def _parse_section_contributions(data: bytes) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.pdb:_parse_section_contributions`

Metadata: internal · line 402

### _parse_section_map

No function or method docstring is declared in the v0.7.4 source.

```
def _parse_section_map(data: bytes) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.pdb:_parse_section_map`

Metadata: internal · line 433

### _parse_dbi

No function or method docstring is declared in the v0.7.4 source.

```
def _parse_dbi(data: bytes | None) -> dict[str, Any] | None
```

**Catalog symbol:** `x86decomp.pdb:_parse_dbi`

Metadata: internal · line 545

### _correlate_pe

No function or method docstring is declared in the v0.7.4 source.

```
def _correlate_pe(info: dict[str, Any] | None, pe_path: Path | None) -> dict[str, Any] | None
```

**Catalog symbol:** `x86decomp.pdb:_correlate_pe`

Metadata: public · line 576

### parse_pdb_bytes

No function or method docstring is declared in the v0.7.4 source.

```
def parse_pdb_bytes(data: bytes, *, path: Path | None = None, pe_path: Path | None = None) -> PDBFile
```

**Catalog symbol:** `x86decomp.pdb:parse_pdb_bytes`

Metadata: public · line 612

### parse_pdb

No function or method docstring is declared in the v0.7.4 source.

```
def parse_pdb(path: Path, *, pe_path: Path | None = None) -> PDBFile
```

**Catalog symbol:** `x86decomp.pdb:parse_pdb`
