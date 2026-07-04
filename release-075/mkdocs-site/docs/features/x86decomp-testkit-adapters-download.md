---
title: x86decomp_testkit.adapters.download
description: No module docstring is declared in the 0.7.5 source.
---

# `x86decomp_testkit.adapters.download`

No module docstring is declared in the 0.7.5 source.

**Area:** Verification harness  
**Source:** `test-suite/src/x86decomp_testkit/adapters/download.py`  
**SHA-256:** `401b21f76ba8bdb1437d3a36de425c5f3b581c4fc31caa7cc81ad47611399fc0`  
**Functions/methods:** 6

> Module names, signatures, line numbers, and docstrings are extracted directly from the source AST. No behavior is inferred when a docstring is absent.

## Functions and methods

<a id="function-platform-key"></a>

### `platform_key`

No function or method docstring is declared in the 0.7.5 source.

```python
def platform_key() -> str
```

**Catalog symbol:** `x86decomp_testkit.adapters.download:platform_key`  
**Visibility:** public  
**Source line:** 21

<a id="function-github-latest-release"></a>

### `github_latest_release`

No function or method docstring is declared in the 0.7.5 source.

```python
def github_latest_release(repository: str, timeout: int=30) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp_testkit.adapters.download:github_latest_release`  
**Visibility:** public  
**Source line:** 31

<a id="function-select-release-asset"></a>

### `select_release_asset`

No function or method docstring is declared in the 0.7.5 source.

```python
def select_release_asset(release: dict[str, Any], required_tokens: tuple[str, ...]) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp_testkit.adapters.download:select_release_asset`  
**Visibility:** public  
**Source line:** 43

<a id="function-download-file"></a>

### `download_file`

No function or method docstring is declared in the 0.7.5 source.

```python
def download_file(url: str, destination: Path, max_bytes: int=2000000000) -> str
```

**Catalog symbol:** `x86decomp_testkit.adapters.download:download_file`  
**Visibility:** public  
**Source line:** 58

<a id="function-safe-destination"></a>

### `_safe_destination`

No function or method docstring is declared in the 0.7.5 source.

```python
def _safe_destination(root: Path, member_name: str) -> Path
```

**Catalog symbol:** `x86decomp_testkit.adapters.download:_safe_destination`  
**Visibility:** internal  
**Source line:** 83

<a id="function-safe-extract-archive"></a>

### `safe_extract_archive`

No function or method docstring is declared in the 0.7.5 source.

```python
def safe_extract_archive(archive: Path, destination: Path, max_members: int=200000) -> None
```

**Catalog symbol:** `x86decomp_testkit.adapters.download:safe_extract_archive`  
**Visibility:** public  
**Source line:** 94
