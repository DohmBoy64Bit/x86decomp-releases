---
title: x86decomp.workflow
description: Per-function decompilation mode and validation-state management.
---

# `x86decomp.workflow`

Per-function decompilation mode and validation-state management.

The workflow intentionally keeps matching and functional progress independent.
A function can be byte matched but not functionally exercised, or behaviorally
validated without reproducing the original instruction stream.

**Area:** Toolkit  
**Source:** `src/x86decomp/workflow.py`  
**SHA-256:** `cae8a093f08f66f9412393e59867c4d32ca7caf88533a175d22eebe1f325c0a5`  
**Functions/methods:** 7

> Module names, signatures, line numbers, and docstrings are extracted directly from the source AST. No behavior is inferred when a docstring is absent.

## Functions and methods

<a id="function-functionworkflow-to-dict"></a>

### `FunctionWorkflow.to_dict`

No function or method docstring is declared in the 0.7.5 source.

```python
def FunctionWorkflow.to_dict(self) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.workflow:FunctionWorkflow.to_dict`  
**Visibility:** public  
**Source line:** 79

<a id="function-functionworkflow-from-dict"></a>

### `FunctionWorkflow.from_dict`

No function or method docstring is declared in the 0.7.5 source.

```python
def FunctionWorkflow.from_dict(cls, value: Any) -> 'FunctionWorkflow'
```

**Catalog symbol:** `x86decomp.workflow:FunctionWorkflow.from_dict`  
**Visibility:** public  
**Source line:** 95

<a id="function-state-path"></a>

### `_state_path`

No function or method docstring is declared in the 0.7.5 source.

```python
def _state_path(project_root: Path, function_id: str) -> Path
```

**Catalog symbol:** `x86decomp.workflow:_state_path`  
**Visibility:** internal  
**Source line:** 126

<a id="function-initialize-function-workflow"></a>

### `initialize_function_workflow`

No function or method docstring is declared in the 0.7.5 source.

```python
def initialize_function_workflow(project_root: Path, *, function_id: str | None=None, rva: int | None=None, modes: set[DecompilationMode] | None=None) -> FunctionWorkflow
```

**Catalog symbol:** `x86decomp.workflow:initialize_function_workflow`  
**Visibility:** public  
**Source line:** 131

<a id="function-load-function-workflow"></a>

### `load_function_workflow`

No function or method docstring is declared in the 0.7.5 source.

```python
def load_function_workflow(project_root: Path, function_id: str) -> FunctionWorkflow
```

**Catalog symbol:** `x86decomp.workflow:load_function_workflow`  
**Visibility:** public  
**Source line:** 161

<a id="function-save-function-workflow"></a>

### `save_function_workflow`

No function or method docstring is declared in the 0.7.5 source.

```python
def save_function_workflow(project_root: Path, workflow: FunctionWorkflow) -> None
```

**Catalog symbol:** `x86decomp.workflow:save_function_workflow`  
**Visibility:** public  
**Source line:** 168

<a id="function-update-function-workflow"></a>

### `update_function_workflow`

No function or method docstring is declared in the 0.7.5 source.

```python
def update_function_workflow(project_root: Path, function_id: str, *, source_stage: SourceStage | None=None, matching_status: MatchingStatus | None=None, functional_status: FunctionalStatus | None=None, active_candidate: str | None=None, compiler_profile: str | None=None, report_kind: str | None=None, report_path: str | None=None, blocker: str | None=None, allow_regression: bool=False) -> FunctionWorkflow
```

**Catalog symbol:** `x86decomp.workflow:update_function_workflow`  
**Visibility:** public  
**Source line:** 173
