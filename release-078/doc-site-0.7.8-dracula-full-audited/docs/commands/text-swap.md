---
title: x86decomp text-swap
---

# `x86decomp text-swap`

Canonical text-swap commands implemented by the current capability subsystem.

## Usage

```text
usage: x86decomp text-swap [-h] [--project PROJECT] [--actor ACTOR]
                           {build,inject,plan,verify} ...
```

## Actions

| Action | Usage |
| --- | --- |
| `build` | `usage: x86decomp text-swap build [-h] --original ORIGINAL [--section-name SECTION_NAME] replacement output` |
| `inject` | `usage: x86decomp text-swap inject [-h] [--output OUTPUT] plan` |
| `plan` | `usage: x86decomp text-swap plan [-h] [--section-name SECTION_NAME] original replacement output` |
| `verify` | `usage: x86decomp text-swap verify [-h] [--output OUTPUT] plan image` |

## Canonical routes

| Route | Owner |
| --- | --- |
| `x86decomp text-swap build` | `reconstruction` |
| `x86decomp text-swap inject` | `reconstruction` |
| `x86decomp text-swap plan` | `reconstruction` |
| `x86decomp text-swap verify` | `reconstruction` |

## Verification boundary

This page is source-derived from the current parser. It does not claim that optional adapters, external tools, target inputs, or candidate artifacts exist in your environment.
