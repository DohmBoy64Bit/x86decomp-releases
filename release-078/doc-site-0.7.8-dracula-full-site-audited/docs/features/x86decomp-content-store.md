---
title: x86decomp.content_store
description: Source module reference for x86decomp.content_store.
---

# `x86decomp.content_store`

**Source path:** `src/x86decomp/content_store.py`  
**SHA-256:** `2348ce9593959da0a9f52b144435a70b30965443a06e701c0ff9cf7c86e7d1a4`  
**Documented symbols:** 18

| Symbol | Kind | Line | End line | Docstring summary |
| --- | --- | ---: | ---: | --- |
| `StoredArtifact` | class | 23 | 42 | no docstring declared |
| `to_dict` | function | 29 | 42 | no docstring declared |
| `display` | function | 30 | 36 | no docstring declared |
| `ContentStore` | class | 45 | 254 | Immutable SHA-256 store rooted at ``root``. |
| `__init__` | function | 48 | 57 | no docstring declared |
| `_paths` | function | 59 | 63 | no docstring declared |
| `_validate_digest` | function | 66 | 68 | no docstring declared |
| `_locked` | function | 71 | 91 | Cross-process advisory lock using an exclusive lock file. |
| `put_bytes` | function | 93 | 124 | no docstring declared |
| `put_file` | function | 126 | 141 | no docstring declared |
| `get` | function | 143 | 148 | no docstring declared |
| `read_bytes` | function | 150 | 155 | no docstring declared |
| `add_reference` | function | 157 | 171 | no docstring declared |
| `remove_reference` | function | 173 | 179 | no docstring declared |
| `referenced_digests` | function | 181 | 186 | no docstring declared |
| `verify` | function | 188 | 217 | no docstring declared |
| `garbage_collect` | function | 219 | 244 | no docstring declared |
| `export_index` | function | 246 | 254 | no docstring declared |
