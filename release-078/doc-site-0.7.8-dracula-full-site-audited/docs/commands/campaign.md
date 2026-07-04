---
title: x86decomp campaign
description: Exact v0.7.8 parser-derived reference for `x86decomp campaign`.
---


# `x86decomp campaign`

Canonical campaign commands implemented by the current capability subsystem.

## Usage

```text
usage: x86decomp campaign [-h] [--project PROJECT] [--actor ACTOR]
                          {branch,create,list,pause,plan,resume,snapshot,start,status,stop} ...
```

## Arguments

| Argument | Exact parser declaration |
| --- | --- |
| `--project` | default: `'.'` · parser destination: `project`. project root used by the capability implementation (default: current directory) |
| `--actor` | default: `'analyst'` · parser destination: `actor`. No help text declared. |

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

| Argument | Exact parser declaration |
| --- | --- |
| `campaign_id` | required · parser destination: `campaign_id`. No help text declared. |
| `name` | required · parser destination: `name`. No help text declared. |
| `--parent` | parser destination: `parent`. No help text declared. |

### `x86decomp campaign create`

```text
usage: x86decomp campaign create [-h] [--budget-json BUDGET_JSON]
                                 [--policy-json POLICY_JSON]
                                 goal
```

| Argument | Exact parser declaration |
| --- | --- |
| `goal` | required · parser destination: `goal`. No help text declared. |
| `--budget-json` | parser destination: `budget_json`. No help text declared. |
| `--policy-json` | parser destination: `policy_json`. No help text declared. |

### `x86decomp campaign list`

```text
usage: x86decomp campaign list [-h]
```

### `x86decomp campaign pause`

```text
usage: x86decomp campaign pause [-h] campaign_id
```

| Argument | Exact parser declaration |
| --- | --- |
| `campaign_id` | required · parser destination: `campaign_id`. No help text declared. |

### `x86decomp campaign plan`

```text
usage: x86decomp campaign plan [-h] campaign_id
```

| Argument | Exact parser declaration |
| --- | --- |
| `campaign_id` | required · parser destination: `campaign_id`. No help text declared. |

### `x86decomp campaign resume`

```text
usage: x86decomp campaign resume [-h] campaign_id
```

| Argument | Exact parser declaration |
| --- | --- |
| `campaign_id` | required · parser destination: `campaign_id`. No help text declared. |

### `x86decomp campaign snapshot`

```text
usage: x86decomp campaign snapshot [-h] campaign_id
```

| Argument | Exact parser declaration |
| --- | --- |
| `campaign_id` | required · parser destination: `campaign_id`. No help text declared. |

### `x86decomp campaign start`

```text
usage: x86decomp campaign start [-h] campaign_id
```

| Argument | Exact parser declaration |
| --- | --- |
| `campaign_id` | required · parser destination: `campaign_id`. No help text declared. |

### `x86decomp campaign status`

```text
usage: x86decomp campaign status [-h] campaign_id
```

| Argument | Exact parser declaration |
| --- | --- |
| `campaign_id` | required · parser destination: `campaign_id`. No help text declared. |

### `x86decomp campaign stop`

```text
usage: x86decomp campaign stop [-h] campaign_id
```

| Argument | Exact parser declaration |
| --- | --- |
| `campaign_id` | required · parser destination: `campaign_id`. No help text declared. |

## Source basis

| Parser owner | Source file | SHA-256 |
| --- | --- | --- |
| canonical cli | `src/x86decomp/canonical.py` | `9dfc1a2d1ba31559b1a9cd31a0cda1ab1a1e88ffef0a47c4632995f649296166` |
| governance cli | `src/x86decomp/governance/cli.py` | `34d9488f9d07dfded83f5e9191aa7faba7140e8b2d0a2d0da66925851fa090de` |

## Verification boundary

This page is regenerated from the v0.7.8 parser surface. It documents syntax, parser-declared arguments, canonical owners, and source files; it does not claim that optional adapters, target binaries, compiler toolchains, or runtime inputs exist on the reader's machine.
