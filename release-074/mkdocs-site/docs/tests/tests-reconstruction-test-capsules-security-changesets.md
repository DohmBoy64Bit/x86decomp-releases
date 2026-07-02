---
title: tests/reconstruction/test_capsules_security_changesets.py
description: 4 exact current test nodes
original_path: tests/tests-reconstruction-test-capsules-security-changesets.html
---

<a id="test-test-capsule-is-deterministic-verifiable-and-reproducible"></a>
<a id="test-test-library-recognition-never-silently-replaces-code"></a>
<a id="test-test-security-scan-reports-without-modifying-behavior"></a>
<a id="test-test-semantic-changesets-detect-conflicts-and-verify-clean-merges"></a>

Section: Source-derived test reference

# `tests/reconstruction/test_capsules_security_changesets.py`

4 current test nodes in the Toolkit behavior inventory.

> **Truth basis.** Node IDs, line numbers, docstrings, and direct call names are extracted from the AST. No behavior is inferred when a test lacks a docstring. Source SHA-256: `a6b9cf3505de163803435daf9b909e5f7f1ead3a660325818faf379abe8979b4`.

Metadata: Toolkit behavior · line 12

### `test_capsule_is_deterministic_verifiable_and_reproducible`

No test docstring is declared. The node identifier and direct call names are shown without inferring additional behavior.

**Direct call names in source:** `mkdir`, `write_text`, `Capsules`, `api.create`, `api.inspect`, `api.reproduce`, `ReconstructionStore`, `api.verify`, `read_text`

**Node ID:** `tests/reconstruction/test_capsules_security_changesets.py::test_capsule_is_deterministic_verifiable_and_reproducible`

Metadata: Toolkit behavior · line 21

### `test_library_recognition_never_silently_replaces_code`

No test docstring is declared. The node identifier and direct call names are shown without inferring additional behavior.

**Direct call names in source:** `LibraryRecognition`, `api.identify`, `api.disposition`, `ReconstructionStore`, `api.candidates`

**Node ID:** `tests/reconstruction/test_capsules_security_changesets.py::test_library_recognition_never_silently_replaces_code`

Metadata: Toolkit behavior · line 28

### `test_security_scan_reports_without_modifying_behavior`

No test docstring is declared. The node identifier and direct call names are shown without inferring additional behavior.

**Direct call names in source:** `SecurityReview`, `api.scan`, `api.policy`, `ReconstructionStore`, `api.report`

**Node ID:** `tests/reconstruction/test_capsules_security_changesets.py::test_security_scan_reports_without_modifying_behavior`

Metadata: Toolkit behavior · line 35

### `test_semantic_changesets_detect_conflicts_and_verify_clean_merges`

No test docstring is declared. The node identifier and direct call names are shown without inferring additional behavior.

**Direct call names in source:** `SemanticChangeSets`, `api.create`, `api.add_operation`, `api.merge`, `api.rebase`, `ReconstructionStore`, `len`, `api.verify`, `api.conflicts`

**Node ID:** `tests/reconstruction/test_capsules_security_changesets.py::test_semantic_changesets_detect_conflicts_and_verify_clean_merges`
