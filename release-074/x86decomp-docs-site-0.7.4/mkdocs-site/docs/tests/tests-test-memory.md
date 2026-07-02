---
title: tests/test_memory.py
description: 2 exact current test nodes
original_path: tests/tests-test-memory.html
---

<a id="test-memorytests-test-hash-chain"></a>
<a id="test-memorytests-test-tamper-detection"></a>

Section: Source-derived test reference

# `tests/test_memory.py`

2 current test nodes in the Toolkit behavior inventory.

> **Truth basis.** Node IDs, line numbers, docstrings, and direct call names are extracted from the AST. No behavior is inferred when a test lacks a docstring. Source SHA-256: `dd3384d0fa0c87ed61bde90498b97a3dc2d642d24b57fc9e00f95e52f47ca0b1`.

Metadata: Toolkit behavior · line 12

### `MemoryTests::test_hash_chain`

No test docstring is declared. The node identifier and direct call names are shown without inferring additional behavior.

**Direct call names in source:** `tempfile.TemporaryDirectory`, `ProjectMemory`, `memory.append`, `memory.verify`, `self.assertTrue`, `Path`, `memory.rendered_path.is_file`

**Node ID:** `tests/test_memory.py::MemoryTests::test_hash_chain`

Metadata: Toolkit behavior · line 21

### `MemoryTests::test_tamper_detection`

No test docstring is declared. The node identifier and direct call names are shown without inferring additional behavior.

**Direct call names in source:** `tempfile.TemporaryDirectory`, `ProjectMemory`, `memory.append`, `splitlines`, `json.loads`, `memory.events_path.write_text`, `memory.verify`, `self.assertFalse`, `Path`, `memory.events_path.read_text`, `json.dumps`

**Node ID:** `tests/test_memory.py::MemoryTests::test_tamper_detection`
