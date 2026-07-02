---
title: test-suite/tests/test_archive_security.py
description: 4 exact current test nodes
original_path: tests/test-suite-tests-test-archive-security.html
---

<a id="test-test-safe-zip-and-tar-extraction"></a>
<a id="test-test-rejects-traversal-and-links"></a>
<a id="test-test-release-asset-selection-is-deterministic"></a>
<a id="test-test-download-file-hash-and-size-limit"></a>

Section: Source-derived test reference

# `test-suite/tests/test_archive_security.py`

4 current test nodes in the Standalone verifier inventory.

> **Truth basis.** Node IDs, line numbers, docstrings, and direct call names are extracted from the AST. No behavior is inferred when a test lacks a docstring. Source SHA-256: `e731b4d36cbf94828e09245b2118b858bfd6c284e1d8a4be43c7f72b36412792`.

Metadata: Standalone verifier · line 13

### `test_safe_zip_and_tar_extraction`

No test docstring is declared. The node identifier and direct call names are shown without inferring additional behavior.

**Direct call names in source:** `safe_extract_archive`, `zipfile.ZipFile`, `zf.writestr`, `read_text`, `tarfile.open`, `tarfile.TarInfo`, `len`, `tf.addfile`, `read_bytes`, `io.BytesIO`

**Node ID:** `test-suite/tests/test_archive_security.py::test_safe_zip_and_tar_extraction`

Metadata: Standalone verifier · line 32

### `test_rejects_traversal_and_links`

No test docstring is declared. The node identifier and direct call names are shown without inferring additional behavior.

**Direct call names in source:** `zipfile.ZipFile`, `zf.writestr`, `pytest.raises`, `safe_extract_archive`, `tarfile.open`, `tarfile.TarInfo`, `tf.addfile`

**Node ID:** `test-suite/tests/test_archive_security.py::test_rejects_traversal_and_links`

Metadata: Standalone verifier · line 49

### `test_release_asset_selection_is_deterministic`

No test docstring is declared. The node identifier and direct call names are shown without inferring additional behavior.

**Direct call names in source:** `pytest.raises`, `select_release_asset`

**Node ID:** `test-suite/tests/test_archive_security.py::test_release_asset_selection_is_deterministic`

Metadata: Standalone verifier · line 58

### `test_download_file_hash_and_size_limit`

No test docstring is declared. The node identifier and direct call names are shown without inferring additional behavior.

**Direct call names in source:** `source.write_bytes`, `download_file`, `source.as_uri`, `destination.read_bytes`, `hexdigest`, `pytest.raises`, `hashlib.sha256`

**Node ID:** `test-suite/tests/test_archive_security.py::test_download_file_hash_and_size_limit`
