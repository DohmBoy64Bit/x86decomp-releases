---
title: x86decomp.msvc_metadata
description: Microsoft C++ metadata, unwind, TLS, and initializer recovery.
---

# `x86decomp.msvc_metadata`

Microsoft C++ metadata, unwind, TLS, and initializer recovery.

The scanner is intentionally conservative.  A record is returned only after its
internal pointers, counts, and section relationships pass structural checks.
RTTI layouts are derived from the Microsoft C++ ABI as emitted by Clang/MSVC;
these structures are not a promise that original source-level class names or
layouts have been fully recovered.

**Area:** Toolkit  
**Source:** `src/x86decomp/msvc_metadata.py`  
**SHA-256:** `a09e12dd6d748ba39648bf05d885656080c1c03be63d8dde592e26cb36b72951`  
**Functions/methods:** 34

> Module names, signatures, line numbers, and docstrings are extracted directly from the source AST. No behavior is inferred when a docstring is absent.

## Functions and methods

<a id="function-typedescriptorrecord-to-dict"></a>

### `TypeDescriptorRecord.to_dict`

No function or method docstring is declared in the 0.7.5 source.

```python
def TypeDescriptorRecord.to_dict(self) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.msvc_metadata:TypeDescriptorRecord.to_dict`  
**Visibility:** public  
**Source line:** 35

<a id="function-baseclassrecord-to-dict"></a>

### `BaseClassRecord.to_dict`

No function or method docstring is declared in the 0.7.5 source.

```python
def BaseClassRecord.to_dict(self) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.msvc_metadata:BaseClassRecord.to_dict`  
**Visibility:** public  
**Source line:** 58

<a id="function-completeobjectlocatorrecord-to-dict"></a>

### `CompleteObjectLocatorRecord.to_dict`

No function or method docstring is declared in the 0.7.5 source.

```python
def CompleteObjectLocatorRecord.to_dict(self) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.msvc_metadata:CompleteObjectLocatorRecord.to_dict`  
**Visibility:** public  
**Source line:** 87

<a id="function-vtablerecord-to-dict"></a>

### `VTableRecord.to_dict`

No function or method docstring is declared in the 0.7.5 source.

```python
def VTableRecord.to_dict(self) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.msvc_metadata:VTableRecord.to_dict`  
**Visibility:** public  
**Source line:** 109

<a id="function-unwindcoderecord-to-dict"></a>

### `UnwindCodeRecord.to_dict`

No function or method docstring is declared in the 0.7.5 source.

```python
def UnwindCodeRecord.to_dict(self) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.msvc_metadata:UnwindCodeRecord.to_dict`  
**Visibility:** public  
**Source line:** 127

<a id="function-unwindinforecord-to-dict"></a>

### `UnwindInfoRecord.to_dict`

No function or method docstring is declared in the 0.7.5 source.

```python
def UnwindInfoRecord.to_dict(self) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.msvc_metadata:UnwindInfoRecord.to_dict`  
**Visibility:** public  
**Source line:** 154

<a id="function-peview-init"></a>

### `PEView.__init__`

No function or method docstring is declared in the 0.7.5 source.

```python
def PEView.__init__(self, path: Path)
```

**Catalog symbol:** `x86decomp.msvc_metadata:PEView.__init__`  
**Visibility:** internal  
**Source line:** 173

<a id="function-peview-rva-to-offset"></a>

### `PEView.rva_to_offset`

No function or method docstring is declared in the 0.7.5 source.

```python
def PEView.rva_to_offset(self, rva: int) -> int
```

**Catalog symbol:** `x86decomp.msvc_metadata:PEView.rva_to_offset`  
**Visibility:** public  
**Source line:** 180

<a id="function-peview-valid-rva"></a>

### `PEView.valid_rva`

No function or method docstring is declared in the 0.7.5 source.

```python
def PEView.valid_rva(self, rva: int, size: int=1) -> bool
```

**Catalog symbol:** `x86decomp.msvc_metadata:PEView.valid_rva`  
**Visibility:** public  
**Source line:** 183

<a id="function-peview-read"></a>

### `PEView.read`

No function or method docstring is declared in the 0.7.5 source.

```python
def PEView.read(self, rva: int, size: int) -> bytes
```

**Catalog symbol:** `x86decomp.msvc_metadata:PEView.read`  
**Visibility:** public  
**Source line:** 190

<a id="function-peview-u16"></a>

### `PEView.u16`

No function or method docstring is declared in the 0.7.5 source.

