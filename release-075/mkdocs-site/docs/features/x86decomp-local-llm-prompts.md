---
title: x86decomp.local_llm.prompts
description: Deterministic, injection-resistant prompts for C candidate generation.
---

# `x86decomp.local_llm.prompts`

Deterministic, injection-resistant prompts for C candidate generation.

**Area:** Toolkit  
**Source:** `src/x86decomp/local_llm/prompts.py`  
**SHA-256:** `b1a06cda047e95e59b0b415753e88bca82d111e6898c056880d972ac89e270e7`  
**Functions/methods:** 7

> Module names, signatures, line numbers, and docstrings are extracted directly from the source AST. No behavior is inferred when a docstring is absent.

## Functions and methods

<a id="function-text"></a>

### `_text`

No function or method docstring is declared in the 0.7.5 source.

```python
def _text(value: Any, field: str, *, required: bool=False) -> str
```

**Catalog symbol:** `x86decomp.local_llm.prompts:_text`  
**Visibility:** internal  
**Source line:** 15

<a id="function-integer"></a>

### `_integer`

No function or method docstring is declared in the 0.7.5 source.

```python
def _integer(value: Any, field: str, *, minimum: int=0) -> int
```

**Catalog symbol:** `x86decomp.local_llm.prompts:_integer`  
**Visibility:** internal  
**Source line:** 30

<a id="function-resolve-job-path"></a>

### `_resolve_job_path`

No function or method docstring is declared in the 0.7.5 source.

```python
def _resolve_job_path(job_path: Path, value: str, field: str) -> Path
```

**Catalog symbol:** `x86decomp.local_llm.prompts:_resolve_job_path`  
**Visibility:** internal  
**Source line:** 36

<a id="function-load-job"></a>

### `load_job`

Load and normalize a local-LLM generation/matching job.

```python
def load_job(job_path: Path) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.local_llm.prompts:load_job`  
**Visibility:** public  
**Source line:** 46

<a id="function-evidence-block"></a>

### `_evidence_block`

No function or method docstring is declared in the 0.7.5 source.

```python
def _evidence_block(job: dict[str, Any]) -> str
```

**Catalog symbol:** `x86decomp.local_llm.prompts:_evidence_block`  
**Visibility:** internal  
**Source line:** 128

<a id="function-build-messages"></a>

### `build_messages`

Build a deterministic two-message prompt with explicit trust boundaries.

```python
def build_messages(job: dict[str, Any], feedback: list[dict[str, Any]] | None=None) -> list[dict[str, str]]
```

**Catalog symbol:** `x86decomp.local_llm.prompts:build_messages`  
**Visibility:** public  
**Source line:** 142

<a id="function-prompt-record"></a>

### `prompt_record`

No function or method docstring is declared in the 0.7.5 source.

```python
def prompt_record(job: dict[str, Any], feedback: list[dict[str, Any]] | None=None) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.local_llm.prompts:prompt_record`  
**Visibility:** public  
**Source line:** 189
