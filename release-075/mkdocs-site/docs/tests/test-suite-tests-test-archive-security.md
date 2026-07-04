---
title: test-suite/tests/test_archive_security.py
description: Source-derived reference for 4 collected test nodes.
---

# `test-suite/tests/test_archive_security.py`

**Collected nodes:** 4  
**Source SHA-256:** `e731b4d36cbf94828e09245b2118b858bfd6c284e1d8a4be43c7f72b36412792`

> Node identifiers, source lines, docstrings, and direct call names are extracted from pytest collection and the source AST. No behavior is inferred when a test has no docstring.

## `test_safe_zip_and_tar_extraction`

No test docstring is declared.

**Direct call names in source:** `(out / 'root' / 'file.txt').read_text`, `(out2 / 'root' / 'file.txt').read_bytes`, `io.BytesIO`, `len`, `safe_extract_archive`, `tarfile.TarInfo`, `tarfile.open`, `tf.addfile`, `zf.writestr`, `zipfile.ZipFile`  
**Node ID:** `tests/test_archive_security.py::test_safe_zip_and_tar_extraction`  
**Area:** Standalone verification harness  
**Source line:** 13

## `test_rejects_traversal_and_links`

No test docstring is declared.

**Direct call names in source:** `pytest.raises`, `safe_extract_archive`, `tarfile.TarInfo`, `tarfile.open`, `tf.addfile`, `zf.writestr`, `zipfile.ZipFile`  
**Node ID:** `tests/test_archive_security.py::test_rejects_traversal_and_links`  
**Area:** Standalone verification harness  
**Source line:** 32

## `test_release_asset_selection_is_deterministic`

No test docstring is declared.

**Direct call names in source:** `pytest.raises`, `select_release_asset`  
**Node ID:** `tests/test_archive_security.py::test_release_asset_selection_is_deterministic`  
**Area:** Standalone verification harness  
**Source line:** 49

## `test_download_file_hash_and_size_limit`

No test docstring is declared.

**Direct call names in source:** `destination.read_bytes`, `download_file`, `hashlib.sha256`, `hashlib.sha256(b'abc').hexdigest`, `pytest.raises`, `source.as_uri`, `source.write_bytes`  
**Node ID:** `tests/test_archive_security.py::test_download_file_hash_and_size_limit`  
**Area:** Standalone verification harness  
**Source line:** 58
