---
title: x86decomp.util
description: Small, dependency-free utilities shared by all modules.
original_path: features/x86decomp-util.html
---

<a id="function-utc-now"></a>
<a id="function-sha256-bytes"></a>
<a id="function-sha256-file"></a>
<a id="function-canonical-json-bytes"></a>
<a id="function-load-json"></a>
<a id="function-atomic-write-bytes"></a>
<a id="function-atomic-write-text"></a>
<a id="function-write-json"></a>
<a id="function-copy-file-atomic"></a>
<a id="function-ensure-relative-path"></a>
<a id="function-require-mapping"></a>
<a id="function-require-string"></a>
<a id="function-require-int"></a>

Section: Source-derived feature and function reference

# x86decomp.util

Small, dependency-free utilities shared by all modules.

Metadata: core · current · 13 functions/methods

**Source:** `src/x86decomp/util.py`

> **Truth basis.** Module and symbol names, signatures, line numbers, docstrings, and SHA-256 are read directly from the sealed source. When source docstrings are absent, this page says so instead of inferring behavior. Source SHA-256: `f38c92cec5d269f8597282a84f5cfb76dd9e952cedb3606be592e8f5f89d8fe1`.

## Functions and methods

Metadata: public · line 17

### utc_now

Return a stable RFC 3339 UTC timestamp.

```
def utc_now() -> str
```

**Catalog symbol:** `x86decomp.util:utc_now`

Metadata: public · line 22

### sha256_bytes

No function or method docstring is declared in the v0.7.4 source.

```
def sha256_bytes(data: bytes) -> str
```

**Catalog symbol:** `x86decomp.util:sha256_bytes`

Metadata: public · line 26

### sha256_file

No function or method docstring is declared in the v0.7.4 source.

```
def sha256_file(path: Path, chunk_size: int = 1024 * 1024) -> str
```

**Catalog symbol:** `x86decomp.util:sha256_file`

Metadata: public · line 34

### canonical_json_bytes

No function or method docstring is declared in the v0.7.4 source.

```
def canonical_json_bytes(value: Any) -> bytes
```

**Catalog symbol:** `x86decomp.util:canonical_json_bytes`

Metadata: public · line 40

### load_json

No function or method docstring is declared in the v0.7.4 source.

```
def load_json(path: Path) -> Any
```

**Catalog symbol:** `x86decomp.util:load_json`

Metadata: public · line 45

### atomic_write_bytes

No function or method docstring is declared in the v0.7.4 source.

```
def atomic_write_bytes(path: Path, data: bytes) -> None
```

**Catalog symbol:** `x86decomp.util:atomic_write_bytes`

Metadata: public · line 61

### atomic_write_text

No function or method docstring is declared in the v0.7.4 source.

```
def atomic_write_text(path: Path, text: str) -> None
```

**Catalog symbol:** `x86decomp.util:atomic_write_text`

Metadata: public · line 65

### write_json

No function or method docstring is declared in the v0.7.4 source.

```
def write_json(path: Path, value: Any) -> None
```

**Catalog symbol:** `x86decomp.util:write_json`

Metadata: public · line 70

### copy_file_atomic

No function or method docstring is declared in the v0.7.4 source.

```
def copy_file_atomic(source: Path, destination: Path) -> None
```

**Catalog symbol:** `x86decomp.util:copy_file_atomic`

Metadata: public · line 84

### ensure_relative_path

Resolve candidate and reject paths that escape root.

```
def ensure_relative_path(root: Path, candidate: Path) -> Path
```

**Catalog symbol:** `x86decomp.util:ensure_relative_path`

Metadata: public · line 95

### require_mapping

No function or method docstring is declared in the v0.7.4 source.

```
def require_mapping(value: Any, name: str) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.util:require_mapping`

Metadata: public · line 101

### require_string

No function or method docstring is declared in the v0.7.4 source.

```
def require_string(mapping: dict[str, Any], key: str, *, nonempty: bool = True) -> str
```

**Catalog symbol:** `x86decomp.util:require_string`

Metadata: public · line 108

### require_int

No function or method docstring is declared in the v0.7.4 source.

```
def require_int(mapping: dict[str, Any], key: str, *, minimum: int | None = None) -> int
```

**Catalog symbol:** `x86decomp.util:require_int`
