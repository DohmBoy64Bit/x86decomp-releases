---
title: x86decomp.coff
description: Strict COFF object parsing, COMDAT resolution, and deterministic synthesis.
---

# `x86decomp.coff`

Strict COFF object parsing, COMDAT resolution, and deterministic synthesis.

The implementation covers classic Microsoft COFF and ``ANON_OBJECT_HEADER_BIGOBJ``
objects for IMAGE_FILE_MACHINE_I386 and IMAGE_FILE_MACHINE_AMD64.  It preserves
auxiliary symbol records, section-definition COMDAT metadata, weak externals,
function definitions, relocation-overflow records, and enough linker semantics
to reconstruct deterministic object groups for matching-decompilation projects.

It intentionally does not pretend that a linked PE still contains every original
COFF relocation.  This module operates on actual object files or explicitly
reconstructed synthetic objects.

**Area:** Toolkit  
**Source:** `src/x86decomp/coff.py`  
**SHA-256:** `f6900af73b991d2ed380250c78d4a228ff6b10f45bd4bcf04fb449c45f13d28e`  
**Functions/methods:** 53

> Module names, signatures, line numbers, and docstrings are extracted directly from the source AST. No behavior is inferred when a docstring is absent.

## Functions and methods

<a id="function-relocation-name"></a>

### `relocation_name`

No function or method docstring is declared in the 0.7.5 source.

```python
def relocation_name(machine: int, relocation_type: int) -> str
```

**Catalog symbol:** `x86decomp.coff:relocation_name`  
**Visibility:** public  
**Source line:** 127

<a id="function-relocation-width"></a>

### `relocation_width`

No function or method docstring is declared in the 0.7.5 source.

```python
def relocation_width(machine: int, relocation_type: int) -> int | None
```

**Catalog symbol:** `x86decomp.coff:relocation_width`  
**Visibility:** public  
**Source line:** 132

<a id="function-relocation-is-pc-relative"></a>

### `relocation_is_pc_relative`

No function or method docstring is declared in the 0.7.5 source.

```python
def relocation_is_pc_relative(machine: int, relocation_type: int) -> bool
```

**Catalog symbol:** `x86decomp.coff:relocation_is_pc_relative`  
**Visibility:** public  
**Source line:** 137

<a id="function-coffrelocation-width"></a>

### `CoffRelocation.width`

No function or method docstring is declared in the 0.7.5 source.

```python
def CoffRelocation.width(self, machine: int) -> int | None
```

**Catalog symbol:** `x86decomp.coff:CoffRelocation.width`  
**Visibility:** public  
**Source line:** 151

<a id="function-coffrelocation-to-dict"></a>

### `CoffRelocation.to_dict`

No function or method docstring is declared in the 0.7.5 source.

```python
def CoffRelocation.to_dict(self, machine: int) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.coff:CoffRelocation.to_dict`  
**Visibility:** public  
**Source line:** 154

<a id="function-sectiondefinitionaux-selection-name"></a>

### `SectionDefinitionAux.selection_name`

No function or method docstring is declared in the 0.7.5 source.

```python
def SectionDefinitionAux.selection_name(self) -> str
```

**Catalog symbol:** `x86decomp.coff:SectionDefinitionAux.selection_name`  
**Visibility:** public  
**Source line:** 178

<a id="function-sectiondefinitionaux-to-dict"></a>

### `SectionDefinitionAux.to_dict`

No function or method docstring is declared in the 0.7.5 source.

```python
def SectionDefinitionAux.to_dict(self) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.coff:SectionDefinitionAux.to_dict`  
**Visibility:** public  
**Source line:** 181

<a id="function-functiondefinitionaux-to-dict"></a>

### `FunctionDefinitionAux.to_dict`

No function or method docstring is declared in the 0.7.5 source.

```python
def FunctionDefinitionAux.to_dict(self) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.coff:FunctionDefinitionAux.to_dict`  
**Visibility:** public  
**Source line:** 202

<a id="function-weakexternalaux-to-dict"></a>

### `WeakExternalAux.to_dict`

No function or method docstring is declared in the 0.7.5 source.

