---
title: x86decomp family
---

# `x86decomp family`

Canonical family commands implemented by the current capability subsystem.

## Usage

```text
usage: x86decomp family [-h] [--project PROJECT] [--actor ACTOR]
                        {add,correlate,create,report} ...
```

## Actions

| Action | Usage |
| --- | --- |
| `add` | `usage: x86decomp family add [-h] [--metadata-json METADATA_JSON] family_id label path` |
| `correlate` | `usage: x86decomp family correlate [-h] [--block-size BLOCK_SIZE] left_member_id right_member_id` |
| `create` | `usage: x86decomp family create [-h] name` |
| `report` | `usage: x86decomp family report [-h] family_id` |

## Canonical routes

| Route | Owner |
| --- | --- |
| `x86decomp family add` | `governance` |
| `x86decomp family correlate` | `governance` |
| `x86decomp family create` | `governance` |
| `x86decomp family report` | `governance` |

## Verification boundary

This page is source-derived from the current parser. It does not claim that optional adapters, external tools, target inputs, or candidate artifacts exist in your environment.
