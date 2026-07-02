---
title: x86decomp.reproducibility
description: Reproducibility manifests and verification.
original_path: features/x86decomp-reproducibility.html
---

<a id="function-version"></a>
<a id="function-build-reproduction-manifest"></a>
<a id="function-verify-reproduction-manifest"></a>

Section: Source-derived feature and function reference

# x86decomp.reproducibility

Reproducibility manifests and verification.

Metadata: core · current · 3 functions/methods

**Source:** `src/x86decomp/reproducibility.py`

> **Truth basis.** Module and symbol names, signatures, line numbers, docstrings, and SHA-256 are read directly from the sealed source. When source docstrings are absent, this page says so instead of inferring behavior. Source SHA-256: `bcc5e2a773d7eb7589f28df90c0fe898155788b8e695d15e363e6dbad249ae7b`.

## Functions and methods

Metadata: internal · line 26

### _version

No function or method docstring is declared in the v0.7.4 source.

```
def _version(executable: str) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.reproducibility:_version`

Metadata: public · line 52

### build_reproduction_manifest

No function or method docstring is declared in the v0.7.4 source.

```
def build_reproduction_manifest(project_root: Path, *, output: Path | None = None, required_tools: list[str] | None = None) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.reproducibility:build_reproduction_manifest`

Metadata: public · line 120

### verify_reproduction_manifest

No function or method docstring is declared in the v0.7.4 source.

```
def verify_reproduction_manifest(project_root: Path, manifest_path: Path) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.reproducibility:verify_reproduction_manifest`
