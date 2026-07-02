---
title: x86decomp.coff
description: Strict COFF object parsing, COMDAT resolution, and deterministic synthesis.
original_path: features/x86decomp-coff.html
---

<a id="function-relocation-name"></a>
<a id="function-relocation-width"></a>
<a id="function-relocation-is-pc-relative"></a>
<a id="function-coffrelocation-width"></a>
<a id="function-coffrelocation-to-dict"></a>
<a id="function-sectiondefinitionaux-selection-name"></a>
<a id="function-sectiondefinitionaux-to-dict"></a>
<a id="function-functiondefinitionaux-to-dict"></a>
<a id="function-weakexternalaux-to-dict"></a>
<a id="function-fileaux-to-dict"></a>
<a id="function-rawaux-to-dict"></a>
<a id="function-coffsection-is-comdat"></a>
<a id="function-coffsection-comdat-selection-name"></a>
<a id="function-coffsection-alignment-power"></a>
<a id="function-coffsection-alignment"></a>
<a id="function-coffsection-to-dict"></a>
<a id="function-coffsymbol-is-function"></a>
<a id="function-coffsymbol-section-definition"></a>
<a id="function-coffsymbol-function-definition"></a>
<a id="function-coffsymbol-weak-external"></a>
<a id="function-coffsymbol-to-dict"></a>
<a id="function-coffobject-architecture"></a>
<a id="function-coffobject-section"></a>
<a id="function-coffobject-find-symbols"></a>
<a id="function-coffobject-symbol-by-index"></a>
<a id="function-coffobject-to-dict"></a>
<a id="function-extractedsymbol-to-dict"></a>
<a id="function-comdatcandidate-to-dict"></a>
<a id="function-comdatresolution-valid"></a>
<a id="function-comdatresolution-to-dict"></a>
<a id="function-reader-init"></a>
<a id="function-reader-require"></a>
<a id="function-reader-unpack"></a>
<a id="function-read-string-table"></a>
<a id="function-string-at"></a>
<a id="function-decode-symbol-name"></a>
<a id="function-decode-section-name"></a>
<a id="function-parse-header"></a>
<a id="function-parse-auxiliary-records"></a>
<a id="function-read-addend"></a>
<a id="function-parse-coff-bytes"></a>
<a id="function-parse-coff"></a>
<a id="function-extract-symbol"></a>
<a id="function-collect-comdat-candidates"></a>
<a id="function-resolve-comdats"></a>
<a id="function-encode-name"></a>
<a id="function-section-aux-bytes"></a>
<a id="function-build-synthetic-coff-object"></a>
<a id="function-synthetic-symbol-indices"></a>
<a id="function-build-synthetic-coff"></a>
<a id="function-build-comdat-coff"></a>
<a id="function-write-synthetic-coff"></a>
<a id="function-write-synthetic-coff-object"></a>

Section: Source-derived feature and function reference

# x86decomp.coff

Strict COFF object parsing, COMDAT resolution, and deterministic synthesis.

Metadata: core · current · 53 functions/methods

**Source:** `src/x86decomp/coff.py`

> **Truth basis.** Module and symbol names, signatures, line numbers, docstrings, and SHA-256 are read directly from the sealed source. When source docstrings are absent, this page says so instead of inferring behavior. Source SHA-256: `f6900af73b991d2ed380250c78d4a228ff6b10f45bd4bcf04fb449c45f13d28e`.

## Functions and methods

Metadata: public · line 127

### relocation_name

No function or method docstring is declared in the v0.7.4 source.

```
def relocation_name(machine: int, relocation_type: int) -> str
```

**Catalog symbol:** `x86decomp.coff:relocation_name`

Metadata: public · line 132

### relocation_width

No function or method docstring is declared in the v0.7.4 source.

```
def relocation_width(machine: int, relocation_type: int) -> int | None
```

**Catalog symbol:** `x86decomp.coff:relocation_width`

Metadata: public · line 137

### relocation_is_pc_relative

No function or method docstring is declared in the v0.7.4 source.

```
def relocation_is_pc_relative(machine: int, relocation_type: int) -> bool
```

**Catalog symbol:** `x86decomp.coff:relocation_is_pc_relative`

Metadata: public · line 151

### CoffRelocation.width

No function or method docstring is declared in the v0.7.4 source.

```
def width(self, machine: int) -> int | None
```

**Catalog symbol:** `x86decomp.coff:CoffRelocation.width`

Metadata: public · line 154

