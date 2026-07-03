---
title: tests/reconstruction/test_capsules_security_changesets.py
description: Source-derived reference for 4 collected test nodes.
---

# `tests/reconstruction/test_capsules_security_changesets.py`

**Collected nodes:** 4  
**Source SHA-256:** `59cac792da40127ce5f720a150756ec984e6fcbf0cca358237dd9deee1b24ae2`

> Node identifiers, source lines, docstrings, and direct call names are extracted from pytest collection and the source AST. No behavior is inferred when a test has no docstring.

## `test_capsule_is_deterministic_verifiable_and_reproducible`

No test docstring is declared.

**Direct call names in source:** `(tmp_path / 'reproduced/src/a.c').read_text`, `(tmp_path / 'src').mkdir`, `(tmp_path / 'src/a.c').write_text`, `Capsules`, `ReconstructionStore`, `api.create`, `api.inspect`, `api.reproduce`, `api.verify`  
**Node ID:** `tests/reconstruction/test_capsules_security_changesets.py::test_capsule_is_deterministic_verifiable_and_reproducible`  
**Area:** Toolkit behavior  
**Source line:** 12

## `test_library_recognition_never_silently_replaces_code`

No test docstring is declared.

**Direct call names in source:** `LibraryRecognition`, `ReconstructionStore`, `api.candidates`, `api.disposition`, `api.identify`  
**Node ID:** `tests/reconstruction/test_capsules_security_changesets.py::test_library_recognition_never_silently_replaces_code`  
**Area:** Toolkit behavior  
**Source line:** 21

## `test_security_scan_reports_without_modifying_behavior`

No test docstring is declared.

**Direct call names in source:** `ReconstructionStore`, `SecurityReview`, `api.policy`, `api.report`, `api.scan`  
**Node ID:** `tests/reconstruction/test_capsules_security_changesets.py::test_security_scan_reports_without_modifying_behavior`  
**Area:** Toolkit behavior  
**Source line:** 28

## `test_semantic_changesets_detect_conflicts_and_verify_clean_merges`

No test docstring is declared.

**Direct call names in source:** `ReconstructionStore`, `SemanticChangeSets`, `api.add_operation`, `api.conflicts`, `api.create`, `api.merge`, `api.rebase`, `api.verify`, `len`  
**Node ID:** `tests/reconstruction/test_capsules_security_changesets.py::test_semantic_changesets_detect_conflicts_and_verify_clean_merges`  
**Area:** Toolkit behavior  
**Source line:** 35
