---
title: x86decomp.compiler_worker
description: Module reference for x86decomp.compiler_worker.
---

# `x86decomp.compiler_worker`

- Area: `toolkit`
- Source path: `src/x86decomp/compiler_worker.py`
- SHA-256: `587489d60ee4c66870a3fb37ecadfb1f03d675902a5bb7438c066e6e9571cec9`
- Size: `5685` bytes
- Lines: `136`

## Module docstring

Isolated compiler-worker facade.

The facade copies declared inputs into an ephemeral workspace and invokes the
normal compiler profile through a bounded local or container worker.  Local mode
is explicitly not a security boundary; container mode is the production
isolation option.

## Symbols

| Kind | Name | Line | Docstring summary |
| --- | --- | --- | --- |
| function | `run_compiler_worker` | 23 | Run compiler worker for the current toolkit workflow. |