```python
def WeakExternalAux.to_dict(self) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.coff:WeakExternalAux.to_dict`  
**Visibility:** public  
**Source line:** 217

<a id="function-fileaux-to-dict"></a>

### `FileAux.to_dict`

No function or method docstring is declared in the 0.7.5 source.

```python
def FileAux.to_dict(self) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.coff:FileAux.to_dict`  
**Visibility:** public  
**Source line:** 231

<a id="function-rawaux-to-dict"></a>

### `RawAux.to_dict`

No function or method docstring is declared in the 0.7.5 source.

```python
def RawAux.to_dict(self) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.coff:RawAux.to_dict`  
**Visibility:** public  
**Source line:** 239

<a id="function-coffsection-is-comdat"></a>

### `CoffSection.is_comdat`

No function or method docstring is declared in the 0.7.5 source.

```python
def CoffSection.is_comdat(self) -> bool
```

**Catalog symbol:** `x86decomp.coff:CoffSection.is_comdat`  
**Visibility:** public  
**Source line:** 263

<a id="function-coffsection-comdat-selection-name"></a>

### `CoffSection.comdat_selection_name`

No function or method docstring is declared in the 0.7.5 source.

```python
def CoffSection.comdat_selection_name(self) -> str
```

**Catalog symbol:** `x86decomp.coff:CoffSection.comdat_selection_name`  
**Visibility:** public  
**Source line:** 267

<a id="function-coffsection-alignment-power"></a>

### `CoffSection.alignment_power`

No function or method docstring is declared in the 0.7.5 source.

```python
def CoffSection.alignment_power(self) -> int | None
```

**Catalog symbol:** `x86decomp.coff:CoffSection.alignment_power`  
**Visibility:** public  
**Source line:** 271

<a id="function-coffsection-alignment"></a>

### `CoffSection.alignment`

No function or method docstring is declared in the 0.7.5 source.

```python
def CoffSection.alignment(self) -> int | None
```

**Catalog symbol:** `x86decomp.coff:CoffSection.alignment`  
**Visibility:** public  
**Source line:** 280

<a id="function-coffsection-to-dict"></a>

### `CoffSection.to_dict`

No function or method docstring is declared in the 0.7.5 source.

```python
def CoffSection.to_dict(self, machine: int) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.coff:CoffSection.to_dict`  
**Visibility:** public  
**Source line:** 284

<a id="function-coffsymbol-is-function"></a>

### `CoffSymbol.is_function`

No function or method docstring is declared in the 0.7.5 source.

```python
def CoffSymbol.is_function(self) -> bool
```

**Catalog symbol:** `x86decomp.coff:CoffSymbol.is_function`  
**Visibility:** public  
**Source line:** 320

<a id="function-coffsymbol-section-definition"></a>

### `CoffSymbol.section_definition`

No function or method docstring is declared in the 0.7.5 source.

```python
def CoffSymbol.section_definition(self) -> SectionDefinitionAux | None
```

**Catalog symbol:** `x86decomp.coff:CoffSymbol.section_definition`  
**Visibility:** public  
**Source line:** 326

<a id="function-coffsymbol-function-definition"></a>

### `CoffSymbol.function_definition`

No function or method docstring is declared in the 0.7.5 source.

```python
def CoffSymbol.function_definition(self) -> FunctionDefinitionAux | None
```

**Catalog symbol:** `x86decomp.coff:CoffSymbol.function_definition`  
**Visibility:** public  
**Source line:** 333

<a id="function-coffsymbol-weak-external"></a>

### `CoffSymbol.weak_external`

No function or method docstring is declared in the 0.7.5 source.

```python
def CoffSymbol.weak_external(self) -> WeakExternalAux | None
```

**Catalog symbol:** `x86decomp.coff:CoffSymbol.weak_external`  
**Visibility:** public  
**Source line:** 340

<a id="function-coffsymbol-to-dict"></a>

### `CoffSymbol.to_dict`

No function or method docstring is declared in the 0.7.5 source.

```python
def CoffSymbol.to_dict(self) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.coff:CoffSymbol.to_dict`  
**Visibility:** public  
**Source line:** 346

<a id="function-coffobject-architecture"></a>

### `CoffObject.architecture`

