---
title: x86decomp campaign
description: Command reference for `x86decomp campaign`.
---


# `x86decomp campaign`

Canonical campaign commands implemented by the current capability subsystem.

## Usage

```text
usage: x86decomp campaign [-h] [--project PROJECT] [--actor ACTOR]
                          {branch,create,list,pause,plan,resume,snapshot,start,status,stop} ...
```

## Arguments

| Argument | Details |
| --- | --- |
| `--project` | default: `'.'`. project root used by the capability implementation (default: current directory) |
| `--actor` | default: `'analyst'`. |

## Actions

| Action | Usage | Canonical owner |
| --- | --- | --- |
| `branch` | `usage: x86decomp campaign branch [-h] [--parent PARENT] campaign_id name` | `governance` |
| `create` | `usage: x86decomp campaign create [-h] [--budget-json BUDGET_JSON] [--policy-json POLICY_JSON] goal` | `governance` |
| `list` | `usage: x86decomp campaign list [-h]` | `governance` |
| `pause` | `usage: x86decomp campaign pause [-h] campaign_id` | `governance` |
| `plan` | `usage: x86decomp campaign plan [-h] campaign_id` | `governance` |
| `resume` | `usage: x86decomp campaign resume [-h] campaign_id` | `governance` |
| `snapshot` | `usage: x86decomp campaign snapshot [-h] campaign_id` | `governance` |
| `start` | `usage: x86decomp campaign start [-h] campaign_id` | `governance` |
| `status` | `usage: x86decomp campaign status [-h] campaign_id` | `governance` |
| `stop` | `usage: x86decomp campaign stop [-h] campaign_id` | `governance` |

### `x86decomp campaign branch`

```text
usage: x86decomp campaign branch [-h] [--parent PARENT] campaign_id name
```

| Argument | Details |
| --- | --- |
| `campaign_id` | required. |
| `name` | required. |
| `--parent` | — |

### `x86decomp campaign create`

```text
usage: x86decomp campaign create [-h] [--budget-json BUDGET_JSON]
                                 [--policy-json POLICY_JSON]
                                 goal
```

| Argument | Details |
| --- | --- |
| `goal` | required. |
| `--budget-json` | — |
| `--policy-json` | — |

### `x86decomp campaign list`

```text
usage: x86decomp campaign list [-h]
```

### `x86decomp campaign pause`

```text
usage: x86decomp campaign pause [-h] campaign_id
```

| Argument | Details |
| --- | --- |
| `campaign_id` | required. |

### `x86decomp campaign plan`

```text
usage: x86decomp campaign plan [-h] campaign_id
```

| Argument | Details |
| --- | --- |
| `campaign_id` | required. |

### `x86decomp campaign resume`

```text
usage: x86decomp campaign resume [-h] campaign_id
```

| Argument | Details |
| --- | --- |
| `campaign_id` | required. |

### `x86decomp campaign snapshot`

```text
usage: x86decomp campaign snapshot [-h] campaign_id
```

| Argument | Details |
| --- | --- |
| `campaign_id` | required. |

### `x86decomp campaign start`

```text
usage: x86decomp campaign start [-h] campaign_id
```

| Argument | Details |
| --- | --- |
| `campaign_id` | required. |

### `x86decomp campaign status`

```text
usage: x86decomp campaign status [-h] campaign_id
```

| Argument | Details |
| --- | --- |
| `campaign_id` | required. |

### `x86decomp campaign stop`

```text
usage: x86decomp campaign stop [-h] campaign_id
```

| Argument | Details |
| --- | --- |
| `campaign_id` | required. |


