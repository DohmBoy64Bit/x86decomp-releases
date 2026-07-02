---
title: x86decomp_testkit.adapters.download
description: No module docstring is declared in the v0.7.4 source.
original_path: features/x86decomp-testkit-adapters-download.html
---

<a id="function-platform-key"></a>
<a id="function-github-latest-release"></a>
<a id="function-select-release-asset"></a>
<a id="function-download-file"></a>
<a id="function-safe-destination"></a>
<a id="function-safe-extract-archive"></a>

Section: Source-derived feature and function reference

# x86decomp_testkit.adapters.download

No module docstring is declared in the v0.7.4 source.

Metadata: verification harness · current · 6 functions/methods

**Source:** `test-suite/src/x86decomp_testkit/adapters/download.py`

> **Truth basis.** Module and symbol names, signatures, line numbers, docstrings, and SHA-256 are read directly from the sealed source. When source docstrings are absent, this page says so instead of inferring behavior. Source SHA-256: `60a341280d4c00b4289c4a0d6ef12e60b86331c5cd0dde794dbfe22ed40f5e77`.

## Functions and methods

Metadata: public · line 21

### platform_key

No function or method docstring is declared in the v0.7.4 source.

```
def platform_key() -> str
```

**Catalog symbol:** `x86decomp_testkit.adapters.download:platform_key`

Metadata: public · line 31

### github_latest_release

No function or method docstring is declared in the v0.7.4 source.

```
def github_latest_release(repository: str, timeout: int = 30) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp_testkit.adapters.download:github_latest_release`

Metadata: public · line 43

### select_release_asset

No function or method docstring is declared in the v0.7.4 source.

```
def select_release_asset(release: dict[str, Any], required_tokens: tuple[str, ...]) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp_testkit.adapters.download:select_release_asset`

Metadata: public · line 58

### download_file

No function or method docstring is declared in the v0.7.4 source.

```
def download_file(url: str, destination: Path, max_bytes: int = 2000000000) -> str
```

**Catalog symbol:** `x86decomp_testkit.adapters.download:download_file`

Metadata: internal · line 83

### _safe_destination

No function or method docstring is declared in the v0.7.4 source.

```
def _safe_destination(root: Path, member_name: str) -> Path
```

**Catalog symbol:** `x86decomp_testkit.adapters.download:_safe_destination`

Metadata: public · line 94

### safe_extract_archive

No function or method docstring is declared in the v0.7.4 source.

```
def safe_extract_archive(archive: Path, destination: Path, max_members: int = 200000) -> None
```

**Catalog symbol:** `x86decomp_testkit.adapters.download:safe_extract_archive`
