---
title: x86decomp.assembly.annotation
description: Module reference for x86decomp.assembly.annotation.
---

# `x86decomp.assembly.annotation`

- Area: `toolkit`
- Source path: `src/x86decomp/assembly/annotation.py`
- SHA-256: `b124d036b79e6ffa168f1e500717af68c615534f8bb789892f2818c5787bb1cd`
- Size: `4642` bytes
- Lines: `126`

## Module docstring

Provide the current runtime implementation for the `x86decomp.assembly.annotation` module.

## Symbols

| Kind | Name | Line | Docstring summary |
| --- | --- | --- | --- |
| function | `validate_symbol` | 15 | Validate symbol for the current toolkit workflow. |
| function | `render_byte_assembly` | 22 | Render the original compatibility form. This output intentionally preserves byte-form assembly semantics. |
| function | `parse_byte_directives` | 40 | Parse byte directives for the current toolkit workflow. |
| function | `_chunk_comments` | 63 | Support chunk comments processing for internal toolkit callers. |
| function | `render_annotated_assembly` | 74 | Render byte-identical directives with idempotent Capstone comments. |
| function | `annotate_source` | 96 | Execute the annotate source operation for the current toolkit workflow. |
| function | `byte_directive_lines` | 121 | Execute the byte directive lines operation for the current toolkit workflow. |