```python
def PEView.u16(self, rva: int) -> int
```

**Catalog symbol:** `x86decomp.msvc_metadata:PEView.u16`  
**Visibility:** public  
**Source line:** 196

<a id="function-peview-u32"></a>

### `PEView.u32`

No function or method docstring is declared in the 0.7.5 source.

```python
def PEView.u32(self, rva: int) -> int
```

**Catalog symbol:** `x86decomp.msvc_metadata:PEView.u32`  
**Visibility:** public  
**Source line:** 199

<a id="function-peview-i32"></a>

### `PEView.i32`

No function or method docstring is declared in the 0.7.5 source.

```python
def PEView.i32(self, rva: int) -> int
```

**Catalog symbol:** `x86decomp.msvc_metadata:PEView.i32`  
**Visibility:** public  
**Source line:** 202

<a id="function-peview-u64"></a>

### `PEView.u64`

No function or method docstring is declared in the 0.7.5 source.

```python
def PEView.u64(self, rva: int) -> int
```

**Catalog symbol:** `x86decomp.msvc_metadata:PEView.u64`  
**Visibility:** public  
**Source line:** 205

<a id="function-peview-pointer"></a>

### `PEView.pointer`

No function or method docstring is declared in the 0.7.5 source.

```python
def PEView.pointer(self, rva: int) -> int
```

**Catalog symbol:** `x86decomp.msvc_metadata:PEView.pointer`  
**Visibility:** public  
**Source line:** 208

<a id="function-peview-va-to-rva"></a>

### `PEView.va_to_rva`

No function or method docstring is declared in the 0.7.5 source.

```python
def PEView.va_to_rva(self, value: int) -> int | None
```

**Catalog symbol:** `x86decomp.msvc_metadata:PEView.va_to_rva`  
**Visibility:** public  
**Source line:** 211

<a id="function-peview-encoded-pointer-to-rva"></a>

### `PEView.encoded_pointer_to_rva`

No function or method docstring is declared in the 0.7.5 source.

```python
def PEView.encoded_pointer_to_rva(self, value: int) -> int | None
```

**Catalog symbol:** `x86decomp.msvc_metadata:PEView.encoded_pointer_to_rva`  
**Visibility:** public  
**Source line:** 217

<a id="function-peview-c-string"></a>

### `PEView.c_string`

No function or method docstring is declared in the 0.7.5 source.

```python
def PEView.c_string(self, rva: int, limit: int=4096) -> str
```

**Catalog symbol:** `x86decomp.msvc_metadata:PEView.c_string`  
**Visibility:** public  
**Source line:** 222

<a id="function-peview-executable-rva"></a>

### `PEView.executable_rva`

No function or method docstring is declared in the 0.7.5 source.

```python
def PEView.executable_rva(self, rva: int) -> bool
```

**Catalog symbol:** `x86decomp.msvc_metadata:PEView.executable_rva`  
**Visibility:** public  
**Source line:** 229

<a id="function-peview-readonly-data-sections"></a>

### `PEView.readonly_data_sections`

No function or method docstring is declared in the 0.7.5 source.

```python
def PEView.readonly_data_sections(self) -> tuple[Section, ...]
```

**Catalog symbol:** `x86decomp.msvc_metadata:PEView.readonly_data_sections`  
**Visibility:** public  
**Source line:** 236

<a id="function-display-type-name"></a>

### `_display_type_name`

No function or method docstring is declared in the 0.7.5 source.

```python
def _display_type_name(name: str) -> str
```

**Catalog symbol:** `x86decomp.msvc_metadata:_display_type_name`  
**Visibility:** internal  
**Source line:** 246

<a id="function-scan-type-descriptors"></a>

### `scan_type_descriptors`

No function or method docstring is declared in the 0.7.5 source.

```python
def scan_type_descriptors(view: PEView) -> tuple[TypeDescriptorRecord, ...]
```

**Catalog symbol:** `x86decomp.msvc_metadata:scan_type_descriptors`  
**Visibility:** public  
**Source line:** 255

<a id="function-parse-base-class"></a>

### `_parse_base_class`

No function or method docstring is declared in the 0.7.5 source.

```python
def _parse_base_class(view: PEView, descriptor_rva: int, types: dict[int, TypeDescriptorRecord]) -> BaseClassRecord | None
```

**Catalog symbol:** `x86decomp.msvc_metadata:_parse_base_class`  
**Visibility:** internal  
**Source line:** 288

<a id="function-parse-hierarchy"></a>

### `_parse_hierarchy`

