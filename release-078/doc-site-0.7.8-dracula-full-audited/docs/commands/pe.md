---
title: x86decomp pe
---

# `x86decomp pe`

Canonical pe commands implemented by the current capability subsystem.

## Usage

```text
usage: x86decomp pe [-h] [--project PROJECT] [--actor ACTOR]
                    {export-coff,export-sections,inventory,patch-apply,patch-plan,text-swap} ...
```

## Actions

| Action | Usage |
| --- | --- |
| `export-coff` | `usage: x86decomp pe export-coff [-h] [--section SECTION] image output` |
| `export-sections` | `usage: x86decomp pe export-sections [-h] [--section SECTION] image output` |
| `inventory` | `usage: x86decomp pe inventory [-h] image` |
| `patch-apply` | `usage: x86decomp pe patch-apply [-h] plan_id` |
| `patch-plan` | `usage: x86decomp pe patch-plan [-h] original output operations_json` |
| `text-swap` | `usage: x86decomp pe text-swap [-h] [--section-name SECTION_NAME] original replacement output` |

## Canonical routes

| Route | Owner |
| --- | --- |
| `x86decomp pe export-coff` | `native` |
| `x86decomp pe export-sections` | `native` |
| `x86decomp pe inventory` | `native` |
| `x86decomp pe patch-apply` | `native` |
| `x86decomp pe patch-plan` | `native` |
| `x86decomp pe text-swap` | `native` |

## Verification boundary

This page is source-derived from the current parser. It does not claim that optional adapters, external tools, target inputs, or candidate artifacts exist in your environment.
