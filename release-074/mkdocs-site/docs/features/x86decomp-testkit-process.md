---
title: x86decomp_testkit.process
description: No module docstring is declared in the v0.7.4 source.
original_path: features/x86decomp-testkit-process.html
---

<a id="function-run-process-test"></a>
<a id="function-blocked-result"></a>

Section: Source-derived feature and function reference

# x86decomp_testkit.process

No module docstring is declared in the v0.7.4 source.

Metadata: verification harness · current · 2 functions/methods

**Source:** `test-suite/src/x86decomp_testkit/process.py`

> **Truth basis.** Module and symbol names, signatures, line numbers, docstrings, and SHA-256 are read directly from the sealed source. When source docstrings are absent, this page says so instead of inferring behavior. Source SHA-256: `1968fbfaad57ef05e06e85613d6efa7fedf1f2c57aab895bcf1e90cd2854dbf9`.

## Functions and methods

Metadata: public · line 14

### run_process_test

No function or method docstring is declared in the v0.7.4 source.

```
def run_process_test(*, test_id: str, suite: str, command: list[str], cwd: Path, output_directory: Path, timeout: int, environment: Mapping[str, str] | None = None, required_adapters: list[str] | None = None, event_logger: JsonlEventLogger | None = None, accepted_return_codes: tuple[int, ...] = (0,)) -> TestResult
```

**Catalog symbol:** `x86decomp_testkit.process:run_process_test`

Metadata: public · line 89

### blocked_result

No function or method docstring is declared in the v0.7.4 source.

```
def blocked_result(test_id: str, suite: str, missing_adapters: list[str], summary: str | None = None) -> TestResult
```

**Catalog symbol:** `x86decomp_testkit.process:blocked_result`
