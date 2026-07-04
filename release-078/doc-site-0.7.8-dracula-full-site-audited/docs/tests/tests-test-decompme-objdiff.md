---
title: tests/test_decompme_objdiff.py
description: Source-derived reference for 2 collected test nodes.
---

# `tests/test_decompme_objdiff.py`

**Collected nodes:** 2  
**Source SHA-256:** `5b9c426c8062799b1dd013a426638767e12d93e03e9425e6f21987abecfdcb60`

> Node identifiers, source lines, docstrings, and direct call names are extracted from pytest collection and the source AST. No behavior is inferred when a test has no docstring.

## `test_create_local_decompme_packet`

No test docstring is declared.

**Direct call names in source:** `(artifact / 'function.json').write_text`, `(artifact / 'listing.asm').read_text`, `(artifact / name).write_text`, `(output / 'packet.json').is_file`, `(output / 'target_asm_ghidra.txt').read_text`, `artifact.mkdir`, `create_decompme_packet`, `json.dumps`, `{'listing.asm': 'xor eax,eax\nret\n', 'decompiler.c': 'int f(void) { return 0; }\n', 'context.h': 'typedef unsigned int uint;\n', 'references.jsonl': ''}.items`  
**Node ID:** `tests/test_decompme_objdiff.py::test_create_local_decompme_packet`  
**Area:** Toolkit behavior  
**Source line:** 11

## `test_manifest_driven_objdiff_adapter`

No test docstring is declared.

**Direct call names in source:** `candidate.write_bytes`, `json.dumps`, `manifest.write_text`, `run_objdiff_manifest`, `script.write_text`, `str`, `target.write_bytes`  
**Node ID:** `tests/test_decompme_objdiff.py::test_manifest_driven_objdiff_adapter`  
**Area:** Toolkit behavior  
**Source line:** 40
