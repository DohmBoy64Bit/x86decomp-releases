---
title: x86decomp hypothesis
---

# `x86decomp hypothesis`

Canonical hypothesis commands implemented by the current capability subsystem.

## Usage

```text
usage: x86decomp hypothesis [-h] [--project PROJECT] [--actor ACTOR]
                            {create,dependency,evidence,gate,list,show,transition} ...
```

## Actions

| Action | Usage |
| --- | --- |
| `create` | `usage: x86decomp hypothesis create [-h] --origin ORIGIN statement scope_kind scope_id` |
| `dependency` | `usage: x86decomp hypothesis dependency [-h] hypothesis_id depends_on_id` |
| `evidence` | `usage: x86decomp hypothesis evidence [-h] --stance STANCE --weight WEIGHT --kind KIND --group GROUP [--artifact-sha256 ARTIFACT_SHA256] [--details-json DETAILS_JSON] hypothesis_id evidence_id` |
| `gate` | `usage: x86decomp hypothesis gate [-h] hypothesis_id` |
| `list` | `usage: x86decomp hypothesis list [-h] [--state STATE] [--scope-id SCOPE_ID]` |
| `show` | `usage: x86decomp hypothesis show [-h] hypothesis_id` |
| `transition` | `usage: x86decomp hypothesis transition [-h] --reason REASON [--lock] hypothesis_id state` |

## Canonical routes

| Route | Owner |
| --- | --- |
| `x86decomp hypothesis create` | `governance` |
| `x86decomp hypothesis dependency` | `governance` |
| `x86decomp hypothesis evidence` | `governance` |
| `x86decomp hypothesis gate` | `governance` |
| `x86decomp hypothesis list` | `governance` |
| `x86decomp hypothesis show` | `governance` |
| `x86decomp hypothesis transition` | `governance` |

## Verification boundary

This page is source-derived from the current parser. It does not claim that optional adapters, external tools, target inputs, or candidate artifacts exist in your environment.
