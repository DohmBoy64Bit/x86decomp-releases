---
title: x86decomp worker
description: Command reference for `x86decomp worker`.
---


# `x86decomp worker`

Canonical worker commands implemented by the current capability subsystem.

## Usage

```text
usage: x86decomp worker [-h] [--project PROJECT] [--actor ACTOR]
                        {doctor,list,register,select,status} ...
```

## Arguments

| Argument | Details |
| --- | --- |
| `--project` | default: `'.'`. project root used by the capability implementation (default: current directory) |
| `--actor` | default: `'analyst'`. |

## Actions

| Action | Usage | Canonical owner |
| --- | --- | --- |
| `doctor` | `usage: x86decomp worker doctor [-h] worker_id` | `governance` |
| `list` | `usage: x86decomp worker list [-h] [--status STATUS]` | `governance` |
| `register` | `usage: x86decomp worker register [-h] [--endpoint ENDPOINT] [--environment-sha256 ENVIRONMENT_SHA256] name capabilities_json` | `governance` |
| `select` | `usage: x86decomp worker select [-h] required_json` | `governance` |
| `status` | `usage: x86decomp worker status [-h] worker_id status` | `governance` |

### `x86decomp worker doctor`

```text
usage: x86decomp worker doctor [-h] worker_id
```

| Argument | Details |
| --- | --- |
| `worker_id` | required. |

### `x86decomp worker list`

```text
usage: x86decomp worker list [-h] [--status STATUS]
```

| Argument | Details |
| --- | --- |
| `--status` | — |

### `x86decomp worker register`

```text
usage: x86decomp worker register [-h] [--endpoint ENDPOINT]
                                 [--environment-sha256 ENVIRONMENT_SHA256]
                                 name capabilities_json
```

| Argument | Details |
| --- | --- |
| `name` | required. |
| `capabilities_json` | required. |
| `--endpoint` | — |
| `--environment-sha256` | — |

### `x86decomp worker select`

```text
usage: x86decomp worker select [-h] required_json
```

| Argument | Details |
| --- | --- |
| `required_json` | required. |

### `x86decomp worker status`

```text
usage: x86decomp worker status [-h] worker_id status
```

| Argument | Details |
| --- | --- |
| `worker_id` | required. |
| `status` | required. |


