---
title: x86decomp.test_bundle
description: Safe, static-only ingestion and analysis of user-supplied test bundles.
---

# `x86decomp.test_bundle`

Safe, static-only ingestion and analysis of user-supplied test bundles.

A test bundle is a ZIP archive containing an explicit ``x86decomp-test-bundle.json``
manifest.  The default runner never executes any supplied binary or build script.
It performs integrity verification and invokes the toolkit's bounded static parsers.

This module is intentionally strict because ZIP archives and native binaries are
untrusted input even when the user has authorization to analyze them.

**Area:** Toolkit  
**Source:** `src/x86decomp/test_bundle.py`  
**SHA-256:** `7b65953eff2b3ba85cc543e11a8ab007f85565e85fe29e73e12db9eb099efc31`  
**Functions/methods:** 8

> Module names, signatures, line numbers, and docstrings are extracted directly from the source AST. No behavior is inferred when a docstring is absent.

## Functions and methods

<a id="function-safe-member-path"></a>

### `_safe_member_path`

No function or method docstring is declared in the 0.7.5 source.

```python
def _safe_member_path(name: str) -> PurePosixPath
```

**Catalog symbol:** `x86decomp.test_bundle:_safe_member_path`  
**Visibility:** internal  
**Source line:** 56

<a id="function-is-symlink"></a>

### `_is_symlink`

No function or method docstring is declared in the 0.7.5 source.

```python
def _is_symlink(info: zipfile.ZipInfo) -> bool
```

**Catalog symbol:** `x86decomp.test_bundle:_is_symlink`  
**Visibility:** internal  
**Source line:** 69

<a id="function-validate-archive-infos"></a>

### `_validate_archive_infos`

No function or method docstring is declared in the 0.7.5 source.

```python
def _validate_archive_infos(infos: list[zipfile.ZipInfo], limits: BundleLimits) -> None
```

**Catalog symbol:** `x86decomp.test_bundle:_validate_archive_infos`  
**Visibility:** internal  
**Source line:** 74

<a id="function-extract-safely"></a>

### `_extract_safely`

No function or method docstring is declared in the 0.7.5 source.

```python
def _extract_safely(archive: Path, destination: Path, limits: BundleLimits) -> None
```

**Catalog symbol:** `x86decomp.test_bundle:_extract_safely`  
**Visibility:** internal  
**Source line:** 103

<a id="function-manifest-artifacts"></a>

### `_manifest_artifacts`

No function or method docstring is declared in the 0.7.5 source.

```python
def _manifest_artifacts(manifest: dict[str, Any], root: Path) -> list[dict[str, Any]]
```

**Catalog symbol:** `x86decomp.test_bundle:_manifest_artifacts`  
**Visibility:** internal  
**Source line:** 134

<a id="function-single-role"></a>

### `_single_role`

No function or method docstring is declared in the 0.7.5 source.

```python
def _single_role(artifacts: list[dict[str, Any]], role: str) -> Path | None
```

**Catalog symbol:** `x86decomp.test_bundle:_single_role`  
**Visibility:** internal  
**Source line:** 187

<a id="function-create-test-bundle"></a>

### `create_test_bundle`

Create a deterministic authorized static test bundle.

Each artifact tuple is ``(role, path)``. Files are copied into the archive;
no supplied content is executed. The archive is validated after creation.

```python
def create_test_bundle(output: Path, *, artifacts: list[tuple[str, Path]], authorization_statement: str, name: str | None=None, description: str | None=None, expected_architecture: str | None=None) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.test_bundle:create_test_bundle`  
**Visibility:** public  
**Source line:** 194

<a id="function-inspect-test-bundle"></a>

### `inspect_test_bundle`

Verify and statically inspect a test bundle without executing its contents.

```python
def inspect_test_bundle(archive: Path, *, report_path: Path | None=None, limits: BundleLimits | None=None) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.test_bundle:inspect_test_bundle`  
**Visibility:** public  
**Source line:** 281
