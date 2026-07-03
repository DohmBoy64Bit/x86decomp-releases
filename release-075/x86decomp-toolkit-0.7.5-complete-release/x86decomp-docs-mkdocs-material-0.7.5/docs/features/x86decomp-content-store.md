---
title: x86decomp.content_store
description: Content-addressed immutable artifact storage.
---

# `x86decomp.content_store`

Content-addressed immutable artifact storage.

Artifacts are addressed by SHA-256 and written atomically.  Metadata records
are immutable except for the separate reference index, which is transactionally
updated under an advisory file lock.  The store never executes artifacts.

**Area:** Toolkit  
**Source:** `src/x86decomp/content_store.py`  
**SHA-256:** `2348ce9593959da0a9f52b144435a70b30965443a06e701c0ff9cf7c86e7d1a4`  
**Functions/methods:** 15

> Module names, signatures, line numbers, and docstrings are extracted directly from the source AST. No behavior is inferred when a docstring is absent.

## Functions and methods

<a id="function-storedartifact-to-dict"></a>

### `StoredArtifact.to_dict`

No function or method docstring is declared in the 0.7.5 source.

```python
def StoredArtifact.to_dict(self, *, root: Path | None=None) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.content_store:StoredArtifact.to_dict`  
**Visibility:** public  
**Source line:** 29

<a id="function-contentstore-init"></a>

### `ContentStore.__init__`

No function or method docstring is declared in the 0.7.5 source.

```python
def ContentStore.__init__(self, root: Path)
```

**Catalog symbol:** `x86decomp.content_store:ContentStore.__init__`  
**Visibility:** internal  
**Source line:** 48

<a id="function-contentstore-paths"></a>

### `ContentStore._paths`

No function or method docstring is declared in the 0.7.5 source.

```python
def ContentStore._paths(self, digest: str) -> tuple[Path, Path]
```

**Catalog symbol:** `x86decomp.content_store:ContentStore._paths`  
**Visibility:** internal  
**Source line:** 59

<a id="function-contentstore-validate-digest"></a>

### `ContentStore._validate_digest`

No function or method docstring is declared in the 0.7.5 source.

```python
def ContentStore._validate_digest(digest: str) -> None
```

**Catalog symbol:** `x86decomp.content_store:ContentStore._validate_digest`  
**Visibility:** internal  
**Source line:** 66

<a id="function-contentstore-locked"></a>

### `ContentStore._locked`

Cross-process advisory lock using an exclusive lock file.

The lock is intentionally simple and portable.  A stale lock is never
silently removed; callers receive a clear error and may inspect it.

```python
def ContentStore._locked(self) -> Iterator[None]
```

**Catalog symbol:** `x86decomp.content_store:ContentStore._locked`  
**Visibility:** internal  
**Source line:** 71

<a id="function-contentstore-put-bytes"></a>

### `ContentStore.put_bytes`

No function or method docstring is declared in the 0.7.5 source.

```python
def ContentStore.put_bytes(self, data: bytes, *, media_type: str='application/octet-stream', source: str | None=None, attributes: dict[str, Any] | None=None) -> StoredArtifact
```

**Catalog symbol:** `x86decomp.content_store:ContentStore.put_bytes`  
**Visibility:** public  
**Source line:** 93

<a id="function-contentstore-put-file"></a>

### `ContentStore.put_file`

No function or method docstring is declared in the 0.7.5 source.

```python
def ContentStore.put_file(self, path: Path, *, media_type: str='application/octet-stream', attributes: dict[str, Any] | None=None) -> StoredArtifact
```

**Catalog symbol:** `x86decomp.content_store:ContentStore.put_file`  
**Visibility:** public  
**Source line:** 126

<a id="function-contentstore-get"></a>

### `ContentStore.get`

No function or method docstring is declared in the 0.7.5 source.

```python
def ContentStore.get(self, digest: str) -> StoredArtifact
```

**Catalog symbol:** `x86decomp.content_store:ContentStore.get`  
**Visibility:** public  
**Source line:** 143

<a id="function-contentstore-read-bytes"></a>

### `ContentStore.read_bytes`

No function or method docstring is declared in the 0.7.5 source.

```python
def ContentStore.read_bytes(self, digest: str) -> bytes
```

**Catalog symbol:** `x86decomp.content_store:ContentStore.read_bytes`  
**Visibility:** public  
**Source line:** 150

<a id="function-contentstore-add-reference"></a>

### `ContentStore.add_reference`

No function or method docstring is declared in the 0.7.5 source.

```python
def ContentStore.add_reference(self, reference: str, digest: str, *, kind: str, owner: str) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.content_store:ContentStore.add_reference`  
**Visibility:** public  
**Source line:** 157

<a id="function-contentstore-remove-reference"></a>

### `ContentStore.remove_reference`

No function or method docstring is declared in the 0.7.5 source.

```python
def ContentStore.remove_reference(self, reference: str) -> bool
```

**Catalog symbol:** `x86decomp.content_store:ContentStore.remove_reference`  
**Visibility:** public  
**Source line:** 173

<a id="function-contentstore-referenced-digests"></a>

### `ContentStore.referenced_digests`

No function or method docstring is declared in the 0.7.5 source.

```python
def ContentStore.referenced_digests(self) -> set[str]
```

**Catalog symbol:** `x86decomp.content_store:ContentStore.referenced_digests`  
**Visibility:** public  
**Source line:** 181

<a id="function-contentstore-verify"></a>

### `ContentStore.verify`

No function or method docstring is declared in the 0.7.5 source.

```python
def ContentStore.verify(self) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.content_store:ContentStore.verify`  
**Visibility:** public  
**Source line:** 188

<a id="function-contentstore-garbage-collect"></a>

### `ContentStore.garbage_collect`

No function or method docstring is declared in the 0.7.5 source.

```python
def ContentStore.garbage_collect(self, *, dry_run: bool=True) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.content_store:ContentStore.garbage_collect`  
**Visibility:** public  
**Source line:** 219

<a id="function-contentstore-export-index"></a>

### `ContentStore.export_index`

No function or method docstring is declared in the 0.7.5 source.

```python
def ContentStore.export_index(self) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.content_store:ContentStore.export_index`  
**Visibility:** public  
**Source line:** 246
