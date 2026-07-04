---
title: x86decomp runtime-analysis
---

# `x86decomp runtime-analysis`

Canonical runtime-analysis commands implemented by the current capability subsystem.

## Usage

```text
usage: x86decomp runtime-analysis [-h] [--project PROJECT] [--actor ACTOR]
                                  {identify,match-library,quarantine} ...
```

## Actions

| Action | Usage |
| --- | --- |
| `identify` | `usage: x86decomp runtime-analysis identify [-h] [--output OUTPUT]` |
| `match-library` | `usage: x86decomp runtime-analysis match-library [-h] [--output OUTPUT] library_inventory` |
| `quarantine` | `usage: x86decomp runtime-analysis quarantine [-h] [--output OUTPUT] identification_report` |

## Canonical routes

| Route | Owner |
| --- | --- |
| `x86decomp runtime-analysis identify` | `reconstruction` |
| `x86decomp runtime-analysis match-library` | `reconstruction` |
| `x86decomp runtime-analysis quarantine` | `reconstruction` |

## Verification boundary

This page is source-derived from the current parser. It does not claim that optional adapters, external tools, target inputs, or candidate artifacts exist in your environment.
