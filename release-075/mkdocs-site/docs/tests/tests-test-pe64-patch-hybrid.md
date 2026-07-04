---
title: tests/test_pe64_patch_hybrid.py
description: Source-derived reference for 3 collected test nodes.
---

# `tests/test_pe64_patch_hybrid.py`

**Collected nodes:** 3  
**Source SHA-256:** `6894dd0e5abce06a30df7ce445f6cf7faa87bcc16dac9f314f187e938697a62f`

> Node identifiers, source lines, docstrings, and direct call names are extracted from pytest collection and the source AST. No behavior is inferred when a test has no docstring.

## `test_pe64_project`

No test docstring is declared.

**Direct call names in source:** `build_minimal_pe64`, `image.to_dict`, `initialize_project`, `parse_pe`, `verify_project`  
**Node ID:** `tests/test_pe64_patch_hybrid.py::test_pe64_project`  
**Area:** Toolkit behavior  
**Source line:** 12

## `test_patch_image`

No test docstring is declared.

**Direct call names in source:** `build_minimal_pe32`, `candidate.read_bytes`, `candidate.write_bytes`, `output.read_bytes`, `parse_pe`, `patch_pe_function`  
**Node ID:** `tests/test_pe64_patch_hybrid.py::test_patch_image`  
**Area:** Toolkit behavior  
**Source line:** 22

## `test_hybrid_project_builds_assembly_objects`

No test docstring is declared.

**Direct call names in source:** `(artifact / 'context.h').write_text`, `(artifact / 'decompiler.c').write_text`, `(artifact / 'function.json').write_text`, `(artifact / 'ranges' / '00.bin').write_bytes`, `(artifact / 'ranges').mkdir`, `(out / 'Makefile').is_file`, `(out / 'build' / 'sub_00001000.o').is_file`, `build_minimal_pe32`, `generate_hybrid_project`, `initialize_project`, `json.dumps`, `len`, `subprocess.run`  
**Node ID:** `tests/test_pe64_patch_hybrid.py::test_hybrid_project_builds_assembly_objects`  
**Area:** Toolkit behavior  
**Source line:** 33
