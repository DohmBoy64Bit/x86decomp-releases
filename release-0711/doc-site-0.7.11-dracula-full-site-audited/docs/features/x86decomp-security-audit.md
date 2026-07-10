---
title: x86decomp.security_audit
description: Module reference for x86decomp.security_audit.
---

# `x86decomp.security_audit`

- Area: `toolkit`
- Source path: `src/x86decomp/security_audit.py`
- SHA-256: `908cac0bdfd28cbd619ecf628ebee71753c735617f4570b3a07f36a35c8dfb6c`
- Size: `10037` bytes
- Lines: `242`

## Module docstring

Release/project security auditing and SBOM generation.

The audit is deterministic and offline.  It inventories dependencies and risky
filesystem state; vulnerability databases require an external scanner and are
reported as unavailable rather than fabricated.

## Symbols

| Kind | Name | Line | Docstring summary |
| --- | --- | --- | --- |
| function | `_secret_findings` | 30 | Support secret findings processing for internal toolkit callers. |
| function | `generate_sbom` | 44 | Generate sbom for the current toolkit workflow. |
| function | `audit_source_tree` | 80 | Audit source tree for the current toolkit workflow. |
| function | `verify_release_manifest` | 136 | Verify release manifest for the current toolkit workflow. |
| function | `run_dependency_vulnerability_audit` | 168 | Run an installed pip-audit executable and preserve its exact findings. |
