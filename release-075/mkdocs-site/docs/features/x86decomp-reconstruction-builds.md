---
title: x86decomp.reconstruction.builds
description: No module docstring is declared in the 0.7.5 source.
---

# `x86decomp.reconstruction.builds`

No module docstring is declared in the 0.7.5 source.

**Area:** Toolkit  
**Source:** `src/x86decomp/reconstruction/builds.py`  
**SHA-256:** `a336a177a2549a570f55c1efbd7d58d87ba8f5a077e1271e2f969a1e8c6ff040`  
**Functions/methods:** 11

> Module names, signatures, line numbers, and docstrings are extracted directly from the source AST. No behavior is inferred when a docstring is absent.

## Functions and methods

<a id="function-buildmanager-init"></a>

### `BuildManager.__init__`

No function or method docstring is declared in the 0.7.5 source.

```python
def BuildManager.__init__(self, store: ReconstructionStore)
```

**Catalog symbol:** `x86decomp.reconstruction.builds:BuildManager.__init__`  
**Visibility:** internal  
**Source line:** 11

<a id="function-buildmanager-create"></a>

### `BuildManager.create`

No function or method docstring is declared in the 0.7.5 source.

```python
def BuildManager.create(self, name: str, *, mode: str, generator: str='cmake', output_root: str='build', metadata: dict[str, Any] | None=None, actor: str='analyst') -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.reconstruction.builds:BuildManager.create`  
**Visibility:** public  
**Source line:** 12

<a id="function-buildmanager-add-target"></a>

### `BuildManager.add_target`

No function or method docstring is declared in the 0.7.5 source.

```python
def BuildManager.add_target(self, build_id: str, name: str, *, kind: str='executable', output_name: str | None=None, sources: list[str] | None=None, dependencies: list[str] | None=None, actor: str='analyst') -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.reconstruction.builds:BuildManager.add_target`  
**Visibility:** public  
**Source line:** 20

<a id="function-buildmanager-add-variant"></a>

### `BuildManager.add_variant`

No function or method docstring is declared in the 0.7.5 source.

```python
def BuildManager.add_variant(self, target_id: str, name: str, *, compiler: str, linker: str, compile_flags: list[str] | None=None, link_flags: list[str] | None=None, environment: dict[str, str] | None=None, actor: str='analyst') -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.reconstruction.builds:BuildManager.add_variant`  
**Visibility:** public  
**Source line:** 28

<a id="function-buildmanager-show"></a>

### `BuildManager.show`

No function or method docstring is declared in the 0.7.5 source.

```python
def BuildManager.show(self, build_id: str) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.reconstruction.builds:BuildManager.show`  
**Visibility:** public  
**Source line:** 35

<a id="function-buildmanager-show-target"></a>

### `BuildManager.show_target`

No function or method docstring is declared in the 0.7.5 source.

```python
def BuildManager.show_target(self, target_id: str) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.reconstruction.builds:BuildManager.show_target`  
**Visibility:** public  
**Source line:** 41

<a id="function-buildmanager-show-variant"></a>

### `BuildManager.show_variant`

No function or method docstring is declared in the 0.7.5 source.

```python
def BuildManager.show_variant(self, variant_id: str) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.reconstruction.builds:BuildManager.show_variant`  
**Visibility:** public  
**Source line:** 47

<a id="function-buildmanager-generate"></a>

### `BuildManager.generate`

No function or method docstring is declared in the 0.7.5 source.

```python
def BuildManager.generate(self, build_id: str, *, output_root: str | Path | None=None) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.reconstruction.builds:BuildManager.generate`  
**Visibility:** public  
**Source line:** 52

<a id="function-buildmanager-validate"></a>

### `BuildManager.validate`

No function or method docstring is declared in the 0.7.5 source.

```python
def BuildManager.validate(self, target_id: str, variant_id: str | None=None, *, actor: str='validator') -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.reconstruction.builds:BuildManager.validate`  
**Visibility:** public  
**Source line:** 71

<a id="function-buildmanager-compare-modes"></a>

### `BuildManager.compare_modes`

No function or method docstring is declared in the 0.7.5 source.

```python
def BuildManager.compare_modes(self, historical_build_id: str, portable_build_id: str) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.reconstruction.builds:BuildManager.compare_modes`  
**Visibility:** public  
**Source line:** 81

<a id="function-buildmanager-matrix"></a>

### `BuildManager.matrix`

No function or method docstring is declared in the 0.7.5 source.

```python
def BuildManager.matrix(self) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.reconstruction.builds:BuildManager.matrix`  
**Visibility:** public  
**Source line:** 85
