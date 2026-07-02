---
title: x86decomp.linker_reconstruction
description: Evidence-driven linker reconstruction plans.
original_path: features/x86decomp-linker-reconstruction.html
---

<a id="function-build-linker-reconstruction-plan"></a>
<a id="function-write-relink-manifest-from-plan"></a>

Section: Source-derived feature and function reference

# x86decomp.linker_reconstruction

Evidence-driven linker reconstruction plans.

Metadata: core · current · 2 functions/methods

**Source:** `src/x86decomp/linker_reconstruction.py`

> **Truth basis.** Module and symbol names, signatures, line numbers, docstrings, and SHA-256 are read directly from the sealed source. When source docstrings are absent, this page says so instead of inferring behavior. Source SHA-256: `f67bc3077e7d54a9a32e542113cc28eadf00fa581c8e3d3c26e5c1b45a4e0900`.

## Functions and methods

Metadata: public · line 21

### build_linker_reconstruction_plan

No function or method docstring is declared in the v0.7.4 source.

```
def build_linker_reconstruction_plan(pe_path: Path, map_path: Path, *, object_paths: Iterable[Path], library_paths: Iterable[Path] = (), linker: str = 'lld-link', output_path: str = 'build/reconstructed.exe', report_path: Path | None = None) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.linker_reconstruction:build_linker_reconstruction_plan`

Metadata: public · line 145

### write_relink_manifest_from_plan

No function or method docstring is declared in the v0.7.4 source.

```
def write_relink_manifest_from_plan(plan: dict[str, Any], output: Path) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.linker_reconstruction:write_relink_manifest_from_plan`
