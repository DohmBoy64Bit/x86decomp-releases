---
title: x86decomp.msvc_metadata
description: Microsoft C++ metadata, unwind, TLS, and initializer recovery.
original_path: features/x86decomp-msvc-metadata.html
---

<a id="function-typedescriptorrecord-to-dict"></a>
<a id="function-baseclassrecord-to-dict"></a>
<a id="function-completeobjectlocatorrecord-to-dict"></a>
<a id="function-vtablerecord-to-dict"></a>
<a id="function-unwindcoderecord-to-dict"></a>
<a id="function-unwindinforecord-to-dict"></a>
<a id="function-peview-init"></a>
<a id="function-peview-rva-to-offset"></a>
<a id="function-peview-valid-rva"></a>
<a id="function-peview-read"></a>
<a id="function-peview-u16"></a>
<a id="function-peview-u32"></a>
<a id="function-peview-i32"></a>
<a id="function-peview-u64"></a>
<a id="function-peview-pointer"></a>
<a id="function-peview-va-to-rva"></a>
<a id="function-peview-encoded-pointer-to-rva"></a>
<a id="function-peview-c-string"></a>
<a id="function-peview-executable-rva"></a>
<a id="function-peview-readonly-data-sections"></a>
<a id="function-display-type-name"></a>
<a id="function-scan-type-descriptors"></a>
<a id="function-parse-base-class"></a>
<a id="function-parse-hierarchy"></a>
<a id="function-scan-complete-object-locators"></a>
<a id="function-scan-vtables"></a>
<a id="function-decode-unwind-codes"></a>
<a id="function-parse-x64-unwind"></a>
<a id="function-parse-safe-seh"></a>
<a id="function-tls-report"></a>
<a id="function-scan-exception-func-info"></a>
<a id="function-scan-coff-tls"></a>
<a id="function-scan-static-initializers"></a>
<a id="function-analyze-msvc-metadata"></a>

Section: Source-derived feature and function reference

# x86decomp.msvc_metadata

Microsoft C++ metadata, unwind, TLS, and initializer recovery.

Metadata: core · current · 34 functions/methods

**Source:** `src/x86decomp/msvc_metadata.py`

> **Truth basis.** Module and symbol names, signatures, line numbers, docstrings, and SHA-256 are read directly from the sealed source. When source docstrings are absent, this page says so instead of inferring behavior. Source SHA-256: `a09e12dd6d748ba39648bf05d885656080c1c03be63d8dde592e26cb36b72951`.

## Functions and methods

Metadata: public · line 35

### TypeDescriptorRecord.to_dict

No function or method docstring is declared in the v0.7.4 source.

```
def to_dict(self) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.msvc_metadata:TypeDescriptorRecord.to_dict`

Metadata: public · line 58

### BaseClassRecord.to_dict

No function or method docstring is declared in the v0.7.4 source.

```
def to_dict(self) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.msvc_metadata:BaseClassRecord.to_dict`

Metadata: public · line 87

### CompleteObjectLocatorRecord.to_dict

No function or method docstring is declared in the v0.7.4 source.

```
def to_dict(self) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.msvc_metadata:CompleteObjectLocatorRecord.to_dict`

Metadata: public · line 109

### VTableRecord.to_dict

No function or method docstring is declared in the v0.7.4 source.

```
def to_dict(self) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.msvc_metadata:VTableRecord.to_dict`

Metadata: public · line 127

### UnwindCodeRecord.to_dict

No function or method docstring is declared in the v0.7.4 source.

```
def to_dict(self) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.msvc_metadata:UnwindCodeRecord.to_dict`

Metadata: public · line 154

### UnwindInfoRecord.to_dict

No function or method docstring is declared in the v0.7.4 source.

```
def to_dict(self) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.msvc_metadata:UnwindInfoRecord.to_dict`

Metadata: internal · line 173

### PEView.__init__

No function or method docstring is declared in the v0.7.4 source.

