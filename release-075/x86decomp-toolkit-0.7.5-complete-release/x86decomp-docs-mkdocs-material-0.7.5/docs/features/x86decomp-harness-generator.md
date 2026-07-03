---
title: x86decomp.harness_generator
description: Generate bounded differential-execution harnesses from explicit ABI facts.
---

# `x86decomp.harness_generator`

Generate bounded differential-execution harnesses from explicit ABI facts.

Generated values are deterministic test inputs, not recovered original inputs.
Pointer regions are allocated only when the user declares pointer parameters.

**Area:** Toolkit  
**Source:** `src/x86decomp/harness_generator.py`  
**SHA-256:** `75ab6f14bcef35574409e280dad90a705f71bc5763d507258f705ad8f4c431f2`  
**Functions/methods:** 3

> Module names, signatures, line numbers, and docstrings are extracted directly from the source AST. No behavior is inferred when a docstring is absent.

## Functions and methods

<a id="function-deterministic-word"></a>

### `_deterministic_word`

No function or method docstring is declared in the 0.7.5 source.

```python
def _deterministic_word(index: int, bits: int) -> int
```

**Catalog symbol:** `x86decomp.harness_generator:_deterministic_word`  
**Visibility:** internal  
**Source line:** 17

<a id="function-generate-execution-harness"></a>

### `generate_execution_harness`

No function or method docstring is declared in the 0.7.5 source.

```python
def generate_execution_harness(abi_contract: ABIContract, *, output: Path | None=None, pointer_parameters: list[dict[str, Any]] | None=None, observe_pointer_parameters: bool=True, max_instructions: int=100000, timeout_ms: int=1000) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.harness_generator:generate_execution_harness`  
**Visibility:** public  
**Source line:** 22

<a id="function-generate-execution-harness-from-files"></a>

### `generate_execution_harness_from_files`

No function or method docstring is declared in the 0.7.5 source.

```python
def generate_execution_harness_from_files(abi_contract_path: Path, output: Path, *, pointer_parameters_path: Path | None=None, observe_pointer_parameters: bool=True, max_instructions: int=100000, timeout_ms: int=1000) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.harness_generator:generate_execution_harness_from_files`  
**Visibility:** public  
**Source line:** 139
