---
title: x86decomp campaign
---

# `x86decomp campaign`

Canonical campaign commands implemented by the current capability subsystem.

## Usage

```text
usage: x86decomp campaign [-h] [--project PROJECT] [--actor ACTOR]
                          {branch,create,list,pause,plan,resume,snapshot,start,status,stop} ...
```

## Actions

| Action | Usage |
| --- | --- |
| `branch` | `usage: x86decomp campaign branch [-h] [--parent PARENT] campaign_id name` |
| `create` | `usage: x86decomp campaign create [-h] [--budget-json BUDGET_JSON] [--policy-json POLICY_JSON] goal` |
| `list` | `usage: x86decomp campaign list [-h]` |
| `pause` | `usage: x86decomp campaign pause [-h] campaign_id` |
| `plan` | `usage: x86decomp campaign plan [-h] campaign_id` |
| `resume` | `usage: x86decomp campaign resume [-h] campaign_id` |
| `snapshot` | `usage: x86decomp campaign snapshot [-h] campaign_id` |
| `start` | `usage: x86decomp campaign start [-h] campaign_id` |
| `status` | `usage: x86decomp campaign status [-h] campaign_id` |
| `stop` | `usage: x86decomp campaign stop [-h] campaign_id` |

## Canonical routes

| Route | Owner |
| --- | --- |
| `x86decomp campaign branch` | `governance` |
| `x86decomp campaign create` | `governance` |
| `x86decomp campaign list` | `governance` |
| `x86decomp campaign pause` | `governance` |
| `x86decomp campaign plan` | `governance` |
| `x86decomp campaign resume` | `governance` |
| `x86decomp campaign snapshot` | `governance` |
| `x86decomp campaign start` | `governance` |
| `x86decomp campaign status` | `governance` |
| `x86decomp campaign stop` | `governance` |

## Verification boundary

This page is source-derived from the current parser. It does not claim that optional adapters, external tools, target inputs, or candidate artifacts exist in your environment.
