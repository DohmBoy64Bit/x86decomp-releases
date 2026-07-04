---
title: x86decomp source-map
---

# `x86decomp source-map`

Canonical source-map commands implemented by the current capability subsystem.

## Usage

```text
usage: x86decomp source-map [-h] [--project PROJECT] [--actor ACTOR]
                            {annotate,verify} ...
```

## Actions

| Action | Usage |
| --- | --- |
| `annotate` | `usage: x86decomp source-map annotate [-h] [--binary BINARY] [--report REPORT] source_root` |
| `verify` | `usage: x86decomp source-map verify [-h] [--report REPORT] source_root` |

## Canonical routes

| Route | Owner |
| --- | --- |
| `x86decomp source-map annotate` | `reconstruction` |
| `x86decomp source-map verify` | `reconstruction` |

## Verification boundary

This page is source-derived from the current parser. It does not claim that optional adapters, external tools, target inputs, or candidate artifacts exist in your environment.