```
def __init__(self, path: Path)
```

**Catalog symbol:** `x86decomp.msvc_metadata:PEView.__init__`

Metadata: public · line 180

### PEView.rva_to_offset

No function or method docstring is declared in the v0.7.4 source.

```
def rva_to_offset(self, rva: int) -> int
```

**Catalog symbol:** `x86decomp.msvc_metadata:PEView.rva_to_offset`

Metadata: public · line 183

### PEView.valid_rva

No function or method docstring is declared in the v0.7.4 source.

```
def valid_rva(self, rva: int, size: int = 1) -> bool
```

**Catalog symbol:** `x86decomp.msvc_metadata:PEView.valid_rva`

Metadata: public · line 190

### PEView.read

No function or method docstring is declared in the v0.7.4 source.

```
def read(self, rva: int, size: int) -> bytes
```

**Catalog symbol:** `x86decomp.msvc_metadata:PEView.read`

Metadata: public · line 196

### PEView.u16

No function or method docstring is declared in the v0.7.4 source.

```
def u16(self, rva: int) -> int
```

**Catalog symbol:** `x86decomp.msvc_metadata:PEView.u16`

Metadata: public · line 199

### PEView.u32

No function or method docstring is declared in the v0.7.4 source.

```
def u32(self, rva: int) -> int
```

**Catalog symbol:** `x86decomp.msvc_metadata:PEView.u32`

Metadata: public · line 202

### PEView.i32

No function or method docstring is declared in the v0.7.4 source.

```
def i32(self, rva: int) -> int
```

**Catalog symbol:** `x86decomp.msvc_metadata:PEView.i32`

Metadata: public · line 205

### PEView.u64

No function or method docstring is declared in the v0.7.4 source.

```
def u64(self, rva: int) -> int
```

**Catalog symbol:** `x86decomp.msvc_metadata:PEView.u64`

Metadata: public · line 208

### PEView.pointer

No function or method docstring is declared in the v0.7.4 source.

```
def pointer(self, rva: int) -> int
```

**Catalog symbol:** `x86decomp.msvc_metadata:PEView.pointer`

Metadata: public · line 211

### PEView.va_to_rva

No function or method docstring is declared in the v0.7.4 source.

```
def va_to_rva(self, value: int) -> int | None
```

**Catalog symbol:** `x86decomp.msvc_metadata:PEView.va_to_rva`

Metadata: public · line 217

### PEView.encoded_pointer_to_rva

No function or method docstring is declared in the v0.7.4 source.

```
def encoded_pointer_to_rva(self, value: int) -> int | None
```

**Catalog symbol:** `x86decomp.msvc_metadata:PEView.encoded_pointer_to_rva`

Metadata: public · line 222

### PEView.c_string

No function or method docstring is declared in the v0.7.4 source.

```
def c_string(self, rva: int, limit: int = 4096) -> str
```

**Catalog symbol:** `x86decomp.msvc_metadata:PEView.c_string`

Metadata: public · line 229

### PEView.executable_rva

No function or method docstring is declared in the v0.7.4 source.

```
def executable_rva(self, rva: int) -> bool
```

**Catalog symbol:** `x86decomp.msvc_metadata:PEView.executable_rva`

Metadata: public · line 236

### PEView.readonly_data_sections

No function or method docstring is declared in the v0.7.4 source.

```
def readonly_data_sections(self) -> tuple[Section, ...]
```

**Catalog symbol:** `x86decomp.msvc_metadata:PEView.readonly_data_sections`

Metadata: internal · line 246

### _display_type_name

No function or method docstring is declared in the v0.7.4 source.

```
def _display_type_name(name: str) -> str
```

**Catalog symbol:** `x86decomp.msvc_metadata:_display_type_name`

Metadata: public · line 255

### scan_type_descriptors

No function or method docstring is declared in the v0.7.4 source.

```
def scan_type_descriptors(view: PEView) -> tuple[TypeDescriptorRecord, ...]
```

