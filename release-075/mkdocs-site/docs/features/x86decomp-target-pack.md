---
title: x86decomp.target_pack
description: Target-pack inference, validation, and project-template generation.
---

# `x86decomp.target_pack`

Target-pack inference, validation, and project-template generation.

A target pack records observed facts and user-supplied decisions separately.
Inferences never invent compiler versions, linker flags, names, or source layout.

**Area:** Toolkit  
**Source:** `src/x86decomp/target_pack.py`  
**SHA-256:** `18b4fa2ef39b61edd4c9ecc47d543ed6107395e841d81f9191d447dcaa5edb1d`  
**Functions/methods:** 8

> Module names, signatures, line numbers, and docstrings are extracted directly from the source AST. No behavior is inferred when a docstring is absent.

## Functions and methods

<a id="function-supportingartifact-to-dict"></a>

### `SupportingArtifact.to_dict`

No function or method docstring is declared in the 0.7.5 source.

```python
def SupportingArtifact.to_dict(self) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.target_pack:SupportingArtifact.to_dict`  
**Visibility:** public  
**Source line:** 36

<a id="function-toml-string"></a>

### `_toml_string`

No function or method docstring is declared in the 0.7.5 source.

```python
def _toml_string(value: str) -> str
```

**Catalog symbol:** `x86decomp.target_pack:_toml_string`  
**Visibility:** internal  
**Source line:** 40

<a id="function-write-target-toml"></a>

### `_write_target_toml`

No function or method docstring is declared in the 0.7.5 source.

```python
def _write_target_toml(path: Path, pack: dict[str, Any]) -> None
```

**Catalog symbol:** `x86decomp.target_pack:_write_target_toml`  
**Visibility:** internal  
**Source line:** 44

<a id="function-safe-artifact"></a>

### `_safe_artifact`

No function or method docstring is declared in the 0.7.5 source.

```python
def _safe_artifact(path: Path) -> Path
```

**Catalog symbol:** `x86decomp.target_pack:_safe_artifact`  
**Visibility:** internal  
**Source line:** 86

<a id="function-infer-target-pack"></a>

### `infer_target_pack`

No function or method docstring is declared in the 0.7.5 source.

```python
def infer_target_pack(primary_image: Path, output_directory: Path, *, name: str | None=None, pdb: Path | None=None, linker_map: Path | None=None, objects: Iterable[Path]=(), libraries: Iterable[Path]=(), rebuilt_image: Path | None=None, decisions: dict[str, Any] | None=None, copy_artifacts: bool=True) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.target_pack:infer_target_pack`  
**Visibility:** public  
**Source line:** 93

<a id="function-load-target-pack"></a>

### `load_target_pack`

No function or method docstring is declared in the 0.7.5 source.

```python
def load_target_pack(path: Path) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.target_pack:load_target_pack`  
**Visibility:** public  
**Source line:** 302

<a id="function-verify-target-pack"></a>

### `verify_target_pack`

No function or method docstring is declared in the 0.7.5 source.

```python
def verify_target_pack(path: Path) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.target_pack:verify_target_pack`  
**Visibility:** public  
**Source line:** 313

<a id="function-generate-project-from-target-pack"></a>

### `generate_project_from_target_pack`

No function or method docstring is declared in the 0.7.5 source.

```python
def generate_project_from_target_pack(target_pack: Path, project_root: Path, *, copy_binary: bool=True, overwrite_empty: bool=False) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.target_pack:generate_project_from_target_pack`  
**Visibility:** public  
**Source line:** 343