No function or method docstring is declared in the 0.7.5 source.

```python
def _parse_hierarchy(view: PEView, hierarchy_rva: int, types: dict[int, TypeDescriptorRecord]) -> tuple[int, tuple[BaseClassRecord, ...]] | None
```

**Catalog symbol:** `x86decomp.msvc_metadata:_parse_hierarchy`  
**Visibility:** internal  
**Source line:** 323

<a id="function-scan-complete-object-locators"></a>

### `scan_complete_object_locators`

No function or method docstring is declared in the 0.7.5 source.

```python
def scan_complete_object_locators(view: PEView, type_descriptors: Iterable[TypeDescriptorRecord]) -> tuple[CompleteObjectLocatorRecord, ...]
```

**Catalog symbol:** `x86decomp.msvc_metadata:scan_complete_object_locators`  
**Visibility:** public  
**Source line:** 352

<a id="function-scan-vtables"></a>

### `scan_vtables`

No function or method docstring is declared in the 0.7.5 source.

```python
def scan_vtables(view: PEView, locators: Iterable[CompleteObjectLocatorRecord]) -> tuple[VTableRecord, ...]
```

**Catalog symbol:** `x86decomp.msvc_metadata:scan_vtables`  
**Visibility:** public  
**Source line:** 397

<a id="function-decode-unwind-codes"></a>

### `_decode_unwind_codes`

No function or method docstring is declared in the 0.7.5 source.

```python
def _decode_unwind_codes(view: PEView, rva: int, count: int) -> tuple[UnwindCodeRecord, ...]
```

**Catalog symbol:** `x86decomp.msvc_metadata:_decode_unwind_codes`  
**Visibility:** internal  
**Source line:** 450

<a id="function-parse-x64-unwind"></a>

### `parse_x64_unwind`

No function or method docstring is declared in the 0.7.5 source.

```python
def parse_x64_unwind(view: PEView) -> tuple[UnwindInfoRecord, ...]
```

**Catalog symbol:** `x86decomp.msvc_metadata:parse_x64_unwind`  
**Visibility:** public  
**Source line:** 508

<a id="function-parse-safe-seh"></a>

### `parse_safe_seh`

No function or method docstring is declared in the 0.7.5 source.

```python
def parse_safe_seh(view: PEView) -> tuple[int, ...]
```

**Catalog symbol:** `x86decomp.msvc_metadata:parse_safe_seh`  
**Visibility:** public  
**Source line:** 564

<a id="function-tls-report"></a>

### `tls_report`

No function or method docstring is declared in the 0.7.5 source.

```python
def tls_report(view: PEView) -> dict[str, Any] | None
```

**Catalog symbol:** `x86decomp.msvc_metadata:tls_report`  
**Visibility:** public  
**Source line:** 577

<a id="function-scan-exception-func-info"></a>

### `scan_exception_func_info`

Find structurally plausible MSVC EH3 FuncInfo records.

The records are reported as candidates because handler-specific data layouts
vary by toolset and EH generation.  No source-level catch semantics are
asserted from this scan alone.

```python
def scan_exception_func_info(view: PEView) -> tuple[dict[str, Any], ...]
```

**Catalog symbol:** `x86decomp.msvc_metadata:scan_exception_func_info`  
**Visibility:** public  
**Source line:** 602

<a id="function-scan-coff-tls"></a>

### `scan_coff_tls`

Inventory COFF TLS template and callback subsections.

COFF subsection names and relocations are retained as linker evidence.  The
result does not claim the linked TLS directory or callback order unless a
linked image independently confirms it.

```python
def scan_coff_tls(*, object_paths: Iterable[Path]=()) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.msvc_metadata:scan_coff_tls`  
**Visibility:** public  
**Source line:** 656

<a id="function-scan-static-initializers"></a>

### `scan_static_initializers`

No function or method docstring is declared in the 0.7.5 source.

```python
def scan_static_initializers(*, object_paths: Iterable[Path]=(), map_path: Path | None=None) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.msvc_metadata:scan_static_initializers`  
**Visibility:** public  
**Source line:** 695

<a id="function-analyze-msvc-metadata"></a>

### `analyze_msvc_metadata`

No function or method docstring is declared in the 0.7.5 source.

```python
def analyze_msvc_metadata(pe_path: Path, *, object_paths: Iterable[Path]=(), map_path: Path | None=None, report_path: Path | None=None) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.msvc_metadata:analyze_msvc_metadata`  
**Visibility:** public  
**Source line:** 748
