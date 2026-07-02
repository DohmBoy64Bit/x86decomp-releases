---
title: x86decomp.content_store
description: Content-addressed immutable artifact storage.
original_path: features/x86decomp-content-store.html
---

<a id="function-storedartifact-to-dict"></a>
<a id="function-contentstore-init"></a>
<a id="function-contentstore-paths"></a>
<a id="function-contentstore-validate-digest"></a>
<a id="function-contentstore-locked"></a>
<a id="function-contentstore-put-bytes"></a>
<a id="function-contentstore-put-file"></a>
<a id="function-contentstore-get"></a>
<a id="function-contentstore-read-bytes"></a>
<a id="function-contentstore-add-reference"></a>
<a id="function-contentstore-remove-reference"></a>
<a id="function-contentstore-referenced-digests"></a>
<a id="function-contentstore-verify"></a>
<a id="function-contentstore-garbage-collect"></a>
<a id="function-contentstore-export-index"></a>

Section: Source-derived feature and function reference

# x86decomp.content_store

Content-addressed immutable artifact storage.

Metadata: core · current · 15 functions/methods

**Source:** `src/x86decomp/content_store.py`

> **Truth basis.** Module and symbol names, signatures, line numbers, docstrings, and SHA-256 are read directly from the sealed source. When source docstrings are absent, this page says so instead of inferring behavior. Source SHA-256: `4902a167d8d42224690983536869b729211920840f539ad038d67a587c98001a`.

## Functions and methods

Metadata: public · line 29

### StoredArtifact.to_dict

No function or method docstring is declared in the v0.7.4 source.

```
def to_dict(self, *, root: Path | None = None) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.content_store:StoredArtifact.to_dict`

Metadata: internal · line 48

### ContentStore.__init__

No function or method docstring is declared in the v0.7.4 source.

```
def __init__(self, root: Path)
```

**Catalog symbol:** `x86decomp.content_store:ContentStore.__init__`

Metadata: internal · line 59

### ContentStore._paths

No function or method docstring is declared in the v0.7.4 source.

```
def _paths(self, digest: str) -> tuple[Path, Path]
```

**Catalog symbol:** `x86decomp.content_store:ContentStore._paths`

Metadata: internal · line 66

### ContentStore._validate_digest

No function or method docstring is declared in the v0.7.4 source.

```
def _validate_digest(digest: str) -> None
```

**Catalog symbol:** `x86decomp.content_store:ContentStore._validate_digest`

Metadata: internal · line 71

### ContentStore._locked

Cross-process advisory lock using an exclusive lock file.

```
def _locked(self) -> Iterator[None]
```

**Catalog symbol:** `x86decomp.content_store:ContentStore._locked`

Metadata: public · line 93

### ContentStore.put_bytes

No function or method docstring is declared in the v0.7.4 source.

```
def put_bytes(self, data: bytes, *, media_type: str = 'application/octet-stream', source: str | None = None, attributes: dict[str, Any] | None = None) -> StoredArtifact
```

**Catalog symbol:** `x86decomp.content_store:ContentStore.put_bytes`

Metadata: public · line 126

### ContentStore.put_file

No function or method docstring is declared in the v0.7.4 source.

```
def put_file(self, path: Path, *, media_type: str = 'application/octet-stream', attributes: dict[str, Any] | None = None) -> StoredArtifact
```

**Catalog symbol:** `x86decomp.content_store:ContentStore.put_file`

Metadata: public · line 143

### ContentStore.get

No function or method docstring is declared in the v0.7.4 source.

```
def get(self, digest: str) -> StoredArtifact
```

**Catalog symbol:** `x86decomp.content_store:ContentStore.get`

Metadata: public · line 150

### ContentStore.read_bytes

No function or method docstring is declared in the v0.7.4 source.

```
def read_bytes(self, digest: str) -> bytes
```

**Catalog symbol:** `x86decomp.content_store:ContentStore.read_bytes`

Metadata: public · line 157

### ContentStore.add_reference

No function or method docstring is declared in the v0.7.4 source.

```
def add_reference(self, reference: str, digest: str, *, kind: str, owner: str) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.content_store:ContentStore.add_reference`

Metadata: public · line 173

### ContentStore.remove_reference

No function or method docstring is declared in the v0.7.4 source.

```
def remove_reference(self, reference: str) -> bool
```

**Catalog symbol:** `x86decomp.content_store:ContentStore.remove_reference`

Metadata: public · line 181

### ContentStore.referenced_digests

No function or method docstring is declared in the v0.7.4 source.

```
def referenced_digests(self) -> set[str]
```

**Catalog symbol:** `x86decomp.content_store:ContentStore.referenced_digests`

Metadata: public · line 188

### ContentStore.verify

No function or method docstring is declared in the v0.7.4 source.

```
def verify(self) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.content_store:ContentStore.verify`

Metadata: public · line 219

### ContentStore.garbage_collect

No function or method docstring is declared in the v0.7.4 source.

```
def garbage_collect(self, *, dry_run: bool = True) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.content_store:ContentStore.garbage_collect`

Metadata: public · line 246

### ContentStore.export_index

No function or method docstring is declared in the v0.7.4 source.

```
def export_index(self) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.content_store:ContentStore.export_index`
