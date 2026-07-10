---
title: x86decomp.content_store
description: Module reference for x86decomp.content_store.
---

# `x86decomp.content_store`

- Area: `toolkit`
- Source path: `src/x86decomp/content_store.py`
- SHA-256: `3a7dbe29ec407dff4966ae962ea4685141056fb57cfb8dc4ba84145547ec3a41`
- Size: `11713` bytes
- Lines: `270`

## Module docstring

Content-addressed immutable artifact storage.

Artifacts are addressed by SHA-256 and written atomically.  Metadata records
are immutable except for the separate reference index, which is transactionally
updated under an advisory file lock.  The store never executes artifacts.

## Symbols

| Kind | Name | Line | Docstring summary |
| --- | --- | --- | --- |
| class | `StoredArtifact` | 22 | Store validated stored artifact fields used by toolkit reports and adapters. |
| function | `to_dict` | 29 | Return a serializable dictionary representation. |
| function | `display` | 31 | Execute the display operation for the current toolkit workflow. |
| class | `ContentStore` | 47 | Immutable SHA-256 store rooted at ``root``. |
| function | `__init__` | 50 | Initialize the instance with validated constructor state. |
| function | `_paths` | 62 | Support paths processing for internal toolkit callers. |
| function | `_validate_digest` | 70 | Support validate digest processing for internal toolkit callers. |
| function | `_locked` | 76 | Cross-process advisory lock using an exclusive lock file. |
| function | `put_bytes` | 98 | Execute the put bytes operation for the current toolkit workflow. |
| function | `put_file` | 132 | Execute the put file operation for the current toolkit workflow. |
| function | `get` | 150 | Execute the get operation for the current toolkit workflow. |
| function | `read_bytes` | 158 | Read bytes for the current toolkit workflow. |
| function | `add_reference` | 166 | Execute the add reference operation for the current toolkit workflow. |
| function | `remove_reference` | 183 | Remove reference for the current toolkit workflow. |
| function | `referenced_digests` | 192 | Execute the referenced digests operation for the current toolkit workflow. |
| function | `verify` | 200 | Verify verify for the current toolkit workflow. |
| function | `garbage_collect` | 232 | Execute the garbage collect operation for the current toolkit workflow. |
| function | `export_index` | 260 | Execute the export index operation for the current toolkit workflow. |
