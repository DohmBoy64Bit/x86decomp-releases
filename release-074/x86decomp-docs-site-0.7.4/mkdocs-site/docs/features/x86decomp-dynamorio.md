---
title: x86decomp.dynamorio
description: DynamoRIO drcov execution and text-log normalization.
original_path: features/x86decomp-dynamorio.html
---

<a id="function-parse-drcov-text"></a>
<a id="function-run-drcov-trace"></a>

Section: Source-derived feature and function reference

# x86decomp.dynamorio

DynamoRIO drcov execution and text-log normalization.

Metadata: core · current · 2 functions/methods

**Source:** `src/x86decomp/dynamorio.py`

> **Truth basis.** Module and symbol names, signatures, line numbers, docstrings, and SHA-256 are read directly from the sealed source. When source docstrings are absent, this page says so instead of inferring behavior. Source SHA-256: `8568a98326d91a775f2feec1847e8d3230c58253e1b015c3ee75dcb9b0d8b30d`.

## Functions and methods

Metadata: public · line 34

### parse_drcov_text

Parse a drcov ``-dump_text`` log into stable module/block records.

```
def parse_drcov_text(path: Path) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.dynamorio:parse_drcov_text`

Metadata: public · line 118

### run_drcov_trace

Execute an authorized program under drcov and normalize produced logs.

```
def run_drcov_trace(executable: Path, *, program_arguments: list[str] | None = None, drrun: Path | None = None, output_directory: Path, timeout_seconds: int = 300, report_path: Path | None = None) -> dict[str, Any]
```

**Catalog symbol:** `x86decomp.dynamorio:run_drcov_trace`
