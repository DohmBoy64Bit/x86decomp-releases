---
title: x86decomp.compiler_worker
description: Isolated compiler-worker facade.
---

# `x86decomp.compiler_worker`

Isolated compiler-worker facade.

The facade copies declared inputs into an ephemeral workspace and invokes the
normal compiler profile through a bounded local or container worker.  Local mode
is explicitly not a security boundary; container mode is the production
isolation option.

**Area:** Toolkit  
**Source:** `src/x86decomp/compiler_worker.py`  
**SHA-256:** `d13aa472af6cfb824c896d7a32c9c99ff7a4fcf07019dbba5aa42beba7f82045`  
**Functions/methods:** 1

> Module names, signatures, line numbers, and docstrings are extracted directly from the source AST. No behavior is inferred when a docstring is absent.

## Functions and methods

<a id="function-run-compiler-worker"></a>

### `run_compiler_worker`

No function or method docstring is declared in the 0.7.5 source.

```python
def run_compiler_worker(profile_path: Path, source_path: Path, output_path: Path, *, isolation: str='local_bounded', container_image: str | None=None, cache_directory: Path | None=None, report_path: Path | None=None, limits: WorkerLimits | None=None) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.compiler_worker:run_compiler_worker`  
**Visibility:** public  
**Source line:** 24
