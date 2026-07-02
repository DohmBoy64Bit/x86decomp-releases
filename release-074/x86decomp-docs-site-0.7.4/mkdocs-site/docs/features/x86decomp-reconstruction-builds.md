---
title: x86decomp.reconstruction.builds
description: No module docstring is declared in the v0.7.4 source.
original_path: features/x86decomp-reconstruction-builds.html
---

<a id="function-buildmanager-init"></a>
<a id="function-buildmanager-create"></a>
<a id="function-buildmanager-add-target"></a>
<a id="function-buildmanager-add-variant"></a>
<a id="function-buildmanager-show"></a>
<a id="function-buildmanager-show-target"></a>
<a id="function-buildmanager-show-variant"></a>
<a id="function-buildmanager-generate"></a>
<a id="function-buildmanager-validate"></a>
<a id="function-buildmanager-compare-modes"></a>
<a id="function-buildmanager-matrix"></a>

Section: Source-derived feature and function reference

# x86decomp.reconstruction.builds

No module docstring is declared in the v0.7.4 source.

Metadata: reconstruction · current · 11 functions/methods

**Source:** `src/x86decomp/reconstruction/builds.py`

> **Truth basis.** Module and symbol names, signatures, line numbers, docstrings, and SHA-256 are read directly from the sealed source. When source docstrings are absent, this page says so instead of inferring behavior. Source SHA-256: `b31ec8291d840a45ac78f86bc5ece98f8eca736f2c04eb02d1faba3754826254`.

## Functions and methods

Metadata: internal · line 11

### BuildManager.__init__

No function or method docstring is declared in the v0.7.4 source.

```
def __init__(self, store: ReconstructionStore)
```

**Catalog symbol:** `x86decomp.reconstruction.builds:BuildManager.__init__`

Metadata: public · line 12

### BuildManager.create

No function or method docstring is declared in the v0.7.4 source.

```
def create(self, name: str, *, mode: str, generator: str = 'cmake', output_root: str = 'build', metadata: dict[str, Any] | None = None, actor: str = 'analyst') -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.reconstruction.builds:BuildManager.create`

Metadata: public · line 20

### BuildManager.add_target

No function or method docstring is declared in the v0.7.4 source.

```
def add_target(self, build_id: str, name: str, *, kind: str = 'executable', output_name: str | None = None, sources: list[str] | None = None, dependencies: list[str] | None = None, actor: str = 'analyst') -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.reconstruction.builds:BuildManager.add_target`

Metadata: public · line 28

### BuildManager.add_variant

No function or method docstring is declared in the v0.7.4 source.

```
def add_variant(self, target_id: str, name: str, *, compiler: str, linker: str, compile_flags: list[str] | None = None, link_flags: list[str] | None = None, environment: dict[str, str] | None = None, actor: str = 'analyst') -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.reconstruction.builds:BuildManager.add_variant`

Metadata: public · line 35

### BuildManager.show

No function or method docstring is declared in the v0.7.4 source.

```
def show(self, build_id: str) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.reconstruction.builds:BuildManager.show`

Metadata: public · line 41

### BuildManager.show_target

No function or method docstring is declared in the v0.7.4 source.

```
def show_target(self, target_id: str) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.reconstruction.builds:BuildManager.show_target`

Metadata: public · line 47

### BuildManager.show_variant

No function or method docstring is declared in the v0.7.4 source.

```
def show_variant(self, variant_id: str) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.reconstruction.builds:BuildManager.show_variant`

Metadata: public · line 52

### BuildManager.generate

No function or method docstring is declared in the v0.7.4 source.

```
def generate(self, build_id: str, *, output_root: str | Path | None = None) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.reconstruction.builds:BuildManager.generate`

Metadata: public · line 71

### BuildManager.validate

No function or method docstring is declared in the v0.7.4 source.

```
def validate(self, target_id: str, variant_id: str | None = None, *, actor: str = 'validator') -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.reconstruction.builds:BuildManager.validate`

Metadata: public · line 81

### BuildManager.compare_modes

No function or method docstring is declared in the v0.7.4 source.

```
def compare_modes(self, historical_build_id: str, portable_build_id: str) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.reconstruction.builds:BuildManager.compare_modes`

Metadata: public · line 85

### BuildManager.matrix

No function or method docstring is declared in the v0.7.4 source.

```
def matrix(self) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.reconstruction.builds:BuildManager.matrix`
