---
title: x86decomp.reconstruction.project_layout
description: No module docstring is declared in the v0.7.4 source.
original_path: features/x86decomp-reconstruction-project-layout.html
---

<a id="function-projectlayout-init"></a>
<a id="function-projectlayout-create-module"></a>
<a id="function-projectlayout-add-member"></a>
<a id="function-projectlayout-create-translation-unit"></a>
<a id="function-projectlayout-add-translation-unit-member"></a>
<a id="function-projectlayout-synthesize"></a>
<a id="function-projectlayout-show-module"></a>
<a id="function-projectlayout-show-translation-unit"></a>
<a id="function-projectlayout-list-modules"></a>
<a id="function-projectlayout-explain-boundaries"></a>
<a id="function-projectlayout-export"></a>

Section: Source-derived feature and function reference

# x86decomp.reconstruction.project_layout

No module docstring is declared in the v0.7.4 source.

Metadata: reconstruction · current · 11 functions/methods

**Source:** `src/x86decomp/reconstruction/project_layout.py`

> **Truth basis.** Module and symbol names, signatures, line numbers, docstrings, and SHA-256 are read directly from the sealed source. When source docstrings are absent, this page says so instead of inferring behavior. Source SHA-256: `c56585dbc14339e024cf8fa5d4e4f31f06d7bce0a238b67212a3278a9282f4e7`.

## Functions and methods

Metadata: internal · line 11

### ProjectLayout.__init__

No function or method docstring is declared in the v0.7.4 source.

```
def __init__(self, store: ReconstructionStore)
```

**Catalog symbol:** `x86decomp.reconstruction.project_layout:ProjectLayout.__init__`

Metadata: public · line 13

### ProjectLayout.create_module

No function or method docstring is declared in the v0.7.4 source.

```
def create_module(self, name: str, *, kind: str = 'static-library', source_path: str | None = None, confidence: float = 1.0, evidence: list[dict[str, Any]] | None = None, actor: str = 'analyst') -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.reconstruction.project_layout:ProjectLayout.create_module`

Metadata: public · line 23

### ProjectLayout.add_member

No function or method docstring is declared in the v0.7.4 source.

```
def add_member(self, module_id: str, member_kind: str, member_id: str, *, ordinal: int = 0, evidence: list[dict[str, Any]] | None = None, actor: str = 'analyst') -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.reconstruction.project_layout:ProjectLayout.add_member`

Metadata: public · line 32

### ProjectLayout.create_translation_unit

No function or method docstring is declared in the v0.7.4 source.

```
def create_translation_unit(self, source_path: str, *, module_id: str | None = None, language: str = 'cpp', confidence: float = 1.0, evidence: list[dict[str, Any]] | None = None, actor: str = 'analyst') -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.reconstruction.project_layout:ProjectLayout.create_translation_unit`

Metadata: public · line 44

### ProjectLayout.add_translation_unit_member

No function or method docstring is declared in the v0.7.4 source.

```
def add_translation_unit_member(self, unit_id: str, member_kind: str, member_id: str, *, linkage: str = 'external', ordinal: int = 0, actor: str = 'analyst') -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.reconstruction.project_layout:ProjectLayout.add_translation_unit_member`

Metadata: public · line 53

### ProjectLayout.synthesize

Deterministically group inventory records by explicit object/library/source hints.

```
def synthesize(self, inventory: list[dict[str, Any]], *, actor: str = 'planner') -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.reconstruction.project_layout:ProjectLayout.synthesize`

Metadata: public · line 72

### ProjectLayout.show_module

No function or method docstring is declared in the v0.7.4 source.

```
def show_module(self, module_id: str) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.reconstruction.project_layout:ProjectLayout.show_module`

Metadata: public · line 80

### ProjectLayout.show_translation_unit

No function or method docstring is declared in the v0.7.4 source.

```
def show_translation_unit(self, unit_id: str) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.reconstruction.project_layout:ProjectLayout.show_translation_unit`

Metadata: public · line 88

### ProjectLayout.list_modules

No function or method docstring is declared in the v0.7.4 source.

```
def list_modules(self) -> list[dict[str, Any]]
```

**Catalog symbol:** `x86decomp.reconstruction.project_layout:ProjectLayout.list_modules`

Metadata: public · line 92

### ProjectLayout.explain_boundaries

No function or method docstring is declared in the v0.7.4 source.

```
def explain_boundaries(self, module_id: str) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.reconstruction.project_layout:ProjectLayout.explain_boundaries`

Metadata: public · line 96

### ProjectLayout.export

No function or method docstring is declared in the v0.7.4 source.

```
def export(self, path: str | Path) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.reconstruction.project_layout:ProjectLayout.export`
