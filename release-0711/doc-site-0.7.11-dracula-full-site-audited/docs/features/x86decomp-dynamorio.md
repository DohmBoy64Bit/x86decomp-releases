---
title: x86decomp.dynamorio
description: Module reference for x86decomp.dynamorio.
---

# `x86decomp.dynamorio`

- Area: `toolkit`
- Source path: `src/x86decomp/dynamorio.py`
- SHA-256: `8568a98326d91a775f2feec1847e8d3230c58253e1b015c3ee75dcb9b0d8b30d`
- Size: `8058` bytes
- Lines: `194`

## Module docstring

DynamoRIO drcov execution and text-log normalization.

This backend executes a user-authorized program under ``drrun -t drcov`` and
parses the text basic-block table. It never executes target programs implicitly;
the caller must invoke the command and supply the executable and arguments.

## Symbols

| Kind | Name | Line | Docstring summary |
| --- | --- | --- | --- |
| function | `parse_drcov_text` | 34 | Parse a drcov ``-dump_text`` log into stable module/block records. |
| function | `run_drcov_trace` | 118 | Execute an authorized program under drcov and normalize produced logs. |
