---
title: x86decomp.linker_reconstruction
description: Evidence-driven linker reconstruction plans.
---

# `x86decomp.linker_reconstruction`

Evidence-driven linker reconstruction plans.

Plans are generated only from supplied PE/MAP/COFF/archive evidence.  Unknown
placement, runtime library, linker flag, and import decisions remain explicit
unresolved items rather than inferred facts.

**Area:** Toolkit  
**Source:** `src/x86decomp/linker_reconstruction.py`  
**SHA-256:** `f67bc3077e7d54a9a32e542113cc28eadf00fa581c8e3d3c26e5c1b45a4e0900`  
**Functions/methods:** 2

> Module names, signatures, line numbers, and docstrings are extracted directly from the source AST. No behavior is inferred when a docstring is absent.

## Functions and methods

<a id="function-build-linker-reconstruction-plan"></a>

### `build_linker_reconstruction_plan`

No function or method docstring is declared in the 0.7.5 source.

```python
def build_linker_reconstruction_plan(pe_path: Path, map_path: Path, *, object_paths: Iterable[Path], library_paths: Iterable[Path]=(), linker: str='lld-link', output_path: str='build/reconstructed.exe', report_path: Path | None=None) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.linker_reconstruction:build_linker_reconstruction_plan`  
**Visibility:** public  
**Source line:** 21

<a id="function-write-relink-manifest-from-plan"></a>

### `write_relink_manifest_from_plan`

No function or method docstring is declared in the 0.7.5 source.

```python
def write_relink_manifest_from_plan(plan: dict[str, Any], output: Path) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.linker_reconstruction:write_relink_manifest_from_plan`  
**Visibility:** public  
**Source line:** 145
