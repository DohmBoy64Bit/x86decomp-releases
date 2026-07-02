---
title: x86decomp.reconstruction.headers
description: No module docstring is declared in the v0.7.4 source.
original_path: features/x86decomp-reconstruction-headers.html
---

<a id="function-headermanager-init"></a>
<a id="function-headermanager-create"></a>
<a id="function-headermanager-declare"></a>
<a id="function-headermanager-include"></a>
<a id="function-headermanager-cycles"></a>
<a id="function-headermanager-show"></a>
<a id="function-headermanager-synthesize"></a>
<a id="function-headermanager-validate"></a>

Section: Source-derived feature and function reference

# x86decomp.reconstruction.headers

No module docstring is declared in the v0.7.4 source.

Metadata: reconstruction · current · 8 functions/methods

**Source:** `src/x86decomp/reconstruction/headers.py`

> **Truth basis.** Module and symbol names, signatures, line numbers, docstrings, and SHA-256 are read directly from the sealed source. When source docstrings are absent, this page says so instead of inferring behavior. Source SHA-256: `438c0233df3581b7634dd878b01f5b32f6918d7dac836115ad7bc1c0c50fdacc`.

## Functions and methods

Metadata: internal · line 10

### HeaderManager.__init__

No function or method docstring is declared in the v0.7.4 source.

```
def __init__(self, store: ReconstructionStore)
```

**Catalog symbol:** `x86decomp.reconstruction.headers:HeaderManager.__init__`

Metadata: public · line 11

### HeaderManager.create

No function or method docstring is declared in the v0.7.4 source.

```
def create(self, path: str, *, visibility: str = 'private', actor: str = 'analyst') -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.reconstruction.headers:HeaderManager.create`

Metadata: public · line 20

### HeaderManager.declare

No function or method docstring is declared in the v0.7.4 source.

```
def declare(self, header_id: str, symbol_id: str, declaration: str, *, kind: str = 'function', confidence: float = 1.0, evidence: list[dict[str, Any]] | None = None, actor: str = 'analyst') -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.reconstruction.headers:HeaderManager.declare`

Metadata: public · line 30

### HeaderManager.include

No function or method docstring is declared in the v0.7.4 source.

```
def include(self, source_header_id: str, target_header_id: str, *, reason: str, actor: str = 'analyst') -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.reconstruction.headers:HeaderManager.include`

Metadata: public · line 37

### HeaderManager.cycles

No function or method docstring is declared in the v0.7.4 source.

```
def cycles(self, *, connection = None) -> list[list[str]]
```

**Catalog symbol:** `x86decomp.reconstruction.headers:HeaderManager.cycles`

Metadata: public · line 55

### HeaderManager.show

No function or method docstring is declared in the v0.7.4 source.

```
def show(self, header_id: str) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.reconstruction.headers:HeaderManager.show`

Metadata: public · line 62

### HeaderManager.synthesize

No function or method docstring is declared in the v0.7.4 source.

```
def synthesize(self, header_id: str, *, output_root: str | Path | None = None) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.reconstruction.headers:HeaderManager.synthesize`

Metadata: public · line 73

### HeaderManager.validate

No function or method docstring is declared in the v0.7.4 source.

```
def validate(self, header_id: str) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.reconstruction.headers:HeaderManager.validate`
