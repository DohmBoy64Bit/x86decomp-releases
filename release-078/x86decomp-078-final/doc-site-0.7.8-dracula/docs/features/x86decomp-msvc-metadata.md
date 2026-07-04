---
title: x86decomp.msvc_metadata
description: Source module reference for x86decomp.msvc_metadata.
---

# `x86decomp.msvc_metadata`

**Source path:** `src/x86decomp/msvc_metadata.py`  
**SHA-256:** `a09e12dd6d748ba39648bf05d885656080c1c03be63d8dde592e26cb36b72951`

| Symbol | Kind | Line | Body lines |
| --- | --- | ---: | --- |
| `TypeDescriptorRecord.to_dict` | method | 35 | 36 |
| `BaseClassRecord.to_dict` | method | 58 | 59 |
| `CompleteObjectLocatorRecord.to_dict` | method | 87 | 88 |
| `VTableRecord.to_dict` | method | 109 | 110 |
| `UnwindCodeRecord.to_dict` | method | 127 | 128 |
| `UnwindInfoRecord.to_dict` | method | 154 | 155 |
| `PEView.__init__` | method | 173 | 174, 175, 176, 177, 178 |
| `PEView.rva_to_offset` | method | 180 | 181 |
| `PEView.valid_rva` | method | 183 | 184, 188 |
| `PEView.read` | method | 190 | 191, 192, 194 |
| `PEView.u16` | method | 196 | 197 |
| `PEView.u32` | method | 199 | 200 |
| `PEView.i32` | method | 202 | 203 |
| `PEView.u64` | method | 205 | 206 |
| `PEView.pointer` | method | 208 | 209 |
| `PEView.va_to_rva` | method | 211 | 212, 214, 215 |
| `PEView.encoded_pointer_to_rva` | method | 217 | 218, 220 |
| `PEView.c_string` | method | 222 | 223, 224, 225, 227 |
| `PEView.executable_rva` | method | 229 | 230 |
| `PEView.readonly_data_sections` | method | 236 | 237 |
| `_display_type_name` | function | 246 | 247, 248, 250, 251, 252 |
| `scan_type_descriptors` | function | 255 | 256, 257, 258, 285 |
| `_parse_base_class` | function | 288 | 293, 295, 296, 297, 299, 300, 301, 302, 303, 304, 305, 310 |
| `_parse_hierarchy` | function | 323 | 328, 330, 331, 332, 333, 334, 335, 337, 339, 340, 349 |
| `scan_complete_object_locators` | function | 352 | 355, 356, 357, 358, 394 |
| `scan_vtables` | function | 397 | 400, 403, 404, 429 |
| `_decode_unwind_codes` | function | 450 | 451, 452, 453, 505 |
| `parse_x64_unwind` | function | 508 | 509, 511, 512, 561 |
| `parse_safe_seh` | function | 564 | 565, 566, 568, 570, 571, 573, 574 |
| `tls_report` | function | 577 | 578, 579, 581, 582, 583, 584, 587, 588, 589, 590 |
| `scan_exception_func_info` | function | 602 | 609, 610, 611, 652 |
| `scan_coff_tls` | function | 656 | 663, 664, 688, 689 |
| `scan_static_initializers` | function | 695 | 700, 701, 702, 721, 722, 723, 737, 738, 739 |
| `analyze_msvc_metadata` | function | 748 | 755, 756, 757, 758, 759, 760, 761, 762, 766, 767, 772, 773… |
