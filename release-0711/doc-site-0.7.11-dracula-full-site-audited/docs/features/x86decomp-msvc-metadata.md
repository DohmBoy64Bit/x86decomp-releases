---
title: x86decomp.msvc_metadata
description: Module reference for x86decomp.msvc_metadata.
---

# `x86decomp.msvc_metadata`

- Area: `toolkit`
- Source path: `src/x86decomp/msvc_metadata.py`
- SHA-256: `00acf48e912266dd7142f7b98ad81f218bfed88f8e5276b1bd80037afb681a12`
- Size: `34420` bytes
- Lines: `844`

## Module docstring

Microsoft C++ metadata, unwind, TLS, and initializer recovery.

The scanner is intentionally conservative.  A record is returned only after its
internal pointers, counts, and section relationships pass structural checks.
RTTI layouts are derived from the Microsoft C++ ABI as emitted by Clang/MSVC;
these structures are not a promise that original source-level class names or
layouts have been fully recovered.

## Symbols

| Kind | Name | Line | Docstring summary |
| --- | --- | --- | --- |
| class | `TypeDescriptorRecord` | 27 | Store validated type descriptor record fields used by toolkit reports and adapters. |
| function | `to_dict` | 36 | Return a serializable dictionary representation. |
| class | `BaseClassRecord` | 49 | Store validated base class record fields used by toolkit reports and adapters. |
| function | `to_dict` | 61 | Return a serializable dictionary representation. |
| class | `CompleteObjectLocatorRecord` | 79 | Store validated complete object locator record fields used by toolkit reports and adapters. |
| function | `to_dict` | 92 | Return a serializable dictionary representation. |
| class | `VTableRecord` | 109 | Store validated v table record fields used by toolkit reports and adapters. |
| function | `to_dict` | 116 | Return a serializable dictionary representation. |
| class | `UnwindCodeRecord` | 127 | Store validated unwind code record fields used by toolkit reports and adapters. |
| function | `to_dict` | 136 | Return a serializable dictionary representation. |
| class | `UnwindInfoRecord` | 149 | Store validated unwind info record fields used by toolkit reports and adapters. |
| function | `to_dict` | 165 | Return a serializable dictionary representation. |
| class | `PEView` | 184 | Coordinate p e view behavior for the current toolkit workflow. |
| function | `__init__` | 186 | Initialize the instance with validated constructor state. |
| function | `rva_to_offset` | 194 | Execute the rva to offset operation for the current toolkit workflow. |
| function | `valid_rva` | 198 | Execute the valid rva operation for the current toolkit workflow. |
| function | `read` | 206 | Read read for the current toolkit workflow. |
| function | `u16` | 213 | Execute the u16 operation for the current toolkit workflow. |
| function | `u32` | 217 | Execute the u32 operation for the current toolkit workflow. |
| function | `i32` | 221 | Execute the i32 operation for the current toolkit workflow. |
| function | `u64` | 225 | Execute the u64 operation for the current toolkit workflow. |
| function | `pointer` | 229 | Execute the pointer operation for the current toolkit workflow. |
| function | `va_to_rva` | 233 | Execute the va to rva operation for the current toolkit workflow. |
| function | `encoded_pointer_to_rva` | 240 | Encode d pointer to rva for the current toolkit workflow. |
| function | `c_string` | 246 | Execute the c string operation for the current toolkit workflow. |
| function | `executable_rva` | 254 | Execute the executable rva operation for the current toolkit workflow. |
| function | `readonly_data_sections` | 262 | Read only data sections for the current toolkit workflow. |
| function | `_display_type_name` | 273 | Support display type name processing for internal toolkit callers. |
| function | `scan_type_descriptors` | 283 | Execute the scan type descriptors operation for the current toolkit workflow. |
| function | `_parse_base_class` | 317 | Support parse base class processing for internal toolkit callers. |
| function | `_parse_hierarchy` | 353 | Support parse hierarchy processing for internal toolkit callers. |
| function | `scan_complete_object_locators` | 383 | Execute the scan complete object locators operation for the current toolkit workflow. |
| function | `scan_vtables` | 429 | Execute the scan vtables operation for the current toolkit workflow. |
| function | `_decode_unwind_codes` | 483 | Support decode unwind codes processing for internal toolkit callers. |
| function | `parse_x64_unwind` | 542 | Parse x64 unwind for the current toolkit workflow. |
| function | `parse_safe_seh` | 599 | Parse safe seh for the current toolkit workflow. |
| function | `tls_report` | 613 | Execute the tls report operation for the current toolkit workflow. |
| function | `scan_exception_func_info` | 639 | Find structurally plausible MSVC EH3 FuncInfo records. |
| function | `scan_coff_tls` | 693 | Inventory COFF TLS template and callback subsections. |
| function | `scan_static_initializers` | 732 | Execute the scan static initializers operation for the current toolkit workflow. |
| function | `analyze_msvc_metadata` | 786 | Execute the analyze msvc metadata operation for the current toolkit workflow. |
