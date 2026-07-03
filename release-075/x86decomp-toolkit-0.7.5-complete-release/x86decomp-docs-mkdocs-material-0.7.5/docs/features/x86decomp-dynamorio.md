---
title: x86decomp.dynamorio
description: DynamoRIO drcov execution and text-log normalization.
---

# `x86decomp.dynamorio`

DynamoRIO drcov execution and text-log normalization.

This backend executes a user-authorized program under ``drrun -t drcov`` and
parses the text basic-block table. It never executes target programs implicitly;
the caller must invoke the command and supply the executable and arguments.

**Area:** Toolkit  
**Source:** `src/x86decomp/dynamorio.py`  
**SHA-256:** `8568a98326d91a775f2feec1847e8d3230c58253e1b015c3ee75dcb9b0d8b30d`  
**Functions/methods:** 2

> Module names, signatures, line numbers, and docstrings are extracted directly from the source AST. No behavior is inferred when a docstring is absent.

## Functions and methods

<a id="function-parse-drcov-text"></a>

### `parse_drcov_text`

Parse a drcov ``-dump_text`` log into stable module/block records.

```python
def parse_drcov_text(path: Path) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.dynamorio:parse_drcov_text`  
**Visibility:** public  
**Source line:** 34

<a id="function-run-drcov-trace"></a>

### `run_drcov_trace`

Execute an authorized program under drcov and normalize produced logs.

```python
def run_drcov_trace(executable: Path, *, program_arguments: list[str] | None=None, drrun: Path | None=None, output_directory: Path, timeout_seconds: int=300, report_path: Path | None=None) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.dynamorio:run_drcov_trace`  
**Visibility:** public  
**Source line:** 118
