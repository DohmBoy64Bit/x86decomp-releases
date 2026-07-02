---
title: x86decomp.compiler_worker
description: Isolated compiler-worker facade.
original_path: features/x86decomp-compiler-worker.html
---

<a id="function-run-compiler-worker"></a>

Section: Source-derived feature and function reference

# x86decomp.compiler_worker

Isolated compiler-worker facade.

Metadata: core · current · 1 functions/methods

**Source:** `src/x86decomp/compiler_worker.py`

> **Truth basis.** Module and symbol names, signatures, line numbers, docstrings, and SHA-256 are read directly from the sealed source. When source docstrings are absent, this page says so instead of inferring behavior. Source SHA-256: `d13aa472af6cfb824c896d7a32c9c99ff7a4fcf07019dbba5aa42beba7f82045`.

## Functions and methods

Metadata: public · line 24

### run_compiler_worker

No function or method docstring is declared in the v0.7.4 source.

```
def run_compiler_worker(profile_path: Path, source_path: Path, output_path: Path, *, isolation: str = 'local_bounded', container_image: str | None = None, cache_directory: Path | None = None, report_path: Path | None = None, limits: WorkerLimits | None = None) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.compiler_worker:run_compiler_worker`
