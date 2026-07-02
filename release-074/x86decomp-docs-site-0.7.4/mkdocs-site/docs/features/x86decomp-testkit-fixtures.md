---
title: x86decomp_testkit.fixtures
description: No module docstring is declared in the v0.7.4 source.
original_path: features/x86decomp-testkit-fixtures.html
---

<a id="function-write-json"></a>
<a id="function-build-minimal-pe32"></a>
<a id="function-build-minimal-pe64"></a>
<a id="function-create-common-fixtures"></a>

Section: Source-derived feature and function reference

# x86decomp_testkit.fixtures

No module docstring is declared in the v0.7.4 source.

Metadata: verification harness · current · 4 functions/methods

**Source:** `test-suite/src/x86decomp_testkit/fixtures.py`

> **Truth basis.** Module and symbol names, signatures, line numbers, docstrings, and SHA-256 are read directly from the sealed source. When source docstrings are absent, this page says so instead of inferring behavior. Source SHA-256: `503faabe75a6906a9feda50866fc275f80a0596d8605b6b9125c36330a7ef6ed`.

## Functions and methods

Metadata: public · line 9

### write_json

No function or method docstring is declared in the v0.7.4 source.

```
def write_json(path: Path, value: Any) -> Path
```

**Catalog symbol:** `x86decomp_testkit.fixtures:write_json`

Metadata: public · line 15

### build_minimal_pe32

No function or method docstring is declared in the v0.7.4 source.

```
def build_minimal_pe32(path: Path, code: bytes = b'U\x8b\xec1\xc0]\xc3') -> Path
```

**Catalog symbol:** `x86decomp_testkit.fixtures:build_minimal_pe32`

Metadata: public · line 48

### build_minimal_pe64

No function or method docstring is declared in the v0.7.4 source.

```
def build_minimal_pe64(path: Path, code: bytes = b'1\xc0\xc3') -> Path
```

**Catalog symbol:** `x86decomp_testkit.fixtures:build_minimal_pe64`

Metadata: public · line 82

### create_common_fixtures

No function or method docstring is declared in the v0.7.4 source.

```
def create_common_fixtures(root: Path) -> dict[str, Path]
```

**Catalog symbol:** `x86decomp_testkit.fixtures:create_common_fixtures`
