---
title: x86decomp windows
---

# `x86decomp windows`

Canonical windows commands implemented by the current capability subsystem.

## Usage

```text
usage: x86decomp windows [-h] [--project PROJECT] [--actor ACTOR]
                         {discover-ghidra,doctor,response-file} ...
```

## Actions

| Action | Usage |
| --- | --- |
| `discover-ghidra` | `usage: x86decomp windows discover-ghidra [-h] [--ghidra-home GHIDRA_HOME] [--platform-name PLATFORM_NAME]` |
| `doctor` | `usage: x86decomp windows doctor [-h] [--ghidra-home GHIDRA_HOME]` |
| `response-file` | `usage: x86decomp windows response-file [-h] output arguments_json` |

## Canonical routes

| Route | Owner |
| --- | --- |
| `x86decomp windows discover-ghidra` | `native` |
| `x86decomp windows doctor` | `native` |
| `x86decomp windows response-file` | `native` |

## Verification boundary

This page is source-derived from the current parser. It does not claim that optional adapters, external tools, target inputs, or candidate artifacts exist in your environment.
