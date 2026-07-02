---
title: x86decomp.release_gate
description: Target release acceptance gate.
original_path: features/x86decomp-release-gate.html
---

<a id="function-workflow-gate"></a>
<a id="function-claim-gate"></a>
<a id="function-pipeline-gate"></a>
<a id="function-evaluate-release-gate"></a>

Section: Source-derived feature and function reference

# x86decomp.release_gate

Target release acceptance gate.

Metadata: core · current · 4 functions/methods

**Source:** `src/x86decomp/release_gate.py`

> **Truth basis.** Module and symbol names, signatures, line numbers, docstrings, and SHA-256 are read directly from the sealed source. When source docstrings are absent, this page says so instead of inferring behavior. Source SHA-256: `8e79be8c5af67a90063af185b2239a5ce5a8ca828627ee05c14d897f891e02fd`.

## Functions and methods

Metadata: internal · line 32

### _workflow_gate

No function or method docstring is declared in the v0.7.4 source.

```
def _workflow_gate(root: Path, acceptance: dict[str, Any]) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.release_gate:_workflow_gate`

Metadata: internal · line 65

### _claim_gate

No function or method docstring is declared in the v0.7.4 source.

```
def _claim_gate(root: Path) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.release_gate:_claim_gate`

Metadata: internal · line 78

### _pipeline_gate

No function or method docstring is declared in the v0.7.4 source.

```
def _pipeline_gate(root: Path) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.release_gate:_pipeline_gate`

Metadata: public · line 92

### evaluate_release_gate

No function or method docstring is declared in the v0.7.4 source.

```
def evaluate_release_gate(project_root: Path, *, reproduction_manifest: Path | None = None, security_report: Path | None = None, convergence_report: Path | None = None, require_workflows: bool = False, require_verified_claims: bool = False, require_succeeded_pipelines: bool = False, report_path: Path | None = None) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.release_gate:evaluate_release_gate`
