---
title: x86decomp.test_bundle
description: Module reference for x86decomp.test_bundle.
---

# `x86decomp.test_bundle`

- Area: `toolkit`
- Source path: `src/x86decomp/test_bundle.py`
- SHA-256: `e39fa02455b0bffa5ff85455eaf86bbaad76921df269e3b5cd8c7dc188cb8de3`
- Size: `19119` bytes
- Lines: `414`

## Module docstring

Safe, static-only ingestion and analysis of user-supplied test bundles.

A test bundle is a ZIP archive containing an explicit ``x86decomp-test-bundle.json``
manifest.  The default runner never executes any supplied binary or build script.
It performs integrity verification and invokes the toolkit's bounded static parsers.

This module is intentionally strict because ZIP archives and native binaries are
untrusted input even when the user has authorization to analyze them.

## Symbols

| Kind | Name | Line | Docstring summary |
| --- | --- | --- | --- |
| class | `BundleLimits` | 49 | Store validated bundle limits fields used by toolkit reports and adapters. |
| function | `_safe_member_path` | 57 | Support safe member path processing for internal toolkit callers. |
| function | `_is_symlink` | 71 | Support is symlink processing for internal toolkit callers. |
| function | `_validate_archive_infos` | 77 | Support validate archive infos processing for internal toolkit callers. |
| function | `_extract_safely` | 107 | Support extract safely processing for internal toolkit callers. |
| function | `_manifest_artifacts` | 139 | Support manifest artifacts processing for internal toolkit callers. |
| function | `_single_role` | 193 | Support single role processing for internal toolkit callers. |
| function | `create_test_bundle` | 201 | Create a deterministic authorized static test bundle. |
| function | `inspect_test_bundle` | 288 | Verify and statically inspect a test bundle without executing its contents. |