No function or method docstring is declared in the 0.7.5 source.

```python
def CoffObject.architecture(self) -> str
```

**Catalog symbol:** `x86decomp.coff:CoffObject.architecture`  
**Visibility:** public  
**Source line:** 373

<a id="function-coffobject-section"></a>

### `CoffObject.section`

No function or method docstring is declared in the 0.7.5 source.

```python
def CoffObject.section(self, number: int) -> CoffSection
```

**Catalog symbol:** `x86decomp.coff:CoffObject.section`  
**Visibility:** public  
**Source line:** 380

<a id="function-coffobject-find-symbols"></a>

### `CoffObject.find_symbols`

No function or method docstring is declared in the 0.7.5 source.

```python
def CoffObject.find_symbols(self, name: str) -> list[CoffSymbol]
```

**Catalog symbol:** `x86decomp.coff:CoffObject.find_symbols`  
**Visibility:** public  
**Source line:** 385

<a id="function-coffobject-symbol-by-index"></a>

### `CoffObject.symbol_by_index`

No function or method docstring is declared in the 0.7.5 source.

```python
def CoffObject.symbol_by_index(self, index: int) -> CoffSymbol | None
```

**Catalog symbol:** `x86decomp.coff:CoffObject.symbol_by_index`  
**Visibility:** public  
**Source line:** 391

<a id="function-coffobject-to-dict"></a>

### `CoffObject.to_dict`

No function or method docstring is declared in the 0.7.5 source.

```python
def CoffObject.to_dict(self) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.coff:CoffObject.to_dict`  
**Visibility:** public  
**Source line:** 394

<a id="function-extractedsymbol-to-dict"></a>

### `ExtractedSymbol.to_dict`

No function or method docstring is declared in the 0.7.5 source.

```python
def ExtractedSymbol.to_dict(self, machine: int) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.coff:ExtractedSymbol.to_dict`  
**Visibility:** public  
**Source line:** 420

<a id="function-comdatcandidate-to-dict"></a>

### `ComdatCandidate.to_dict`

No function or method docstring is declared in the 0.7.5 source.

```python
def ComdatCandidate.to_dict(self) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.coff:ComdatCandidate.to_dict`  
**Visibility:** public  
**Source line:** 443

<a id="function-comdatresolution-valid"></a>

### `ComdatResolution.valid`

No function or method docstring is declared in the 0.7.5 source.

```python
def ComdatResolution.valid(self) -> bool
```

**Catalog symbol:** `x86decomp.coff:ComdatResolution.valid`  
**Visibility:** public  
**Source line:** 465

<a id="function-comdatresolution-to-dict"></a>

### `ComdatResolution.to_dict`

No function or method docstring is declared in the 0.7.5 source.

```python
def ComdatResolution.to_dict(self) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.coff:ComdatResolution.to_dict`  
**Visibility:** public  
**Source line:** 468

<a id="function-reader-init"></a>

### `_Reader.__init__`

No function or method docstring is declared in the 0.7.5 source.

```python
def _Reader.__init__(self, data: bytes)
```

**Catalog symbol:** `x86decomp.coff:_Reader.__init__`  
**Visibility:** internal  
**Source line:** 501

<a id="function-reader-require"></a>

### `_Reader.require`

No function or method docstring is declared in the 0.7.5 source.

```python
def _Reader.require(self, offset: int, size: int, context: str) -> None
```

**Catalog symbol:** `x86decomp.coff:_Reader.require`  
**Visibility:** public  
**Source line:** 504

<a id="function-reader-unpack"></a>

### `_Reader.unpack`

No function or method docstring is declared in the 0.7.5 source.

```python
def _Reader.unpack(self, fmt: str, offset: int, context: str) -> tuple[Any, ...]
```

**Catalog symbol:** `x86decomp.coff:_Reader.unpack`  
**Visibility:** public  
**Source line:** 510

<a id="function-read-string-table"></a>

### `_read_string_table`

No function or method docstring is declared in the 0.7.5 source.

```python
def _read_string_table(reader: _Reader, pointer_to_symbols: int, count: int, symbol_record_size: int) -> bytes
```

