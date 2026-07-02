---
title: x86decomp.memory
description: Append-only, hash-chained project memory.
original_path: features/x86decomp-memory.html
---

<a id="function-projectmemory-init"></a>
<a id="function-projectmemory-read-events"></a>
<a id="function-projectmemory-append"></a>
<a id="function-projectmemory-verify"></a>
<a id="function-projectmemory-require-valid"></a>
<a id="function-projectmemory-render"></a>

Section: Source-derived feature and function reference

# x86decomp.memory

Append-only, hash-chained project memory.

Metadata: core · current · 6 functions/methods

**Source:** `src/x86decomp/memory.py`

> **Truth basis.** Module and symbol names, signatures, line numbers, docstrings, and SHA-256 are read directly from the sealed source. When source docstrings are absent, this page says so instead of inferring behavior. Source SHA-256: `4fd6948418a67ffdd502b92649a5b18af16376b55272018305b59d5cddcad813`.

## Functions and methods

Metadata: internal · line 15

### ProjectMemory.__init__

No function or method docstring is declared in the v0.7.4 source.

```
def __init__(self, project_root: Path)
```

**Catalog symbol:** `x86decomp.memory:ProjectMemory.__init__`

Metadata: public · line 24

### ProjectMemory.read_events

No function or method docstring is declared in the v0.7.4 source.

```
def read_events(self) -> list[dict[str, Any]]
```

**Catalog symbol:** `x86decomp.memory:ProjectMemory.read_events`

Metadata: public · line 41

### ProjectMemory.append

No function or method docstring is declared in the v0.7.4 source.

```
def append(self, *, actor: str, category: str, summary: str, details: dict[str, Any] | None = None, evidence_ids: Iterable[str] = ()) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.memory:ProjectMemory.append`

Metadata: public · line 73

### ProjectMemory.verify

No function or method docstring is declared in the v0.7.4 source.

```
def verify(self) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.memory:ProjectMemory.verify`

Metadata: public · line 91

### ProjectMemory.require_valid

No function or method docstring is declared in the v0.7.4 source.

```
def require_valid(self) -> None
```

**Catalog symbol:** `x86decomp.memory:ProjectMemory.require_valid`

Metadata: public · line 96

### ProjectMemory.render

No function or method docstring is declared in the v0.7.4 source.

```
def render(self) -> str
```

**Catalog symbol:** `x86decomp.memory:ProjectMemory.render`
