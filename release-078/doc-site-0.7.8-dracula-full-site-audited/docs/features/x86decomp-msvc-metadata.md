---
title: x86decomp.msvc_metadata
description: Source module reference for x86decomp.msvc_metadata.
---

# `x86decomp.msvc_metadata`

**Source path:** `src/x86decomp/msvc_metadata.py`  
**Documented symbols:** 41

| Symbol | Kind | Line | End line | Docstring summary |
| --- | --- | ---: | ---: | --- |
| `TypeDescriptorRecord` | class | 27 | 43 | — |
| `to_dict` | function | 35 | 43 | — |
| `BaseClassRecord` | class | 47 | 71 | — |
| `to_dict` | function | 58 | 71 | — |
| `CompleteObjectLocatorRecord` | class | 75 | 99 | — |
| `to_dict` | function | 87 | 99 | — |
| `VTableRecord` | class | 103 | 115 | — |
| `to_dict` | function | 109 | 115 | — |
| `UnwindCodeRecord` | class | 119 | 135 | — |
| `to_dict` | function | 127 | 135 | — |
| `UnwindInfoRecord` | class | 139 | 169 | — |
| `to_dict` | function | 154 | 169 | — |
| `PEView` | class | 172 | 243 | — |
| `__init__` | function | 173 | 178 | — |
| `rva_to_offset` | function | 180 | 181 | — |
| `valid_rva` | function | 183 | 188 | — |
| `read` | function | 190 | 194 | — |
| `u16` | function | 196 | 197 | — |
| `u32` | function | 199 | 200 | — |
| `i32` | function | 202 | 203 | — |
| `u64` | function | 205 | 206 | — |
| `pointer` | function | 208 | 209 | — |
| `va_to_rva` | function | 211 | 215 | — |
| `encoded_pointer_to_rva` | function | 217 | 220 | — |
| `c_string` | function | 222 | 227 | — |
| `executable_rva` | function | 229 | 234 | — |
| `readonly_data_sections` | function | 236 | 243 | — |
| `_display_type_name` | function | 246 | 252 | — |
| `scan_type_descriptors` | function | 255 | 285 | — |
| `_parse_base_class` | function | 288 | 320 | — |
| `_parse_hierarchy` | function | 323 | 349 | — |
| `scan_complete_object_locators` | function | 352 | 394 | — |
| `scan_vtables` | function | 397 | 429 | — |
| `_decode_unwind_codes` | function | 450 | 505 | — |
| `parse_x64_unwind` | function | 508 | 561 | — |
| `parse_safe_seh` | function | 564 | 574 | — |
| `tls_report` | function | 577 | 599 | — |
| `scan_exception_func_info` | function | 602 | 652 | Find structurally plausible MSVC EH3 FuncInfo records. |
| `scan_coff_tls` | function | 656 | 693 | Inventory COFF TLS template and callback subsections. |
| `scan_static_initializers` | function | 695 | 745 | — |
| `analyze_msvc_metadata` | function | 748 | 804 | — |
