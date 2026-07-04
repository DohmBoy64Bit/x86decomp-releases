---
title: x86decomp decompiler
---

# `x86decomp decompiler`

Canonical decompiler commands implemented by the current capability subsystem.

## Usage

```text
usage: x86decomp decompiler [-h] [--project PROJECT] [--actor ACTOR]
                            {cleanup} ...
```

## Actions

| Action | Usage |
| --- | --- |
| `cleanup` | `usage: x86decomp decompiler cleanup [-h] [--compiler COMPILER] [--language LANGUAGE] [--locals-at-top] input_file output` |

## Canonical routes

| Route | Owner |
| --- | --- |
| `x86decomp decompiler cleanup` | `reconstruction` |

## Verification boundary

This page is source-derived from the current parser. It does not claim that optional adapters, external tools, target inputs, or candidate artifacts exist in your environment.
