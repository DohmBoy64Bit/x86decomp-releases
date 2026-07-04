---
title: x86decomp.security_audit
description: Release/project security auditing and SBOM generation.
---

# `x86decomp.security_audit`

Release/project security auditing and SBOM generation.

The audit is deterministic and offline.  It inventories dependencies and risky
filesystem state; vulnerability databases require an external scanner and are
reported as unavailable rather than fabricated.

**Area:** Toolkit  
**Source:** `src/x86decomp/security_audit.py`  
**SHA-256:** `6131424e2b3443bd0e6af244fdcf2418a36ea752afa838a124d5e98bedd913d5`  
**Functions/methods:** 5

> Module names, signatures, line numbers, and docstrings are extracted directly from the source AST. No behavior is inferred when a docstring is absent.

## Functions and methods

<a id="function-secret-findings"></a>

### `_secret_findings`

No function or method docstring is declared in the 0.7.5 source.

```python
def _secret_findings(text: str) -> list[dict[str, str]]
```

**Catalog symbol:** `x86decomp.security_audit:_secret_findings`  
**Visibility:** internal  
**Source line:** 30

<a id="function-generate-sbom"></a>

### `generate_sbom`

No function or method docstring is declared in the 0.7.5 source.

```python
def generate_sbom(output: Path | None=None) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.security_audit:generate_sbom`  
**Visibility:** public  
**Source line:** 43

<a id="function-audit-source-tree"></a>

### `audit_source_tree`

No function or method docstring is declared in the 0.7.5 source.

```python
def audit_source_tree(root: Path, *, report_path: Path | None=None) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.security_audit:audit_source_tree`  
**Visibility:** public  
**Source line:** 78

<a id="function-verify-release-manifest"></a>

### `verify_release_manifest`

No function or method docstring is declared in the 0.7.5 source.

```python
def verify_release_manifest(root: Path, manifest_path: Path | None=None) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.security_audit:verify_release_manifest`  
**Visibility:** public  
**Source line:** 133

<a id="function-run-dependency-vulnerability-audit"></a>

### `run_dependency_vulnerability_audit`

Run an installed pip-audit executable and preserve its exact findings.

Exit code 1 is accepted when the tool produced a valid vulnerability report.
Missing tools and malformed output are errors, never silent passes.

```python
def run_dependency_vulnerability_audit(*, executable: str='pip-audit', report_path: Path | None=None, timeout_seconds: int=300) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.security_audit:run_dependency_vulnerability_audit`  
**Visibility:** public  
**Source line:** 164
