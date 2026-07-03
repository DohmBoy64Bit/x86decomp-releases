---
title: x86decomp.local_llm.matching
description: Local-model C generation and deterministic byte-match verification loop.
---

# `x86decomp.local_llm.matching`

Local-model C generation and deterministic byte-match verification loop.

**Area:** Toolkit  
**Source:** `src/x86decomp/local_llm/matching.py`  
**SHA-256:** `349c75f943aaf119368d8eef401330917b1f0abb7fd9f3bc114ccd12ec3c26b5`  
**Functions/methods:** 7

> Module names, signatures, line numbers, and docstrings are extracted directly from the source AST. No behavior is inferred when a docstring is absent.

## Functions and methods

<a id="function-parse-candidate"></a>

### `_parse_candidate`

No function or method docstring is declared in the 0.7.5 source.

```python
def _parse_candidate(content: str, *, function_name: str) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.local_llm.matching:_parse_candidate`  
**Visibility:** internal  
**Source line:** 36

<a id="function-prepare-output"></a>

### `_prepare_output`

No function or method docstring is declared in the 0.7.5 source.

```python
def _prepare_output(output_directory: Path, *, overwrite: bool) -> Path
```

**Catalog symbol:** `x86decomp.local_llm.matching:_prepare_output`  
**Visibility:** internal  
**Source line:** 91

<a id="function-feedback-from-compile"></a>

### `_feedback_from_compile`

No function or method docstring is declared in the 0.7.5 source.

```python
def _feedback_from_compile(report: dict[str, Any] | None, error: Exception) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.local_llm.matching:_feedback_from_compile`  
**Visibility:** internal  
**Source line:** 104

<a id="function-feedback-from-diff"></a>

### `_feedback_from_diff`

No function or method docstring is declared in the 0.7.5 source.

```python
def _feedback_from_diff(comparison: dict[str, Any], relocation: dict[str, Any]) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.local_llm.matching:_feedback_from_diff`  
**Visibility:** internal  
**Source line:** 114

<a id="function-generate-candidate"></a>

### `generate_candidate`

Generate and validate one uncompiled C proposal.

```python
def generate_candidate(profile_path: Path, job_path: Path, output: Path, *, overwrite: bool=False) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.local_llm.matching:generate_candidate`  
**Visibility:** public  
**Source line:** 127

<a id="function-run-match-loop"></a>

### `run_match_loop`

Run bounded local generation, compilation, relocation, and exact comparison.

```python
def run_match_loop(profile_path: Path, compiler_profile_path: Path, job_path: Path, output_directory: Path, *, max_attempts: int | None=None, overwrite: bool=False) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.local_llm.matching:run_match_loop`  
**Visibility:** public  
**Source line:** 171

<a id="function-verify-match-report"></a>

### `verify_match_report`

Verify report invariants and every referenced accepted artifact hash.

```python
def verify_match_report(report_path: Path) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.local_llm.matching:verify_match_report`  
**Visibility:** public  
**Source line:** 363
