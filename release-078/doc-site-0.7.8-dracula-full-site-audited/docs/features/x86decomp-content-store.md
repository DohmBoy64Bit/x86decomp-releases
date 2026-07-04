---
title: x86decomp.content_store
description: Source module reference for x86decomp.content_store.
---

# `x86decomp.content_store`

**Source path:** `src/x86decomp/content_store.py`  
**Documented symbols:** 18

| Symbol | Kind | Line | End line | Docstring summary |
| --- | --- | ---: | ---: | --- |
| `StoredArtifact` | class | 23 | 42 | — |
| `to_dict` | function | 29 | 42 | — |
| `display` | function | 30 | 36 | — |
| `ContentStore` | class | 45 | 254 | Immutable SHA-256 store rooted at ``root``. |
| `__init__` | function | 48 | 57 | — |
| `_paths` | function | 59 | 63 | — |
| `_validate_digest` | function | 66 | 68 | — |
| `_locked` | function | 71 | 91 | Cross-process advisory lock using an exclusive lock file. |
| `put_bytes` | function | 93 | 124 | — |
| `put_file` | function | 126 | 141 | — |
| `get` | function | 143 | 148 | — |
| `read_bytes` | function | 150 | 155 | — |
| `add_reference` | function | 157 | 171 | — |
| `remove_reference` | function | 173 | 179 | — |
| `referenced_digests` | function | 181 | 186 | — |
| `verify` | function | 188 | 217 | — |
| `garbage_collect` | function | 219 | 244 | — |
| `export_index` | function | 246 | 254 | — |
