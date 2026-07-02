---
title: x86decomp.security_audit
description: Release/project security auditing and SBOM generation.
original_path: features/x86decomp-security-audit.html
---

<a id="function-secret-findings"></a>
<a id="function-generate-sbom"></a>
<a id="function-audit-source-tree"></a>
<a id="function-verify-release-manifest"></a>
<a id="function-run-dependency-vulnerability-audit"></a>

Section: Source-derived feature and function reference

# x86decomp.security_audit

Release/project security auditing and SBOM generation.

Metadata: core · current · 5 functions/methods

**Source:** `src/x86decomp/security_audit.py`

> **Truth basis.** Module and symbol names, signatures, line numbers, docstrings, and SHA-256 are read directly from the sealed source. When source docstrings are absent, this page says so instead of inferring behavior. Source SHA-256: `274c689b0141c11b2376e087427f13b55dc9e87beb3ee8e40851dad5d8e2ba1d`.

## Functions and methods

Metadata: internal · line 30

### _secret_findings

No function or method docstring is declared in the v0.7.4 source.

```
def _secret_findings(text: str) -> list[dict[str, str]]
```

**Catalog symbol:** `x86decomp.security_audit:_secret_findings`

Metadata: public · line 43

### generate_sbom

No function or method docstring is declared in the v0.7.4 source.

```
def generate_sbom(output: Path | None = None) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.security_audit:generate_sbom`

Metadata: public · line 78

### audit_source_tree

No function or method docstring is declared in the v0.7.4 source.

```
def audit_source_tree(root: Path, *, report_path: Path | None = None) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.security_audit:audit_source_tree`

Metadata: public · line 133

### verify_release_manifest

No function or method docstring is declared in the v0.7.4 source.

```
def verify_release_manifest(root: Path, manifest_path: Path | None = None) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.security_audit:verify_release_manifest`

Metadata: public · line 164

### run_dependency_vulnerability_audit

Run an installed pip-audit executable and preserve its exact findings.

```
def run_dependency_vulnerability_audit(*, executable: str = 'pip-audit', report_path: Path | None = None, timeout_seconds: int = 300) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.security_audit:run_dependency_vulnerability_audit`