**Catalog symbol:** `x86decomp.coff:_read_string_table`  
**Visibility:** internal  
**Source line:** 516

<a id="function-string-at"></a>

### `_string_at`

No function or method docstring is declared in the 0.7.5 source.

```python
def _string_at(table: bytes, offset: int, context: str) -> str
```

**Catalog symbol:** `x86decomp.coff:_string_at`  
**Visibility:** internal  
**Source line:** 530

<a id="function-decode-symbol-name"></a>

### `_decode_symbol_name`

No function or method docstring is declared in the 0.7.5 source.

```python
def _decode_symbol_name(raw: bytes, table: bytes) -> str
```

**Catalog symbol:** `x86decomp.coff:_decode_symbol_name`  
**Visibility:** internal  
**Source line:** 539

<a id="function-decode-section-name"></a>

### `_decode_section_name`

No function or method docstring is declared in the 0.7.5 source.

```python
def _decode_section_name(raw: bytes, table: bytes) -> str
```

**Catalog symbol:** `x86decomp.coff:_decode_section_name`  
**Visibility:** internal  
**Source line:** 546

<a id="function-parse-header"></a>

### `_parse_header`

Return variant, machine, sections, timestamp, symptr, symcount,
characteristics, section-header-offset, symbol-record-size.

```python
def _parse_header(reader: _Reader) -> tuple[str, int, int, int, int, int, int, int, int]
```

**Catalog symbol:** `x86decomp.coff:_parse_header`  
**Visibility:** internal  
**Source line:** 553

<a id="function-parse-auxiliary-records"></a>

### `_parse_auxiliary_records`

No function or method docstring is declared in the 0.7.5 source.

```python
def _parse_auxiliary_records(*, symbol_name: str, section_number: int, symbol_type: int, storage_class: int, raw_records: Sequence[bytes], symbol_record_size: int) -> tuple[CoffAuxRecord, ...]
```

**Catalog symbol:** `x86decomp.coff:_parse_auxiliary_records`  
**Visibility:** internal  
**Source line:** 607

<a id="function-read-addend"></a>

### `_read_addend`

No function or method docstring is declared in the 0.7.5 source.

```python
def _read_addend(raw_data: bytes, offset: int, width: int | None) -> int | None
```

**Catalog symbol:** `x86decomp.coff:_read_addend`  
**Visibility:** internal  
**Source line:** 665

<a id="function-parse-coff-bytes"></a>

### `parse_coff_bytes`

No function or method docstring is declared in the 0.7.5 source.

```python
def parse_coff_bytes(data: bytes, *, path: Path | None=None) -> CoffObject
```

**Catalog symbol:** `x86decomp.coff:parse_coff_bytes`  
**Visibility:** public  
**Source line:** 671

<a id="function-parse-coff"></a>

### `parse_coff`

No function or method docstring is declared in the 0.7.5 source.

```python
def parse_coff(path: Path) -> CoffObject
```

**Catalog symbol:** `x86decomp.coff:parse_coff`  
**Visibility:** public  
**Source line:** 869

<a id="function-extract-symbol"></a>

### `extract_symbol`

No function or method docstring is declared in the 0.7.5 source.

```python
def extract_symbol(obj: CoffObject, name: str, *, size: int | None=None) -> ExtractedSymbol
```

**Catalog symbol:** `x86decomp.coff:extract_symbol`  
**Visibility:** public  
**Source line:** 876

<a id="function-collect-comdat-candidates"></a>

### `collect_comdat_candidates`

No function or method docstring is declared in the 0.7.5 source.

```python
def collect_comdat_candidates(objects: Sequence[CoffObject]) -> tuple[ComdatCandidate, ...]
```

**Catalog symbol:** `x86decomp.coff:collect_comdat_candidates`  
**Visibility:** public  
**Source line:** 931

<a id="function-resolve-comdats"></a>

### `resolve_comdats`

Resolve COMDAT groups using PE/COFF selection semantics.

Associative sections follow the winner of their associated parent section in
the same object.  The function reports conflicts instead of silently choosing
for NODUPLICATES, SAME_SIZE, or EXACT_MATCH violations.

```python
def resolve_comdats(objects: Sequence[CoffObject]) -> ComdatResolution
```

