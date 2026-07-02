---
title: x86decomp.native.staging
description: No module docstring is declared in the v0.7.4 source.
original_path: features/x86decomp-native-staging.html
---

<a id="function-stagingbridge-init"></a>
<a id="function-stagingbridge-scan"></a>
<a id="function-stagingbridge-generate-context"></a>
<a id="function-stagingbridge-resolve"></a>
<a id="function-stagingbridge-unresolved"></a>
<a id="function-stagingbridge-compile-check"></a>

Section: Source-derived feature and function reference

# x86decomp.native.staging

No module docstring is declared in the v0.7.4 source.

Metadata: native · current · 6 functions/methods

**Source:** `src/x86decomp/native/staging.py`

> **Truth basis.** Module and symbol names, signatures, line numbers, docstrings, and SHA-256 are read directly from the sealed source. When source docstrings are absent, this page says so instead of inferring behavior. Source SHA-256: `0038cab527aaac36dc4ba8ea02eb526b2683f5329a03c4002673091f622239a1`.

## Functions and methods

Metadata: internal · line 26

### StagingBridge.__init__

No function or method docstring is declared in the v0.7.4 source.

```
def __init__(self, store: NativeStore)
```

**Catalog symbol:** `x86decomp.native.staging:StagingBridge.__init__`

Metadata: public · line 28

### StagingBridge.scan

No function or method docstring is declared in the v0.7.4 source.

```
def scan(self, source_paths: Iterable[Path]) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.native.staging:StagingBridge.scan`

Metadata: public · line 40

### StagingBridge.generate_context

No function or method docstring is declared in the v0.7.4 source.

```
def generate_context(self, source_paths: Iterable[Path], output: Path, *, actor: str = 'analyst') -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.native.staging:StagingBridge.generate_context`

Metadata: public · line 59

### StagingBridge.resolve

No function or method docstring is declared in the v0.7.4 source.

```
def resolve(self, mapping: dict[str, str], *, actor: str = 'analyst') -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.native.staging:StagingBridge.resolve`

Metadata: public · line 70

### StagingBridge.unresolved

No function or method docstring is declared in the v0.7.4 source.

```
def unresolved(self) -> list[dict[str, Any]]
```

**Catalog symbol:** `x86decomp.native.staging:StagingBridge.unresolved`

Metadata: public · line 73

### StagingBridge.compile_check

No function or method docstring is declared in the v0.7.4 source.

```
def compile_check(self, command: list[str], *, cwd: Path | None = None, timeout_seconds: int = 120) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.native.staging:StagingBridge.compile_check`
