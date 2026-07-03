---
title: x86decomp.reconstruction.project_layout
description: No module docstring is declared in the 0.7.5 source.
---

# `x86decomp.reconstruction.project_layout`

No module docstring is declared in the 0.7.5 source.

**Area:** Toolkit  
**Source:** `src/x86decomp/reconstruction/project_layout.py`  
**SHA-256:** `c56585dbc14339e024cf8fa5d4e4f31f06d7bce0a238b67212a3278a9282f4e7`  
**Functions/methods:** 11

> Module names, signatures, line numbers, and docstrings are extracted directly from the source AST. No behavior is inferred when a docstring is absent.

## Functions and methods

<a id="function-projectlayout-init"></a>

### `ProjectLayout.__init__`

No function or method docstring is declared in the 0.7.5 source.

```python
def ProjectLayout.__init__(self, store: ReconstructionStore)
```

**Catalog symbol:** `x86decomp.reconstruction.project_layout:ProjectLayout.__init__`  
**Visibility:** internal  
**Source line:** 11

<a id="function-projectlayout-create-module"></a>

### `ProjectLayout.create_module`

No function or method docstring is declared in the 0.7.5 source.

```python
def ProjectLayout.create_module(self, name: str, *, kind: str='static-library', source_path: str | None=None, confidence: float=1.0, evidence: list[dict[str, Any]] | None=None, actor: str='analyst') -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.reconstruction.project_layout:ProjectLayout.create_module`  
**Visibility:** public  
**Source line:** 13

<a id="function-projectlayout-add-member"></a>

### `ProjectLayout.add_member`

No function or method docstring is declared in the 0.7.5 source.

```python
def ProjectLayout.add_member(self, module_id: str, member_kind: str, member_id: str, *, ordinal: int=0, evidence: list[dict[str, Any]] | None=None, actor: str='analyst') -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.reconstruction.project_layout:ProjectLayout.add_member`  
**Visibility:** public  
**Source line:** 23

<a id="function-projectlayout-create-translation-unit"></a>

### `ProjectLayout.create_translation_unit`

No function or method docstring is declared in the 0.7.5 source.

```python
def ProjectLayout.create_translation_unit(self, source_path: str, *, module_id: str | None=None, language: str='cpp', confidence: float=1.0, evidence: list[dict[str, Any]] | None=None, actor: str='analyst') -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.reconstruction.project_layout:ProjectLayout.create_translation_unit`  
**Visibility:** public  
**Source line:** 32

<a id="function-projectlayout-add-translation-unit-member"></a>

### `ProjectLayout.add_translation_unit_member`

No function or method docstring is declared in the 0.7.5 source.

```python
def ProjectLayout.add_translation_unit_member(self, unit_id: str, member_kind: str, member_id: str, *, linkage: str='external', ordinal: int=0, actor: str='analyst') -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.reconstruction.project_layout:ProjectLayout.add_translation_unit_member`  
**Visibility:** public  
**Source line:** 44

<a id="function-projectlayout-synthesize"></a>

### `ProjectLayout.synthesize`

Deterministically group inventory records by explicit object/library/source hints.

It never invents original filenames: absent hints go to an explicit unknown module.

```python
def ProjectLayout.synthesize(self, inventory: list[dict[str, Any]], *, actor: str='planner') -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.reconstruction.project_layout:ProjectLayout.synthesize`  
**Visibility:** public  
**Source line:** 53

<a id="function-projectlayout-show-module"></a>

### `ProjectLayout.show_module`

No function or method docstring is declared in the 0.7.5 source.

```python
def ProjectLayout.show_module(self, module_id: str) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.reconstruction.project_layout:ProjectLayout.show_module`  
**Visibility:** public  
**Source line:** 72

<a id="function-projectlayout-show-translation-unit"></a>

### `ProjectLayout.show_translation_unit`

No function or method docstring is declared in the 0.7.5 source.

```python
def ProjectLayout.show_translation_unit(self, unit_id: str) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.reconstruction.project_layout:ProjectLayout.show_translation_unit`  
**Visibility:** public  
**Source line:** 80

<a id="function-projectlayout-list-modules"></a>

### `ProjectLayout.list_modules`

No function or method docstring is declared in the 0.7.5 source.

```python
def ProjectLayout.list_modules(self) -> list[dict[str, Any]]
```

**Catalog symbol:** `x86decomp.reconstruction.project_layout:ProjectLayout.list_modules`  
**Visibility:** public  
**Source line:** 88

<a id="function-projectlayout-explain-boundaries"></a>

### `ProjectLayout.explain_boundaries`

No function or method docstring is declared in the 0.7.5 source.

```python
def ProjectLayout.explain_boundaries(self, module_id: str) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.reconstruction.project_layout:ProjectLayout.explain_boundaries`  
**Visibility:** public  
**Source line:** 92

<a id="function-projectlayout-export"></a>

### `ProjectLayout.export`

No function or method docstring is declared in the 0.7.5 source.

```python
def ProjectLayout.export(self, path: str | Path) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.reconstruction.project_layout:ProjectLayout.export`  
**Visibility:** public  
**Source line:** 96
