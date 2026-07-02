---
title: x86decomp.test_bundle
description: Safe, static-only ingestion and analysis of user-supplied test bundles.
original_path: features/x86decomp-test-bundle.html
---

<a id="function-safe-member-path"></a>
<a id="function-is-symlink"></a>
<a id="function-validate-archive-infos"></a>
<a id="function-extract-safely"></a>
<a id="function-manifest-artifacts"></a>
<a id="function-single-role"></a>
<a id="function-create-test-bundle"></a>
<a id="function-inspect-test-bundle"></a>

Section: Source-derived feature and function reference

# x86decomp.test_bundle

Safe, static-only ingestion and analysis of user-supplied test bundles.

Metadata: core · current · 8 functions/methods

**Source:** `src/x86decomp/test_bundle.py`

> **Truth basis.** Module and symbol names, signatures, line numbers, docstrings, and SHA-256 are read directly from the sealed source. When source docstrings are absent, this page says so instead of inferring behavior. Source SHA-256: `7b65953eff2b3ba85cc543e11a8ab007f85565e85fe29e73e12db9eb099efc31`.

## Functions and methods

Metadata: internal · line 56

### _safe_member_path

No function or method docstring is declared in the v0.7.4 source.

```
def _safe_member_path(name: str) -> PurePosixPath
```

**Catalog symbol:** `x86decomp.test_bundle:_safe_member_path`

Metadata: internal · line 69

### _is_symlink

No function or method docstring is declared in the v0.7.4 source.

```
def _is_symlink(info: zipfile.ZipInfo) -> bool
```

**Catalog symbol:** `x86decomp.test_bundle:_is_symlink`

Metadata: internal · line 74

### _validate_archive_infos

No function or method docstring is declared in the v0.7.4 source.

```
def _validate_archive_infos(infos: list[zipfile.ZipInfo], limits: BundleLimits) -> None
```

**Catalog symbol:** `x86decomp.test_bundle:_validate_archive_infos`

Metadata: internal · line 103

### _extract_safely

No function or method docstring is declared in the v0.7.4 source.

```
def _extract_safely(archive: Path, destination: Path, limits: BundleLimits) -> None
```

**Catalog symbol:** `x86decomp.test_bundle:_extract_safely`

Metadata: internal · line 134

### _manifest_artifacts

No function or method docstring is declared in the v0.7.4 source.

```
def _manifest_artifacts(manifest: dict[str, Any], root: Path) -> list[dict[str, Any]]
```

**Catalog symbol:** `x86decomp.test_bundle:_manifest_artifacts`

Metadata: internal · line 187

### _single_role

No function or method docstring is declared in the v0.7.4 source.

```
def _single_role(artifacts: list[dict[str, Any]], role: str) -> Path | None
```

**Catalog symbol:** `x86decomp.test_bundle:_single_role`

Metadata: public · line 194

### create_test_bundle

Create a deterministic authorized static test bundle.

```
def create_test_bundle(output: Path, *, artifacts: list[tuple[str, Path]], authorization_statement: str, name: str | None = None, description: str | None = None, expected_architecture: str | None = None) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.test_bundle:create_test_bundle`

Metadata: public · line 281

### inspect_test_bundle

Verify and statically inspect a test bundle without executing its contents.

```
def inspect_test_bundle(archive: Path, *, report_path: Path | None = None, limits: BundleLimits | None = None) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.test_bundle:inspect_test_bundle`
