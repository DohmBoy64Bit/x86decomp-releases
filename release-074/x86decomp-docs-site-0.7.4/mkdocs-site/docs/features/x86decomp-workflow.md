---
title: x86decomp.workflow
description: Per-function decompilation mode and validation-state management.
original_path: features/x86decomp-workflow.html
---

<a id="function-functionworkflow-to-dict"></a>
<a id="function-functionworkflow-from-dict"></a>
<a id="function-state-path"></a>
<a id="function-initialize-function-workflow"></a>
<a id="function-load-function-workflow"></a>
<a id="function-save-function-workflow"></a>
<a id="function-update-function-workflow"></a>

Section: Source-derived feature and function reference

# x86decomp.workflow

Per-function decompilation mode and validation-state management.

Metadata: core · current · 7 functions/methods

**Source:** `src/x86decomp/workflow.py`

> **Truth basis.** Module and symbol names, signatures, line numbers, docstrings, and SHA-256 are read directly from the sealed source. When source docstrings are absent, this page says so instead of inferring behavior. Source SHA-256: `cae8a093f08f66f9412393e59867c4d32ca7caf88533a175d22eebe1f325c0a5`.

## Functions and methods

Metadata: public · line 79

### FunctionWorkflow.to_dict

No function or method docstring is declared in the v0.7.4 source.

```
def to_dict(self) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.workflow:FunctionWorkflow.to_dict`

Metadata: public · line 95

### FunctionWorkflow.from_dict

No function or method docstring is declared in the v0.7.4 source.

```
def from_dict(cls, value: Any) -> 'FunctionWorkflow'
```

**Catalog symbol:** `x86decomp.workflow:FunctionWorkflow.from_dict`

Metadata: internal · line 126

### _state_path

No function or method docstring is declared in the v0.7.4 source.

```
def _state_path(project_root: Path, function_id: str) -> Path
```

**Catalog symbol:** `x86decomp.workflow:_state_path`

Metadata: public · line 131

### initialize_function_workflow

No function or method docstring is declared in the v0.7.4 source.

```
def initialize_function_workflow(project_root: Path, *, function_id: str | None = None, rva: int | None = None, modes: set[DecompilationMode] | None = None) -> FunctionWorkflow
```

**Catalog symbol:** `x86decomp.workflow:initialize_function_workflow`

Metadata: public · line 161

### load_function_workflow

No function or method docstring is declared in the v0.7.4 source.

```
def load_function_workflow(project_root: Path, function_id: str) -> FunctionWorkflow
```

**Catalog symbol:** `x86decomp.workflow:load_function_workflow`

Metadata: public · line 168

### save_function_workflow

No function or method docstring is declared in the v0.7.4 source.

```
def save_function_workflow(project_root: Path, workflow: FunctionWorkflow) -> None
```

**Catalog symbol:** `x86decomp.workflow:save_function_workflow`

Metadata: public · line 173

### update_function_workflow

No function or method docstring is declared in the v0.7.4 source.

```
def update_function_workflow(project_root: Path, function_id: str, *, source_stage: SourceStage | None = None, matching_status: MatchingStatus | None = None, functional_status: FunctionalStatus | None = None, active_candidate: str | None = None, compiler_profile: str | None = None, report_kind: str | None = None, report_path: str | None = None, blocker: str | None = None, allow_regression: bool = False) -> FunctionWorkflow
```

**Catalog symbol:** `x86decomp.workflow:update_function_workflow`
