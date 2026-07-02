---
title: x86decomp.artifacts
description: Function artifact import and validation.
original_path: features/x86decomp-artifacts.html
---

<a id="function-function-id-from-rva"></a>
<a id="function-validate-function-manifest"></a>
<a id="function-import-function-artifact"></a>
<a id="function-verify-function-artifact"></a>

Section: Source-derived feature and function reference

# x86decomp.artifacts

Function artifact import and validation.

Metadata: core · current · 4 functions/methods

**Source:** `src/x86decomp/artifacts.py`

> **Truth basis.** Module and symbol names, signatures, line numbers, docstrings, and SHA-256 are read directly from the sealed source. When source docstrings are absent, this page says so instead of inferring behavior. Source SHA-256: `171833c573e11e5d40d7791f8fea523536905a8486145a1aa1b96ea2761e6e6b`.

## Functions and methods

Metadata: public · line 16

### function_id_from_rva

No function or method docstring is declared in the v0.7.4 source.

```
def function_id_from_rva(rva: int) -> str
```

**Catalog symbol:** `x86decomp.artifacts:function_id_from_rva`

Metadata: public · line 22

### validate_function_manifest

No function or method docstring is declared in the v0.7.4 source.

```
def validate_function_manifest(value: Any) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.artifacts:validate_function_manifest`

Metadata: public · line 45

### import_function_artifact

No function or method docstring is declared in the v0.7.4 source.

```
def import_function_artifact(project_root: Path, exported_dir: Path) -> Path
```

**Catalog symbol:** `x86decomp.artifacts:import_function_artifact`

Metadata: public · line 75

### verify_function_artifact

No function or method docstring is declared in the v0.7.4 source.

```
def verify_function_artifact(artifact_dir: Path) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.artifacts:verify_function_artifact`
