---
title: x86decomp.msvc_metadata
description: Source module reference for x86decomp.msvc_metadata.
---

# `x86decomp.msvc_metadata`

**Source path:** `src/x86decomp/msvc_metadata.py`  
**SHA-256:** `a09e12dd6d748ba39648bf05d885656080c1c03be63d8dde592e26cb36b72951`  
**Documented symbols:** 41

| Symbol | Kind | Line | End line | Docstring summary |
| --- | --- | ---: | ---: | --- |
| `TypeDescriptorRecord` | class | 27 | 43 | no docstring declared |
| `to_dict` | function | 35 | 43 | no docstring declared |
| `BaseClassRecord` | class | 47 | 71 | no docstring declared |
| `to_dict` | function | 58 | 71 | no docstring declared |
| `CompleteObjectLocatorRecord` | class | 75 | 99 | no docstring declared |
| `to_dict` | function | 87 | 99 | no docstring declared |
| `VTableRecord` | class | 103 | 115 | no docstring declared |
| `to_dict` | function | 109 | 115 | no docstring declared |
| `UnwindCodeRecord` | class | 119 | 135 | no docstring declared |
| `to_dict` | function | 127 | 135 | no docstring declared |
| `UnwindInfoRecord` | class | 139 | 169 | no docstring declared |
| `to_dict` | function | 154 | 169 | no docstring declared |
| `PEView` | class | 172 | 243 | no docstring declared |
| `__init__` | function | 173 | 178 | no docstring declared |
| `rva_to_offset` | function | 180 | 181 | no docstring declared |
| `valid_rva` | function | 183 | 188 | no docstring declared |
| `read` | function | 190 | 194 | no docstring declared |
| `u16` | function | 196 | 197 | no docstring declared |
| `u32` | function | 199 | 200 | no docstring declared |
| `i32` | function | 202 | 203 | no docstring declared |
| `u64` | function | 205 | 206 | no docstring declared |
| `pointer` | function | 208 | 209 | no docstring declared |
| `va_to_rva` | function | 211 | 215 | no docstring declared |
| `encoded_pointer_to_rva` | function | 217 | 220 | no docstring declared |
| `c_string` | function | 222 | 227 | no docstring declared |
| `executable_rva` | function | 229 | 234 | no docstring declared |
| `readonly_data_sections` | function | 236 | 243 | no docstring declared |
| `_display_type_name` | function | 246 | 252 | no docstring declared |
| `scan_type_descriptors` | function | 255 | 285 | no docstring declared |
| `_parse_base_class` | function | 288 | 320 | no docstring declared |
| `_parse_hierarchy` | function | 323 | 349 | no docstring declared |
| `scan_complete_object_locators` | function | 352 | 394 | no docstring declared |
| `scan_vtables` | function | 397 | 429 | no docstring declared |
| `_decode_unwind_codes` | function | 450 | 505 | no docstring declared |
| `parse_x64_unwind` | function | 508 | 561 | no docstring declared |
| `parse_safe_seh` | function | 564 | 574 | no docstring declared |
| `tls_report` | function | 577 | 599 | no docstring declared |
| `scan_exception_func_info` | function | 602 | 652 | Find structurally plausible MSVC EH3 FuncInfo records. |
| `scan_coff_tls` | function | 656 | 693 | Inventory COFF TLS template and callback subsections. |
| `scan_static_initializers` | function | 695 | 745 | no docstring declared |
| `analyze_msvc_metadata` | function | 748 | 804 | no docstring declared |
