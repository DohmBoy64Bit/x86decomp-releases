---
title: x86decomp.harness_generator
description: Generate bounded differential-execution harnesses from explicit ABI facts.
original_path: features/x86decomp-harness-generator.html
---

<a id="function-deterministic-word"></a>
<a id="function-generate-execution-harness"></a>
<a id="function-generate-execution-harness-from-files"></a>

Section: Source-derived feature and function reference

# x86decomp.harness_generator

Generate bounded differential-execution harnesses from explicit ABI facts.

Metadata: core · current · 3 functions/methods

**Source:** `src/x86decomp/harness_generator.py`

> **Truth basis.** Module and symbol names, signatures, line numbers, docstrings, and SHA-256 are read directly from the sealed source. When source docstrings are absent, this page says so instead of inferring behavior. Source SHA-256: `75ab6f14bcef35574409e280dad90a705f71bc5763d507258f705ad8f4c431f2`.

## Functions and methods

Metadata: internal · line 17

### _deterministic_word

No function or method docstring is declared in the v0.7.4 source.

```
def _deterministic_word(index: int, bits: int) -> int
```

**Catalog symbol:** `x86decomp.harness_generator:_deterministic_word`

Metadata: public · line 22

### generate_execution_harness

No function or method docstring is declared in the v0.7.4 source.

```
def generate_execution_harness(abi_contract: ABIContract, *, output: Path | None = None, pointer_parameters: list[dict[str, Any]] | None = None, observe_pointer_parameters: bool = True, max_instructions: int = 100000, timeout_ms: int = 1000) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.harness_generator:generate_execution_harness`

Metadata: public · line 139

### generate_execution_harness_from_files

No function or method docstring is declared in the v0.7.4 source.

```
def generate_execution_harness_from_files(abi_contract_path: Path, output: Path, *, pointer_parameters_path: Path | None = None, observe_pointer_parameters: bool = True, max_instructions: int = 100000, timeout_ms: int = 1000) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.harness_generator:generate_execution_harness_from_files`
