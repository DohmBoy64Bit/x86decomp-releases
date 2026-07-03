---
title: x86decomp.pdb
description: Bounded MSF 7.0 / PDB inventory and PE identity correlation.
---

# `x86decomp.pdb`

Bounded MSF 7.0 / PDB inventory and PE identity correlation.

This parser intentionally inventories stable container, PDB, TPI/IPI, and DBI metadata.
It does not claim complete CodeView type/symbol reconstruction. Every read is bounds checked,
stream blocks may be discontiguous, and unsupported variants fail explicitly.

**Area:** Toolkit  
**Source:** `src/x86decomp/pdb.py`  
**SHA-256:** `0ad9c99f6a1b232ce33268d35097ea6b44343d65052339c701588bf4efa79690`  
**Functions/methods:** 21

> Module names, signatures, line numbers, and docstrings are extracted directly from the source AST. No behavior is inferred when a docstring is absent.

## Functions and methods

<a id="function-require"></a>

### `_require`

No function or method docstring is declared in the 0.7.5 source.

```python
def _require(data: bytes, offset: int, size: int, context: str) -> None
```

**Catalog symbol:** `x86decomp.pdb:_require`  
**Visibility:** internal  
**Source line:** 29

<a id="function-u16"></a>

### `_u16`

No function or method docstring is declared in the 0.7.5 source.

```python
def _u16(data: bytes, offset: int, context: str) -> int
```

**Catalog symbol:** `x86decomp.pdb:_u16`  
**Visibility:** internal  
**Source line:** 34

<a id="function-u32"></a>

### `_u32`

No function or method docstring is declared in the 0.7.5 source.

```python
def _u32(data: bytes, offset: int, context: str) -> int
```

**Catalog symbol:** `x86decomp.pdb:_u32`  
**Visibility:** internal  
**Source line:** 39

<a id="function-cstring"></a>

### `_cstring`

No function or method docstring is declared in the 0.7.5 source.

```python
def _cstring(data: bytes, offset: int, limit: int, context: str) -> tuple[str, int]
```

**Catalog symbol:** `x86decomp.pdb:_cstring`  
**Visibility:** internal  
**Source line:** 44

<a id="function-align4"></a>

### `_align4`

No function or method docstring is declared in the 0.7.5 source.

```python
def _align4(value: int) -> int
```

**Catalog symbol:** `x86decomp.pdb:_align4`  
**Visibility:** internal  
**Source line:** 53

<a id="function-pdbstream-to-dict"></a>

### `PDBStream.to_dict`

No function or method docstring is declared in the 0.7.5 source.

```python
def PDBStream.to_dict(self) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.pdb:PDBStream.to_dict`  
**Visibility:** public  
**Source line:** 64

<a id="function-pdbfile-to-dict"></a>

### `PDBFile.to_dict`

No function or method docstring is declared in the 0.7.5 source.

```python
def PDBFile.to_dict(self) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.pdb:PDBFile.to_dict`  
**Visibility:** public  
**Source line:** 89

<a id="function-msf-init"></a>

### `_MSF.__init__`

No function or method docstring is declared in the 0.7.5 source.

```python
def _MSF.__init__(self, data: bytes)
```

**Catalog symbol:** `x86decomp.pdb:_MSF.__init__`  
**Visibility:** internal  
**Source line:** 121

<a id="function-msf-block"></a>

### `_MSF._block`

No function or method docstring is declared in the 0.7.5 source.

```python
def _MSF._block(self, index: int, context: str) -> bytes
```

**Catalog symbol:** `x86decomp.pdb:_MSF._block`  
**Visibility:** internal  
**Source line:** 148

<a id="function-msf-parse-directory"></a>

### `_MSF._parse_directory`

No function or method docstring is declared in the 0.7.5 source.

```python
def _MSF._parse_directory(self) -> tuple[list[int | None], list[tuple[int, ...]]]
```

**Catalog symbol:** `x86decomp.pdb:_MSF._parse_directory`  
**Visibility:** internal  
**Source line:** 154

<a id="function-msf-stream"></a>

### `_MSF.stream`

No function or method docstring is declared in the 0.7.5 source.

```python
def _MSF.stream(self, index: int) -> bytes | None
```

**Catalog symbol:** `x86decomp.pdb:_MSF.stream`  
**Visibility:** public  
**Source line:** 186

<a id="function-parse-info"></a>

### `_parse_info`

No function or method docstring is declared in the 0.7.5 source.

```python
def _parse_info(data: bytes | None) -> dict[str, Any] | None
```

**Catalog symbol:** `x86decomp.pdb:_parse_info`  
**Visibility:** internal  
**Source line:** 195

<a id="function-parse-tpi"></a>

### `_parse_tpi`

No function or method docstring is declared in the 0.7.5 source.

```python
def _parse_tpi(data: bytes | None, name: str) -> dict[str, Any] | None
```

**Catalog symbol:** `x86decomp.pdb:_parse_tpi`  
**Visibility:** internal  
**Source line:** 213

<a id="function-parse-modules"></a>

### `_parse_modules`

No function or method docstring is declared in the 0.7.5 source.

```python
def _parse_modules(data: bytes) -> list[dict[str, Any]]
```

**Catalog symbol:** `x86decomp.pdb:_parse_modules`  
**Visibility:** internal  
**Source line:** 260

<a id="function-parse-source-info"></a>

### `_parse_source_info`

No function or method docstring is declared in the 0.7.5 source.

```python
def _parse_source_info(data: bytes) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.pdb:_parse_source_info`  
**Visibility:** internal  
**Source line:** 324

<a id="function-parse-section-contributions"></a>

### `_parse_section_contributions`

No function or method docstring is declared in the 0.7.5 source.

```python
def _parse_section_contributions(data: bytes) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.pdb:_parse_section_contributions`  
**Visibility:** internal  
**Source line:** 372

<a id="function-parse-section-map"></a>

### `_parse_section_map`

No function or method docstring is declared in the 0.7.5 source.

```python
def _parse_section_map(data: bytes) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.pdb:_parse_section_map`  
**Visibility:** internal  
**Source line:** 402

<a id="function-parse-dbi"></a>

### `_parse_dbi`

No function or method docstring is declared in the 0.7.5 source.

```python
def _parse_dbi(data: bytes | None) -> dict[str, Any] | None
```

**Catalog symbol:** `x86decomp.pdb:_parse_dbi`  
**Visibility:** internal  
**Source line:** 433

<a id="function-correlate-pe"></a>

### `_correlate_pe`

No function or method docstring is declared in the 0.7.5 source.

```python
def _correlate_pe(info: dict[str, Any] | None, pe_path: Path | None) -> dict[str, Any] | None
```

**Catalog symbol:** `x86decomp.pdb:_correlate_pe`  
**Visibility:** internal  
**Source line:** 545

<a id="function-parse-pdb-bytes"></a>

### `parse_pdb_bytes`

No function or method docstring is declared in the 0.7.5 source.

```python
def parse_pdb_bytes(data: bytes, *, path: Path | None=None, pe_path: Path | None=None) -> PDBFile
```

**Catalog symbol:** `x86decomp.pdb:parse_pdb_bytes`  
**Visibility:** public  
**Source line:** 576

<a id="function-parse-pdb"></a>

### `parse_pdb`

No function or method docstring is declared in the 0.7.5 source.

```python
def parse_pdb(path: Path, *, pe_path: Path | None=None) -> PDBFile
```

**Catalog symbol:** `x86decomp.pdb:parse_pdb`  
**Visibility:** public  
**Source line:** 612
