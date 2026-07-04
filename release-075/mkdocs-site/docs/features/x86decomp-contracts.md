---
title: x86decomp.contracts
description: No module docstring is declared in the 0.7.5 source.
---

# `x86decomp.contracts`

No module docstring is declared in the 0.7.5 source.

**Area:** Toolkit  
**Source:** `src/x86decomp/contracts.py`  
**SHA-256:** `59ed708757edb48209337ba38008c4522cd03106686c9b47b08da0b2a32e98ed`  
**Functions/methods:** 12

> Module names, signatures, line numbers, and docstrings are extracted directly from the source AST. No behavior is inferred when a docstring is absent.

## Functions and methods

<a id="function-utc-now"></a>

### `utc_now`

No function or method docstring is declared in the 0.7.5 source.

```python
def utc_now() -> str
```

**Catalog symbol:** `x86decomp.contracts:utc_now`  
**Visibility:** public  
**Source line:** 20

<a id="function-canonical-json"></a>

### `canonical_json`

No function or method docstring is declared in the 0.7.5 source.

```python
def canonical_json(value: Any) -> str
```

**Catalog symbol:** `x86decomp.contracts:canonical_json`  
**Visibility:** public  
**Source line:** 24

<a id="function-sha256-bytes"></a>

### `sha256_bytes`

No function or method docstring is declared in the 0.7.5 source.

```python
def sha256_bytes(data: bytes) -> str
```

**Catalog symbol:** `x86decomp.contracts:sha256_bytes`  
**Visibility:** public  
**Source line:** 28

<a id="function-sha256-file"></a>

### `sha256_file`

No function or method docstring is declared in the 0.7.5 source.

```python
def sha256_file(path: str | Path, *, chunk_size: int=1024 * 1024) -> str
```

**Catalog symbol:** `x86decomp.contracts:sha256_file`  
**Visibility:** public  
**Source line:** 32

<a id="function-stable-id"></a>

### `stable_id`

No function or method docstring is declared in the 0.7.5 source.

```python
def stable_id(prefix: str, *parts: Any) -> str
```

**Catalog symbol:** `x86decomp.contracts:stable_id`  
**Visibility:** public  
**Source line:** 40

<a id="function-random-id"></a>

### `random_id`

No function or method docstring is declared in the 0.7.5 source.

```python
def random_id(prefix: str) -> str
```

**Catalog symbol:** `x86decomp.contracts:random_id`  
**Visibility:** public  
**Source line:** 45

<a id="function-validate-id"></a>

### `validate_id`

No function or method docstring is declared in the 0.7.5 source.

```python
def validate_id(value: str, *, field: str='id') -> str
```

**Catalog symbol:** `x86decomp.contracts:validate_id`  
**Visibility:** public  
**Source line:** 49

<a id="function-ensure-relative-path"></a>

### `ensure_relative_path`

No function or method docstring is declared in the 0.7.5 source.

```python
def ensure_relative_path(value: str | Path) -> Path
```

**Catalog symbol:** `x86decomp.contracts:ensure_relative_path`  
**Visibility:** public  
**Source line:** 55

<a id="function-atomic-write-bytes"></a>

### `atomic_write_bytes`

No function or method docstring is declared in the 0.7.5 source.

```python
def atomic_write_bytes(path: str | Path, data: bytes, *, mode: int=420) -> None
```

**Catalog symbol:** `x86decomp.contracts:atomic_write_bytes`  
**Visibility:** public  
**Source line:** 63

<a id="function-atomic-write-json"></a>

### `atomic_write_json`

No function or method docstring is declared in the 0.7.5 source.

```python
def atomic_write_json(path: str | Path, value: Any) -> None
```

**Catalog symbol:** `x86decomp.contracts:atomic_write_json`  
**Visibility:** public  
**Source line:** 82

<a id="function-read-json"></a>

### `read_json`

No function or method docstring is declared in the 0.7.5 source.

```python
def read_json(path: str | Path) -> Any
```

**Catalog symbol:** `x86decomp.contracts:read_json`  
**Visibility:** public  
**Source line:** 86

<a id="function-dedupe-preserve"></a>

### `dedupe_preserve`

No function or method docstring is declared in the 0.7.5 source.

```python
def dedupe_preserve(values: Iterable[str]) -> list[str]
```

**Catalog symbol:** `x86decomp.contracts:dedupe_preserve`  
**Visibility:** public  
**Source line:** 91
