---
title: tests/test_memory.py
description: Source-derived reference for 2 collected test nodes.
---

# `tests/test_memory.py`

**Collected nodes:** 2  
**Source SHA-256:** `dd3384d0fa0c87ed61bde90498b97a3dc2d642d24b57fc9e00f95e52f47ca0b1`

> Node identifiers, source lines, docstrings, and direct call names are extracted from pytest collection and the source AST. No behavior is inferred when a test has no docstring.

## `test_hash_chain`

No test docstring is declared.

**Direct call names in source:** `Path`, `ProjectMemory`, `memory.append`, `memory.rendered_path.is_file`, `memory.verify`, `self.assertTrue`, `tempfile.TemporaryDirectory`  
**Node ID:** `tests/test_memory.py::MemoryTests::test_hash_chain`  
**Area:** Toolkit behavior  
**Source line:** 12

## `test_tamper_detection`

No test docstring is declared.

**Direct call names in source:** `Path`, `ProjectMemory`, `json.dumps`, `json.loads`, `memory.append`, `memory.events_path.read_text`, `memory.events_path.read_text(encoding='utf-8').splitlines`, `memory.events_path.write_text`, `memory.verify`, `self.assertFalse`, `tempfile.TemporaryDirectory`  
**Node ID:** `tests/test_memory.py::MemoryTests::test_tamper_detection`  
**Area:** Toolkit behavior  
**Source line:** 21
