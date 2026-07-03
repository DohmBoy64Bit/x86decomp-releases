---
title: x86decomp_testkit.process
description: No module docstring is declared in the 0.7.5 source.
---

# `x86decomp_testkit.process`

No module docstring is declared in the 0.7.5 source.

**Area:** Verification harness  
**Source:** `test-suite/src/x86decomp_testkit/process.py`  
**SHA-256:** `1968fbfaad57ef05e06e85613d6efa7fedf1f2c57aab895bcf1e90cd2854dbf9`  
**Functions/methods:** 2

> Module names, signatures, line numbers, and docstrings are extracted directly from the source AST. No behavior is inferred when a docstring is absent.

## Functions and methods

<a id="function-run-process-test"></a>

### `run_process_test`

No function or method docstring is declared in the 0.7.5 source.

```python
def run_process_test(*, test_id: str, suite: str, command: list[str], cwd: Path, output_directory: Path, timeout: int, environment: Mapping[str, str] | None=None, required_adapters: list[str] | None=None, event_logger: JsonlEventLogger | None=None, accepted_return_codes: tuple[int, ...]=(0,)) -> TestResult
```

**Catalog symbol:** `x86decomp_testkit.process:run_process_test`  
**Visibility:** public  
**Source line:** 14

<a id="function-blocked-result"></a>

### `blocked_result`

No function or method docstring is declared in the 0.7.5 source.

```python
def blocked_result(test_id: str, suite: str, missing_adapters: list[str], summary: str | None=None) -> TestResult
```

**Catalog symbol:** `x86decomp_testkit.process:blocked_result`  
**Visibility:** public  
**Source line:** 89