**Catalog symbol:** `x86decomp.coff:resolve_comdats`  
**Visibility:** public  
**Source line:** 958

<a id="function-encode-name"></a>

### `_encode_name`

No function or method docstring is declared in the 0.7.5 source.

```python
def _encode_name(name: str, strings: bytearray) -> bytes
```

**Catalog symbol:** `x86decomp.coff:_encode_name`  
**Visibility:** internal  
**Source line:** 1059

<a id="function-section-aux-bytes"></a>

### `_section_aux_bytes`

No function or method docstring is declared in the 0.7.5 source.

```python
def _section_aux_bytes(*, length: int, relocation_count: int, checksum: int, associative_section: int, selection: int) -> bytes
```

**Catalog symbol:** `x86decomp.coff:_section_aux_bytes`  
**Visibility:** internal  
**Source line:** 1068

<a id="function-build-synthetic-coff-object"></a>

### `build_synthetic_coff_object`

Build a deterministic classic COFF object with multiple sections.

Symbol indices referenced by relocations are the final on-disk indices,
including auxiliary records.  Callers should usually generate symbols first
and use :func:`synthetic_symbol_indices` to compute stable indices.

```python
def build_synthetic_coff_object(*, sections: Sequence[SyntheticSectionSpec], symbols: Sequence[SyntheticSymbolSpec], machine: int=IMAGE_FILE_MACHINE_I386, timestamp: int=0) -> bytes
```

**Catalog symbol:** `x86decomp.coff:build_synthetic_coff_object`  
**Visibility:** public  
**Source line:** 1084

<a id="function-synthetic-symbol-indices"></a>

### `synthetic_symbol_indices`

No function or method docstring is declared in the 0.7.5 source.

```python
def synthetic_symbol_indices(symbols: Sequence[SyntheticSymbolSpec]) -> dict[str, int]
```

**Catalog symbol:** `x86decomp.coff:synthetic_symbol_indices`  
**Visibility:** public  
**Source line:** 1201

<a id="function-build-synthetic-coff"></a>

### `build_synthetic_coff`

Backward-compatible one-section synthetic COFF builder.

```python
def build_synthetic_coff(*, code: bytes, symbol_name: str, machine: int=IMAGE_FILE_MACHINE_I386, relocations: Iterable[CoffRelocation]=(), timestamp: int=0) -> bytes
```

**Catalog symbol:** `x86decomp.coff:build_synthetic_coff`  
**Visibility:** public  
**Source line:** 1212

<a id="function-build-comdat-coff"></a>

### `build_comdat_coff`

No function or method docstring is declared in the 0.7.5 source.

```python
def build_comdat_coff(*, data: bytes, symbol_name: str, section_name: str='.text$mn', machine: int=IMAGE_FILE_MACHINE_I386, selection: int=IMAGE_COMDAT_SELECT_ANY, associative_section: int=0, timestamp: int=0, characteristics: int=IMAGE_SCN_CNT_CODE | IMAGE_SCN_MEM_EXECUTE | IMAGE_SCN_MEM_READ, relocations: Iterable[CoffRelocation]=()) -> bytes
```

**Catalog symbol:** `x86decomp.coff:build_comdat_coff`  
**Visibility:** public  
**Source line:** 1252

<a id="function-write-synthetic-coff"></a>

### `write_synthetic_coff`

No function or method docstring is declared in the 0.7.5 source.

```python
def write_synthetic_coff(path: Path, *, code: bytes, symbol_name: str, machine: int=IMAGE_FILE_MACHINE_I386, relocations: Iterable[CoffRelocation]=()) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.coff:write_synthetic_coff`  
**Visibility:** public  
**Source line:** 1317

<a id="function-write-synthetic-coff-object"></a>

### `write_synthetic_coff_object`

No function or method docstring is declared in the 0.7.5 source.

```python
def write_synthetic_coff_object(path: Path, *, sections: Sequence[SyntheticSectionSpec], symbols: Sequence[SyntheticSymbolSpec], machine: int=IMAGE_FILE_MACHINE_I386, timestamp: int=0) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.coff:write_synthetic_coff_object`  
**Visibility:** public  
**Source line:** 1334