**Catalog symbol:** `x86decomp.msvc_metadata:scan_type_descriptors`

Metadata: internal · line 288

### _parse_base_class

No function or method docstring is declared in the v0.7.4 source.

```
def _parse_base_class(view: PEView, descriptor_rva: int, types: dict[int, TypeDescriptorRecord]) -> BaseClassRecord | None
```

**Catalog symbol:** `x86decomp.msvc_metadata:_parse_base_class`

Metadata: internal · line 323

### _parse_hierarchy

No function or method docstring is declared in the v0.7.4 source.

```
def _parse_hierarchy(view: PEView, hierarchy_rva: int, types: dict[int, TypeDescriptorRecord]) -> tuple[int, tuple[BaseClassRecord, ...]] | None
```

**Catalog symbol:** `x86decomp.msvc_metadata:_parse_hierarchy`

Metadata: public · line 352

### scan_complete_object_locators

No function or method docstring is declared in the v0.7.4 source.

```
def scan_complete_object_locators(view: PEView, type_descriptors: Iterable[TypeDescriptorRecord]) -> tuple[CompleteObjectLocatorRecord, ...]
```

**Catalog symbol:** `x86decomp.msvc_metadata:scan_complete_object_locators`

Metadata: public · line 397

### scan_vtables

No function or method docstring is declared in the v0.7.4 source.

```
def scan_vtables(view: PEView, locators: Iterable[CompleteObjectLocatorRecord]) -> tuple[VTableRecord, ...]
```

**Catalog symbol:** `x86decomp.msvc_metadata:scan_vtables`

Metadata: internal · line 450

### _decode_unwind_codes

No function or method docstring is declared in the v0.7.4 source.

```
def _decode_unwind_codes(view: PEView, rva: int, count: int) -> tuple[UnwindCodeRecord, ...]
```

**Catalog symbol:** `x86decomp.msvc_metadata:_decode_unwind_codes`

Metadata: public · line 508

### parse_x64_unwind

No function or method docstring is declared in the v0.7.4 source.

```
def parse_x64_unwind(view: PEView) -> tuple[UnwindInfoRecord, ...]
```

**Catalog symbol:** `x86decomp.msvc_metadata:parse_x64_unwind`

Metadata: public · line 564

### parse_safe_seh

No function or method docstring is declared in the v0.7.4 source.

```
def parse_safe_seh(view: PEView) -> tuple[int, ...]
```

**Catalog symbol:** `x86decomp.msvc_metadata:parse_safe_seh`

Metadata: public · line 577

### tls_report

No function or method docstring is declared in the v0.7.4 source.

```
def tls_report(view: PEView) -> dict[str, Any] | None
```

**Catalog symbol:** `x86decomp.msvc_metadata:tls_report`

Metadata: public · line 602

### scan_exception_func_info

Find structurally plausible MSVC EH3 FuncInfo records.

```
def scan_exception_func_info(view: PEView) -> tuple[dict[str, Any], ...]
```

**Catalog symbol:** `x86decomp.msvc_metadata:scan_exception_func_info`

Metadata: public · line 656

### scan_coff_tls

Inventory COFF TLS template and callback subsections.

```
def scan_coff_tls(*, object_paths: Iterable[Path] = ()) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.msvc_metadata:scan_coff_tls`

Metadata: public · line 695

### scan_static_initializers

No function or method docstring is declared in the v0.7.4 source.

```
def scan_static_initializers(*, object_paths: Iterable[Path] = (), map_path: Path | None = None) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.msvc_metadata:scan_static_initializers`

Metadata: public · line 748

### analyze_msvc_metadata

No function or method docstring is declared in the v0.7.4 source.

```
def analyze_msvc_metadata(pe_path: Path, *, object_paths: Iterable[Path] = (), map_path: Path | None = None, report_path: Path | None = None) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.msvc_metadata:analyze_msvc_metadata`
