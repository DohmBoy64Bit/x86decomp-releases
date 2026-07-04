---
title: x86decomp staging
---

# `x86decomp staging`

Canonical staging commands implemented by the current capability subsystem.

## Usage

```text
usage: x86decomp staging [-h] [--project PROJECT] [--actor ACTOR]
                         {compile-check,generate-context,resolve,scan,unresolved} ...
```

## Actions

| Action | Usage |
| --- | --- |
| `compile-check` | `usage: x86decomp staging compile-check [-h] [--cwd CWD] [--timeout TIMEOUT] command_json` |
| `generate-context` | `usage: x86decomp staging generate-context [-h] output sources [sources ...]` |
| `resolve` | `usage: x86decomp staging resolve [-h] mapping_json` |
| `scan` | `usage: x86decomp staging scan [-h] sources [sources ...]` |
| `unresolved` | `usage: x86decomp staging unresolved [-h]` |

## Canonical routes

| Route | Owner |
| --- | --- |
| `x86decomp staging compile-check` | `native` |
| `x86decomp staging generate-context` | `native` |
| `x86decomp staging resolve` | `native` |
| `x86decomp staging scan` | `native` |
| `x86decomp staging unresolved` | `native` |

## Verification boundary

This page is source-derived from the current parser. It does not claim that optional adapters, external tools, target inputs, or candidate artifacts exist in your environment.
