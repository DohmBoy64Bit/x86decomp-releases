---
title: x86decomp.target_pack
description: Target-pack inference, validation, and project-template generation.
original_path: features/x86decomp-target-pack.html
---

<a id="function-supportingartifact-to-dict"></a>
<a id="function-toml-string"></a>
<a id="function-write-target-toml"></a>
<a id="function-safe-artifact"></a>
<a id="function-infer-target-pack"></a>
<a id="function-load-target-pack"></a>
<a id="function-verify-target-pack"></a>
<a id="function-generate-project-from-target-pack"></a>

Section: Source-derived feature and function reference

# x86decomp.target_pack

Target-pack inference, validation, and project-template generation.

Metadata: core · current · 8 functions/methods

**Source:** `src/x86decomp/target_pack.py`

> **Truth basis.** Module and symbol names, signatures, line numbers, docstrings, and SHA-256 are read directly from the sealed source. When source docstrings are absent, this page says so instead of inferring behavior. Source SHA-256: `18b4fa2ef39b61edd4c9ecc47d543ed6107395e841d81f9191d447dcaa5edb1d`.

## Functions and methods

Metadata: public · line 36

### SupportingArtifact.to_dict

No function or method docstring is declared in the v0.7.4 source.

```
def to_dict(self) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.target_pack:SupportingArtifact.to_dict`

Metadata: internal · line 40

### _toml_string

No function or method docstring is declared in the v0.7.4 source.

```
def _toml_string(value: str) -> str
```

**Catalog symbol:** `x86decomp.target_pack:_toml_string`

Metadata: internal · line 44

### _write_target_toml

No function or method docstring is declared in the v0.7.4 source.

```
def _write_target_toml(path: Path, pack: dict[str, Any]) -> None
```

**Catalog symbol:** `x86decomp.target_pack:_write_target_toml`

Metadata: internal · line 86

### _safe_artifact

No function or method docstring is declared in the v0.7.4 source.

```
def _safe_artifact(path: Path) -> Path
```

**Catalog symbol:** `x86decomp.target_pack:_safe_artifact`

Metadata: public · line 93

### infer_target_pack

No function or method docstring is declared in the v0.7.4 source.

```
def infer_target_pack(primary_image: Path, output_directory: Path, *, name: str | None = None, pdb: Path | None = None, linker_map: Path | None = None, objects: Iterable[Path] = (), libraries: Iterable[Path] = (), rebuilt_image: Path | None = None, decisions: dict[str, Any] | None = None, copy_artifacts: bool = True) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.target_pack:infer_target_pack`

Metadata: public · line 302

### load_target_pack

No function or method docstring is declared in the v0.7.4 source.

```
def load_target_pack(path: Path) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.target_pack:load_target_pack`

Metadata: public · line 313

### verify_target_pack

No function or method docstring is declared in the v0.7.4 source.

```
def verify_target_pack(path: Path) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.target_pack:verify_target_pack`

Metadata: public · line 343

### generate_project_from_target_pack

No function or method docstring is declared in the v0.7.4 source.

```
def generate_project_from_target_pack(target_pack: Path, project_root: Path, *, copy_binary: bool = True, overwrite_empty: bool = False) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.target_pack:generate_project_from_target_pack`
