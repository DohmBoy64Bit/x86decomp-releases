---
title: x86decomp.contracts
description: No module docstring is declared in the v0.7.4 source.
original_path: features/x86decomp-contracts.html
---

<a id="function-utc-now"></a>
<a id="function-canonical-json"></a>
<a id="function-sha256-bytes"></a>
<a id="function-sha256-file"></a>
<a id="function-stable-id"></a>
<a id="function-random-id"></a>
<a id="function-validate-id"></a>
<a id="function-ensure-relative-path"></a>
<a id="function-atomic-write-bytes"></a>
<a id="function-atomic-write-json"></a>
<a id="function-read-json"></a>
<a id="function-dedupe-preserve"></a>

Section: Source-derived feature and function reference

# x86decomp.contracts

No module docstring is declared in the v0.7.4 source.

Metadata: core · current · 12 functions/methods

**Source:** `src/x86decomp/contracts.py`

> **Truth basis.** Module and symbol names, signatures, line numbers, docstrings, and SHA-256 are read directly from the sealed source. When source docstrings are absent, this page says so instead of inferring behavior. Source SHA-256: `59ed708757edb48209337ba38008c4522cd03106686c9b47b08da0b2a32e98ed`.

## Functions and methods

Metadata: public · line 20

### utc_now

No function or method docstring is declared in the v0.7.4 source.

```
def utc_now() -> str
```

**Catalog symbol:** `x86decomp.contracts:utc_now`

Metadata: public · line 24

### canonical_json

No function or method docstring is declared in the v0.7.4 source.

```
def canonical_json(value: Any) -> str
```

**Catalog symbol:** `x86decomp.contracts:canonical_json`

Metadata: public · line 28

### sha256_bytes

No function or method docstring is declared in the v0.7.4 source.

```
def sha256_bytes(data: bytes) -> str
```

**Catalog symbol:** `x86decomp.contracts:sha256_bytes`

Metadata: public · line 32

### sha256_file

No function or method docstring is declared in the v0.7.4 source.

```
def sha256_file(path: str | Path, *, chunk_size: int = 1024 * 1024) -> str
```

**Catalog symbol:** `x86decomp.contracts:sha256_file`

Metadata: public · line 40

### stable_id

No function or method docstring is declared in the v0.7.4 source.

```
def stable_id(prefix: str, *parts: Any) -> str
```

**Catalog symbol:** `x86decomp.contracts:stable_id`

Metadata: public · line 45

### random_id

No function or method docstring is declared in the v0.7.4 source.

```
def random_id(prefix: str) -> str
```

**Catalog symbol:** `x86decomp.contracts:random_id`

Metadata: public · line 49

### validate_id

No function or method docstring is declared in the v0.7.4 source.

```
def validate_id(value: str, *, field: str = 'id') -> str
```

**Catalog symbol:** `x86decomp.contracts:validate_id`

Metadata: public · line 55

### ensure_relative_path

No function or method docstring is declared in the v0.7.4 source.

```
def ensure_relative_path(value: str | Path) -> Path
```

**Catalog symbol:** `x86decomp.contracts:ensure_relative_path`

Metadata: public · line 63

### atomic_write_bytes

No function or method docstring is declared in the v0.7.4 source.

```
def atomic_write_bytes(path: str | Path, data: bytes, *, mode: int = 420) -> None
```

**Catalog symbol:** `x86decomp.contracts:atomic_write_bytes`

Metadata: public · line 82

### atomic_write_json

No function or method docstring is declared in the v0.7.4 source.

```
def atomic_write_json(path: str | Path, value: Any) -> None
```

**Catalog symbol:** `x86decomp.contracts:atomic_write_json`

Metadata: public · line 86

### read_json

No function or method docstring is declared in the v0.7.4 source.

```
def read_json(path: str | Path) -> Any
```

**Catalog symbol:** `x86decomp.contracts:read_json`

Metadata: public · line 91

### dedupe_preserve

No function or method docstring is declared in the v0.7.4 source.

```
def dedupe_preserve(values: Iterable[str]) -> list[str]
```

**Catalog symbol:** `x86decomp.contracts:dedupe_preserve`