### CoffRelocation.to_dict

No function or method docstring is declared in the v0.7.4 source.

```
def to_dict(self, machine: int) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.coff:CoffRelocation.to_dict`

Metadata: public · line 178

### SectionDefinitionAux.selection_name

No function or method docstring is declared in the v0.7.4 source.

```
def selection_name(self) -> str
```

**Catalog symbol:** `x86decomp.coff:SectionDefinitionAux.selection_name`

Metadata: public · line 181

### SectionDefinitionAux.to_dict

No function or method docstring is declared in the v0.7.4 source.

```
def to_dict(self) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.coff:SectionDefinitionAux.to_dict`

Metadata: public · line 202

### FunctionDefinitionAux.to_dict

No function or method docstring is declared in the v0.7.4 source.

```
def to_dict(self) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.coff:FunctionDefinitionAux.to_dict`

Metadata: public · line 217

### WeakExternalAux.to_dict

No function or method docstring is declared in the v0.7.4 source.

```
def to_dict(self) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.coff:WeakExternalAux.to_dict`

Metadata: public · line 231

### FileAux.to_dict

No function or method docstring is declared in the v0.7.4 source.

```
def to_dict(self) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.coff:FileAux.to_dict`

Metadata: public · line 239

### RawAux.to_dict

No function or method docstring is declared in the v0.7.4 source.

```
def to_dict(self) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.coff:RawAux.to_dict`

Metadata: public · line 263

### CoffSection.is_comdat

No function or method docstring is declared in the v0.7.4 source.

```
def is_comdat(self) -> bool
```

**Catalog symbol:** `x86decomp.coff:CoffSection.is_comdat`

Metadata: public · line 267

### CoffSection.comdat_selection_name

No function or method docstring is declared in the v0.7.4 source.

```
def comdat_selection_name(self) -> str
```

**Catalog symbol:** `x86decomp.coff:CoffSection.comdat_selection_name`

Metadata: public · line 271

### CoffSection.alignment_power

No function or method docstring is declared in the v0.7.4 source.

```
def alignment_power(self) -> int | None
```

**Catalog symbol:** `x86decomp.coff:CoffSection.alignment_power`

Metadata: public · line 280

### CoffSection.alignment

No function or method docstring is declared in the v0.7.4 source.

```
def alignment(self) -> int | None
```

**Catalog symbol:** `x86decomp.coff:CoffSection.alignment`

Metadata: public · line 284

### CoffSection.to_dict

No function or method docstring is declared in the v0.7.4 source.

```
def to_dict(self, machine: int) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.coff:CoffSection.to_dict`

Metadata: public · line 320

### CoffSymbol.is_function

No function or method docstring is declared in the v0.7.4 source.

```
def is_function(self) -> bool
```

**Catalog symbol:** `x86decomp.coff:CoffSymbol.is_function`

Metadata: public · line 326

### CoffSymbol.section_definition

No function or method docstring is declared in the v0.7.4 source.

```
def section_definition(self) -> SectionDefinitionAux | None
```

**Catalog symbol:** `x86decomp.coff:CoffSymbol.section_definition`

Metadata: public · line 333

### CoffSymbol.function_definition

No function or method docstring is declared in the v0.7.4 source.

```
def function_definition(self) -> FunctionDefinitionAux | None
```

**Catalog symbol:** `x86decomp.coff:CoffSymbol.function_definition`

Metadata: public · line 340

### CoffSymbol.weak_external

No function or method docstring is declared in the v0.7.4 source.

```
def weak_external(self) -> WeakExternalAux | None
```

**Catalog symbol:** `x86decomp.coff:CoffSymbol.weak_external`

Metadata: public · line 346

### CoffSymbol.to_dict

No function or method docstring is declared in the v0.7.4 source.

```
def to_dict(self) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.coff:CoffSymbol.to_dict`

Metadata: public · line 373

### CoffObject.architecture

No function or method docstring is declared in the v0.7.4 source.

```
def architecture(self) -> str
```

**Catalog symbol:** `x86decomp.coff:CoffObject.architecture`

Metadata: public · line 380

### CoffObject.section

No function or method docstring is declared in the v0.7.4 source.

```
def section(self, number: int) -> CoffSection
```

**Catalog symbol:** `x86decomp.coff:CoffObject.section`

Metadata: public · line 385

### CoffObject.find_symbols

No function or method docstring is declared in the v0.7.4 source.

```
def find_symbols(self, name: str) -> list[CoffSymbol]
```

