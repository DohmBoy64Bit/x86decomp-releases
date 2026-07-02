---
title: x86decomp.hybrid
description: Continuously buildable hybrid source-tree generation.
original_path: features/x86decomp-hybrid.html
---

<a id="function-assembly-bytes"></a>
<a id="function-generate-hybrid-project"></a>

Section: Source-derived feature and function reference

# x86decomp.hybrid

Continuously buildable hybrid source-tree generation.

Metadata: core · current · 2 functions/methods

**Source:** `src/x86decomp/hybrid.py`

> **Truth basis.** Module and symbol names, signatures, line numbers, docstrings, and SHA-256 are read directly from the sealed source. When source docstrings are absent, this page says so instead of inferring behavior. Source SHA-256: `721221b69c86bd2e7152ea2f322c9b48d89a01891feb6906038509a1f4592e2f`.

## Functions and methods

Metadata: internal · line 15

### _assembly_bytes

No function or method docstring is declared in the v0.7.4 source.

```
def _assembly_bytes(symbol: str, code: bytes, architecture: str) -> str
```

**Catalog symbol:** `x86decomp.hybrid:_assembly_bytes`

Metadata: public · line 24

### generate_hybrid_project

Generate a continuously buildable hybrid tree.

```
def generate_hybrid_project(project_root: Path, output_root: Path, *, architecture: str = 'x86', overwrite: bool = False, asm_format: str = 'bytes', image_base: int = 0, assembler_command: list[str] | None = None, symbol_map: Mapping[str, Any] | list[Mapping[str, Any]] | None = None) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.hybrid:generate_hybrid_project`
