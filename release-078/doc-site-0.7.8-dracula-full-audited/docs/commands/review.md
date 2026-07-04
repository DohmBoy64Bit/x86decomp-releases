---
title: x86decomp review
---

# `x86decomp review`

Canonical review commands implemented by the current capability subsystem.

## Usage

```text
usage: x86decomp review [-h] [--project PROJECT] [--actor ACTOR]
                        {assign,create,decide,list,lock,show} ...
```

## Actions

| Action | Usage |
| --- | --- |
| `assign` | `usage: x86decomp review assign [-h] review_id assignee` |
| `create` | `usage: x86decomp review create [-h] [--priority PRIORITY] [--details-json DETAILS_JSON] kind subject_id summary` |
| `decide` | `usage: x86decomp review decide [-h] --rationale RATIONALE [--lock] review_id decision` |
| `list` | `usage: x86decomp review list [-h] [--status STATUS] [--limit LIMIT]` |
| `lock` | `usage: x86decomp review lock [-h] review_id` |
| `show` | `usage: x86decomp review show [-h] review_id` |

## Canonical routes

| Route | Owner |
| --- | --- |
| `x86decomp review assign` | `governance` |
| `x86decomp review create` | `governance` |
| `x86decomp review decide` | `governance` |
| `x86decomp review list` | `governance` |
| `x86decomp review lock` | `governance` |
| `x86decomp review show` | `governance` |

## Verification boundary

This page is source-derived from the current parser. It does not claim that optional adapters, external tools, target inputs, or candidate artifacts exist in your environment.