**Catalog symbol:** `x86decomp.coff:CoffObject.find_symbols`

Metadata: public · line 391

### CoffObject.symbol_by_index

No function or method docstring is declared in the v0.7.4 source.

```
def symbol_by_index(self, index: int) -> CoffSymbol | None
```

**Catalog symbol:** `x86decomp.coff:CoffObject.symbol_by_index`

Metadata: public · line 394

### CoffObject.to_dict

No function or method docstring is declared in the v0.7.4 source.

```
def to_dict(self) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.coff:CoffObject.to_dict`

Metadata: public · line 420

### ExtractedSymbol.to_dict

No function or method docstring is declared in the v0.7.4 source.

```
def to_dict(self, machine: int) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.coff:ExtractedSymbol.to_dict`

Metadata: public · line 443

### ComdatCandidate.to_dict

No function or method docstring is declared in the v0.7.4 source.

```
def to_dict(self) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.coff:ComdatCandidate.to_dict`

Metadata: public · line 465

### ComdatResolution.valid

No function or method docstring is declared in the v0.7.4 source.

```
def valid(self) -> bool
```

**Catalog symbol:** `x86decomp.coff:ComdatResolution.valid`

Metadata: public · line 468

### ComdatResolution.to_dict

No function or method docstring is declared in the v0.7.4 source.

```
def to_dict(self) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.coff:ComdatResolution.to_dict`

Metadata: internal · line 501

### _Reader.__init__

No function or method docstring is declared in the v0.7.4 source.

```
def __init__(self, data: bytes)
```

**Catalog symbol:** `x86decomp.coff:_Reader.__init__`

Metadata: internal · line 504

### _Reader.require

No function or method docstring is declared in the v0.7.4 source.

```
def require(self, offset: int, size: int, context: str) -> None
```

**Catalog symbol:** `x86decomp.coff:_Reader.require`

Metadata: internal · line 510

### _Reader.unpack

No function or method docstring is declared in the v0.7.4 source.

```
def unpack(self, fmt: str, offset: int, context: str) -> tuple[Any, ...]
```

**Catalog symbol:** `x86decomp.coff:_Reader.unpack`

Metadata: internal · line 516

### _read_string_table

No function or method docstring is declared in the v0.7.4 source.

```
def _read_string_table(reader: _Reader, pointer_to_symbols: int, count: int, symbol_record_size: int) -> bytes
```

**Catalog symbol:** `x86decomp.coff:_read_string_table`

Metadata: internal · line 530

### _string_at

No function or method docstring is declared in the v0.7.4 source.

```
def _string_at(table: bytes, offset: int, context: str) -> str
```

**Catalog symbol:** `x86decomp.coff:_string_at`

Metadata: internal · line 539

### _decode_symbol_name

No function or method docstring is declared in the v0.7.4 source.

```
def _decode_symbol_name(raw: bytes, table: bytes) -> str
```

**Catalog symbol:** `x86decomp.coff:_decode_symbol_name`

Metadata: internal · line 546

### _decode_section_name

No function or method docstring is declared in the v0.7.4 source.

```
def _decode_section_name(raw: bytes, table: bytes) -> str
```

**Catalog symbol:** `x86decomp.coff:_decode_section_name`

Metadata: internal · line 553

### _parse_header

Return variant, machine, sections, timestamp, symptr, symcount, characteristics, section-header-offset, symbol-record-size.

```
def _parse_header(reader: _Reader) -> tuple[str, int, int, int, int, int, int, int, int]
```

**Catalog symbol:** `x86decomp.coff:_parse_header`

Metadata: internal · line 607

### _parse_auxiliary_records

No function or method docstring is declared in the v0.7.4 source.

```
def _parse_auxiliary_records(*, symbol_name: str, section_number: int, symbol_type: int, storage_class: int, raw_records: Sequence[bytes], symbol_record_size: int) -> tuple[CoffAuxRecord, ...]
```

**Catalog symbol:** `x86decomp.coff:_parse_auxiliary_records`

Metadata: internal · line 665

### _read_addend

No function or method docstring is declared in the v0.7.4 source.

```
def _read_addend(raw_data: bytes, offset: int, width: int | None) -> int | None
```

**Catalog symbol:** `x86decomp.coff:_read_addend`

Metadata: public · line 671

### parse_coff_bytes

No function or method docstring is declared in the v0.7.4 source.

```
def parse_coff_bytes(data: bytes, *, path: Path | None = None) -> CoffObject
```

