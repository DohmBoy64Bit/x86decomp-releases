---
title: x86decomp changeset
description: Command reference for `x86decomp changeset`.
---


# `x86decomp changeset`

Canonical changeset commands implemented by the current capability subsystem.

## Usage

```text
usage: x86decomp changeset [-h] [--project PROJECT] [--actor ACTOR]
                           {add-operation,apply,conflicts,create,export,inspect,merge,rebase,show,verify} ...
```

## Arguments

| Argument | Details |
| --- | --- |
| `--project` | default: `'.'`. project root used by the capability implementation (default: current directory) |
| `--actor` | default: `'analyst'`. |

## Actions

| Action | Usage | Canonical owner |
| --- | --- | --- |
| `add-operation` | `usage: x86decomp changeset add-operation [-h] changeset_id operation_json` | `reconstruction` |
| `apply` | `usage: x86decomp changeset apply [-h] path` | `governance` |
| `conflicts` | `usage: x86decomp changeset conflicts [-h] changeset_id` | `reconstruction` |
| `create` | `usage: x86decomp changeset create [-h] [--base-audit-hash BASE_AUDIT_HASH] name` | `reconstruction` |
| `export` | `usage: x86decomp changeset export [-h] [--after-hash AFTER_HASH] output` | `governance` |
| `inspect` | `usage: x86decomp changeset inspect [-h] path` | `governance` |
| `merge` | `usage: x86decomp changeset merge [-h] left_id right_id name` | `reconstruction` |
| `rebase` | `usage: x86decomp changeset rebase [-h] changeset_id new_base_hash` | `reconstruction` |
| `show` | `usage: x86decomp changeset show [-h] changeset_id` | `reconstruction` |
| `verify` | `usage: x86decomp changeset verify [-h] changeset_id` | `reconstruction` |

### `x86decomp changeset add-operation`

```text
usage: x86decomp changeset add-operation [-h] changeset_id operation_json
```

| Argument | Details |
| --- | --- |
| `changeset_id` | required. |
| `operation_json` | required. |

### `x86decomp changeset apply`

```text
usage: x86decomp changeset apply [-h] path
```

| Argument | Details |
| --- | --- |
| `path` | required. |

### `x86decomp changeset conflicts`

```text
usage: x86decomp changeset conflicts [-h] changeset_id
```

| Argument | Details |
| --- | --- |
| `changeset_id` | required. |

### `x86decomp changeset create`

```text
usage: x86decomp changeset create [-h] [--base-audit-hash BASE_AUDIT_HASH]
                                  name
```

| Argument | Details |
| --- | --- |
| `name` | required. |
| `--base-audit-hash` | — |

### `x86decomp changeset export`

```text
usage: x86decomp changeset export [-h] [--after-hash AFTER_HASH] output
```

| Argument | Details |
| --- | --- |
| `output` | required. |
| `--after-hash` | — |

### `x86decomp changeset inspect`

```text
usage: x86decomp changeset inspect [-h] path
```

| Argument | Details |
| --- | --- |
| `path` | required. |

### `x86decomp changeset merge`

```text
usage: x86decomp changeset merge [-h] left_id right_id name
```

| Argument | Details |
| --- | --- |
| `left_id` | required. |
| `right_id` | required. |
| `name` | required. |

### `x86decomp changeset rebase`

```text
usage: x86decomp changeset rebase [-h] changeset_id new_base_hash
```

| Argument | Details |
| --- | --- |
| `changeset_id` | required. |
| `new_base_hash` | required. |

### `x86decomp changeset show`

```text
usage: x86decomp changeset show [-h] changeset_id
```

| Argument | Details |
| --- | --- |
| `changeset_id` | required. |

### `x86decomp changeset verify`

```text
usage: x86decomp changeset verify [-h] changeset_id
```

| Argument | Details |
| --- | --- |
| `changeset_id` | required. |


