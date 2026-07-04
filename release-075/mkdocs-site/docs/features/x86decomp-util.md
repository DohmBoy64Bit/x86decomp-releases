---
title: x86decomp.util
description: Small, dependency-free utilities shared by all modules.
---

# `x86decomp.util`

Small, dependency-free utilities shared by all modules.

**Area:** Toolkit  
**Source:** `src/x86decomp/util.py`  
**SHA-256:** `f38c92cec5d269f8597282a84f5cfb76dd9e952cedb3606be592e8f5f89d8fe1`  
**Functions/methods:** 13

> Module names, signatures, line numbers, and docstrings are extracted directly from the source AST. No behavior is inferred when a docstring is absent.

## Functions and methods

<a id="function-utc-now"></a>

### `utc_now`

Return a stable RFC 3339 UTC timestamp.

```python
def utc_now() -> str
```

**Catalog symbol:** `x86decomp.util:utc_now`  
**Visibility:** public  
**Source line:** 17

<a id="function-sha256-bytes"></a>

### `sha256_bytes`

No function or method docstring is declared in the 0.7.5 source.

```python
def sha256_bytes(data: bytes) -> str
```

**Catalog symbol:** `x86decomp.util:sha256_bytes`  
**Visibility:** public  
**Source line:** 22

<a id="function-sha256-file"></a>

### `sha256_file`

No function or method docstring is declared in the 0.7.5 source.

```python
def sha256_file(path: Path, chunk_size: int=1024 * 1024) -> str
```

**Catalog symbol:** `x86decomp.util:sha256_file`  
**Visibility:** public  
**Source line:** 26

<a id="function-canonical-json-bytes"></a>

### `canonical_json_bytes`

No function or method docstring is declared in the 0.7.5 source.

```python
def canonical_json_bytes(value: Any) -> bytes
```

**Catalog symbol:** `x86decomp.util:canonical_json_bytes`  
**Visibility:** public  
**Source line:** 34

<a id="function-load-json"></a>

### `load_json`

No function or method docstring is declared in the 0.7.5 source.

```python
def load_json(path: Path) -> Any
```

**Catalog symbol:** `x86decomp.util:load_json`  
**Visibility:** public  
**Source line:** 40

<a id="function-atomic-write-bytes"></a>

### `atomic_write_bytes`

No function or method docstring is declared in the 0.7.5 source.

```python
def atomic_write_bytes(path: Path, data: bytes) -> None
```

**Catalog symbol:** `x86decomp.util:atomic_write_bytes`  
**Visibility:** public  
**Source line:** 45

<a id="function-atomic-write-text"></a>

### `atomic_write_text`

No function or method docstring is declared in the 0.7.5 source.

```python
def atomic_write_text(path: Path, text: str) -> None
```

**Catalog symbol:** `x86decomp.util:atomic_write_text`  
**Visibility:** public  
**Source line:** 61

<a id="function-write-json"></a>

### `write_json`

No function or method docstring is declared in the 0.7.5 source.

```python
def write_json(path: Path, value: Any) -> None
```

**Catalog symbol:** `x86decomp.util:write_json`  
**Visibility:** public  
**Source line:** 65

<a id="function-copy-file-atomic"></a>

### `copy_file_atomic`

No function or method docstring is declared in the 0.7.5 source.

```python
def copy_file_atomic(source: Path, destination: Path) -> None
```

**Catalog symbol:** `x86decomp.util:copy_file_atomic`  
**Visibility:** public  
**Source line:** 70

<a id="function-ensure-relative-path"></a>

### `ensure_relative_path`

Resolve candidate and reject paths that escape root.

```python
def ensure_relative_path(root: Path, candidate: Path) -> Path
```

**Catalog symbol:** `x86decomp.util:ensure_relative_path`  
**Visibility:** public  
**Source line:** 84

<a id="function-require-mapping"></a>

### `require_mapping`

No function or method docstring is declared in the 0.7.5 source.

```python
def require_mapping(value: Any, name: str) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.util:require_mapping`  
**Visibility:** public  
**Source line:** 95

<a id="function-require-string"></a>

### `require_string`

No function or method docstring is declared in the 0.7.5 source.

```python
def require_string(mapping: dict[str, Any], key: str, *, nonempty: bool=True) -> str
```

**Catalog symbol:** `x86decomp.util:require_string`  
**Visibility:** public  
**Source line:** 101

<a id="function-require-int"></a>

### `require_int`

No function or method docstring is declared in the 0.7.5 source.

```python
def require_int(mapping: dict[str, Any], key: str, *, minimum: int | None=None) -> int
```

**Catalog symbol:** `x86decomp.util:require_int`  
**Visibility:** public  
**Source line:** 108
