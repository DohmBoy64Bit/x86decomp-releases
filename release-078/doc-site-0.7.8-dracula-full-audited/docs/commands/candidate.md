---
title: x86decomp candidate
---

# `x86decomp candidate`

Canonical candidate commands implemented by the current capability subsystem.

## Usage

```text
usage: x86decomp candidate [-h] [--project PROJECT] [--actor ACTOR]
                           {add-file,compare,create,evaluate,list,promote,search,show,transition} ...
```

## Actions

| Action | Usage |
| --- | --- |
| `add-file` | `usage: x86decomp candidate add-file [-h] candidate_id source relative_path` |
| `compare` | `usage: x86decomp candidate compare [-h] left_id right_id` |
| `create` | `usage: x86decomp candidate create [-h] [--campaign-id CAMPAIGN_ID] [--parent PARENT] [--objective-json OBJECTIVE_JSON] branch_name` |
| `evaluate` | `usage: x86decomp candidate evaluate [-h] [--value VALUE] [--details-json DETAILS_JSON] candidate_id metric status` |
| `list` | `usage: x86decomp candidate list [-h] [--campaign-id CAMPAIGN_ID]` |
| `promote` | `usage: x86decomp candidate promote [-h] --candidate CANDIDATE --report REPORT [--stage STAGE] [--update-workflow] [--update-build] [--overwrite] function_id` |
| `search` | `usage: x86decomp candidate search [-h] [--phase PHASE] [--output OUTPUT]` |
| `show` | `usage: x86decomp candidate show [-h] candidate_id` |
| `transition` | `usage: x86decomp candidate transition [-h] --reason REASON candidate_id state` |

## Canonical routes

| Route | Owner |
| --- | --- |
| `x86decomp candidate add-file` | `governance` |
| `x86decomp candidate compare` | `governance` |
| `x86decomp candidate create` | `governance` |
| `x86decomp candidate evaluate` | `governance` |
| `x86decomp candidate list` | `governance` |
| `x86decomp candidate promote` | `reconstruction` |
| `x86decomp candidate search` | `reconstruction` |
| `x86decomp candidate show` | `governance` |
| `x86decomp candidate transition` | `governance` |

## Verification boundary

This page is source-derived from the current parser. It does not claim that optional adapters, external tools, target inputs, or candidate artifacts exist in your environment.
