---
title: x86decomp.hybrid
description: Continuously buildable hybrid source-tree generation.
---

# `x86decomp.hybrid`

Continuously buildable hybrid source-tree generation.

**Area:** Toolkit  
**Source:** `src/x86decomp/hybrid.py`  
**SHA-256:** `721221b69c86bd2e7152ea2f322c9b48d89a01891feb6906038509a1f4592e2f`  
**Functions/methods:** 2

> Module names, signatures, line numbers, and docstrings are extracted directly from the source AST. No behavior is inferred when a docstring is absent.

## Functions and methods

<a id="function-assembly-bytes"></a>

### `_assembly_bytes`

No function or method docstring is declared in the 0.7.5 source.

```python
def _assembly_bytes(symbol: str, code: bytes, architecture: str) -> str
```

**Catalog symbol:** `x86decomp.hybrid:_assembly_bytes`  
**Visibility:** internal  
**Source line:** 15

<a id="function-generate-hybrid-project"></a>

### `generate_hybrid_project`

Generate a continuously buildable hybrid tree.

``bytes`` is the compatibility default and emits exact byte-form assembly.
``annotated`` retains those directives and appends ignored mnemonic comments.
``mnemonic`` uses the relocation-aware materializer and accepts source
only after exact resolved-byte verification, with per-instruction byte fallback.

```python
def generate_hybrid_project(project_root: Path, output_root: Path, *, architecture: str='x86', overwrite: bool=False, asm_format: str='bytes', image_base: int=0, assembler_command: list[str] | None=None, symbol_map: Mapping[str, Any] | list[Mapping[str, Any]] | None=None) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.hybrid:generate_hybrid_project`  
**Visibility:** public  
**Source line:** 24