**Catalog symbol:** `x86decomp.coff:parse_coff_bytes`

Metadata: public · line 869

### parse_coff

No function or method docstring is declared in the v0.7.4 source.

```
def parse_coff(path: Path) -> CoffObject
```

**Catalog symbol:** `x86decomp.coff:parse_coff`

Metadata: public · line 876

### extract_symbol

No function or method docstring is declared in the v0.7.4 source.

```
def extract_symbol(obj: CoffObject, name: str, *, size: int | None = None) -> ExtractedSymbol
```

**Catalog symbol:** `x86decomp.coff:extract_symbol`

Metadata: public · line 931

### collect_comdat_candidates

No function or method docstring is declared in the v0.7.4 source.

```
def collect_comdat_candidates(objects: Sequence[CoffObject]) -> tuple[ComdatCandidate, ...]
```

**Catalog symbol:** `x86decomp.coff:collect_comdat_candidates`

Metadata: public · line 958

### resolve_comdats

Resolve COMDAT groups using PE/COFF selection semantics.

```
def resolve_comdats(objects: Sequence[CoffObject]) -> ComdatResolution
```

**Catalog symbol:** `x86decomp.coff:resolve_comdats`

Metadata: internal · line 1059

### _encode_name

No function or method docstring is declared in the v0.7.4 source.

```
def _encode_name(name: str, strings: bytearray) -> bytes
```

**Catalog symbol:** `x86decomp.coff:_encode_name`

Metadata: internal · line 1068

### _section_aux_bytes

No function or method docstring is declared in the v0.7.4 source.

```
def _section_aux_bytes(*, length: int, relocation_count: int, checksum: int, associative_section: int, selection: int) -> bytes
```

**Catalog symbol:** `x86decomp.coff:_section_aux_bytes`

Metadata: public · line 1084

### build_synthetic_coff_object

Build a deterministic classic COFF object with multiple sections.

```
def build_synthetic_coff_object(*, sections: Sequence[SyntheticSectionSpec], symbols: Sequence[SyntheticSymbolSpec], machine: int = IMAGE_FILE_MACHINE_I386, timestamp: int = 0) -> bytes
```

**Catalog symbol:** `x86decomp.coff:build_synthetic_coff_object`

Metadata: public · line 1201

### synthetic_symbol_indices

No function or method docstring is declared in the v0.7.4 source.

```
def synthetic_symbol_indices(symbols: Sequence[SyntheticSymbolSpec]) -> dict[str, int]
```

**Catalog symbol:** `x86decomp.coff:synthetic_symbol_indices`

Metadata: public · line 1212

### build_synthetic_coff

Backward-compatible one-section synthetic COFF builder.

```
def build_synthetic_coff(*, code: bytes, symbol_name: str, machine: int = IMAGE_FILE_MACHINE_I386, relocations: Iterable[CoffRelocation] = (), timestamp: int = 0) -> bytes
```

**Catalog symbol:** `x86decomp.coff:build_synthetic_coff`

Metadata: public · line 1252

### build_comdat_coff

No function or method docstring is declared in the v0.7.4 source.

```
def build_comdat_coff(*, data: bytes, symbol_name: str, section_name: str = '.text$mn', machine: int = IMAGE_FILE_MACHINE_I386, selection: int = IMAGE_COMDAT_SELECT_ANY, associative_section: int = 0, timestamp: int = 0, characteristics: int = IMAGE_SCN_CNT_CODE | IMAGE_SCN_MEM_EXECUTE | IMAGE_SCN_MEM_READ, relocations: Iterable[CoffRelocation] = ()) -> bytes
```

**Catalog symbol:** `x86decomp.coff:build_comdat_coff`

Metadata: public · line 1317

### write_synthetic_coff

No function or method docstring is declared in the v0.7.4 source.

```
def write_synthetic_coff(path: Path, *, code: bytes, symbol_name: str, machine: int = IMAGE_FILE_MACHINE_I386, relocations: Iterable[CoffRelocation] = ()) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.coff:write_synthetic_coff`

Metadata: public · line 1334

### write_synthetic_coff_object

No function or method docstring is declared in the v0.7.4 source.

```
def write_synthetic_coff_object(path: Path, *, sections: Sequence[SyntheticSectionSpec], symbols: Sequence[SyntheticSymbolSpec], machine: int = IMAGE_FILE_MACHINE_I386, timestamp: int = 0) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.coff:write_synthetic_coff_object`
