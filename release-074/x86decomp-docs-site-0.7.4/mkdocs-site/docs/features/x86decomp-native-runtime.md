---
title: x86decomp.native.runtime
description: No module docstring is declared in the v0.7.4 source.
original_path: features/x86decomp-native-runtime.html
---

<a id="function-runtimevalidation-init"></a>
<a id="function-runtimevalidation-validate-image"></a>
<a id="function-runtimevalidation-launch"></a>
<a id="function-runtimevalidation-map-crash"></a>
<a id="function-runtimevalidation-record"></a>

Section: Source-derived feature and function reference

# x86decomp.native.runtime

No module docstring is declared in the v0.7.4 source.

Metadata: native · current · 5 functions/methods

**Source:** `src/x86decomp/native/runtime.py`

> **Truth basis.** Module and symbol names, signatures, line numbers, docstrings, and SHA-256 are read directly from the sealed source. When source docstrings are absent, this page says so instead of inferring behavior. Source SHA-256: `42a582f61d69ef1bc07096d003f19db4c0598d7386be494c124cf4272b1aa854`.

## Functions and methods

Metadata: internal · line 15

### RuntimeValidation.__init__

No function or method docstring is declared in the v0.7.4 source.

```
def __init__(self, store: NativeStore)
```

**Catalog symbol:** `x86decomp.native.runtime:RuntimeValidation.__init__`

Metadata: public · line 17

### RuntimeValidation.validate_image

No function or method docstring is declared in the v0.7.4 source.

```
def validate_image(self, image_path: Path, *, actor: str = 'analyst') -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.native.runtime:RuntimeValidation.validate_image`

Metadata: public · line 29

### RuntimeValidation.launch

No function or method docstring is declared in the v0.7.4 source.

```
def launch(self, image_path: Path, *, execute: bool = False, timeout_seconds: int = 10, arguments: list[str] | None = None, actor: str = 'analyst') -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.native.runtime:RuntimeValidation.launch`

Metadata: public · line 44

### RuntimeValidation.map_crash

No function or method docstring is declared in the v0.7.4 source.

```
def map_crash(self, rva: int) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.native.runtime:RuntimeValidation.map_crash`

Metadata: internal · line 50

### RuntimeValidation._record

No function or method docstring is declared in the v0.7.4 source.

```
def _record(self, path: Path, kind: str, checks: dict[str, Any], details: dict[str, Any], authorized: bool, actor: str) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.native.runtime:RuntimeValidation._record`
