---
title: x86decomp.release_gate
description: Target release acceptance gate.
---

# `x86decomp.release_gate`

Target release acceptance gate.

The gate aggregates exact project-state, evidence, workflow, pipeline,
reproducibility, security, and image-convergence records.  It never upgrades a
missing report into a pass and never treats the three-source rule as a guarantee
of semantic truth.

**Area:** Toolkit  
**Source:** `src/x86decomp/release_gate.py`  
**SHA-256:** `8e79be8c5af67a90063af185b2239a5ce5a8ca828627ee05c14d897f891e02fd`  
**Functions/methods:** 4

> Module names, signatures, line numbers, and docstrings are extracted directly from the source AST. No behavior is inferred when a docstring is absent.

## Functions and methods

<a id="function-workflow-gate"></a>

### `_workflow_gate`

No function or method docstring is declared in the 0.7.5 source.

```python
def _workflow_gate(root: Path, acceptance: dict[str, Any]) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.release_gate:_workflow_gate`  
**Visibility:** internal  
**Source line:** 32

<a id="function-claim-gate"></a>

### `_claim_gate`

No function or method docstring is declared in the 0.7.5 source.

```python
def _claim_gate(root: Path) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.release_gate:_claim_gate`  
**Visibility:** internal  
**Source line:** 65

<a id="function-pipeline-gate"></a>

### `_pipeline_gate`

No function or method docstring is declared in the 0.7.5 source.

```python
def _pipeline_gate(root: Path) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.release_gate:_pipeline_gate`  
**Visibility:** internal  
**Source line:** 78

<a id="function-evaluate-release-gate"></a>

### `evaluate_release_gate`

No function or method docstring is declared in the 0.7.5 source.

```python
def evaluate_release_gate(project_root: Path, *, reproduction_manifest: Path | None=None, security_report: Path | None=None, convergence_report: Path | None=None, require_workflows: bool=False, require_verified_claims: bool=False, require_succeeded_pipelines: bool=False, report_path: Path | None=None) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.release_gate:evaluate_release_gate`  
**Visibility:** public  
**Source line:** 92
