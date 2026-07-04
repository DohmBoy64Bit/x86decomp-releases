---
title: x86decomp hypothesis
description: Command reference for `x86decomp hypothesis`.
---


# `x86decomp hypothesis`

Canonical hypothesis commands implemented by the current capability subsystem.

## Usage

```text
usage: x86decomp hypothesis [-h] [--project PROJECT] [--actor ACTOR]
                            {create,dependency,evidence,gate,list,show,transition} ...
```

## Arguments

| Argument | Details |
| --- | --- |
| `--project` | default: `'.'`. project root used by the capability implementation (default: current directory) |
| `--actor` | default: `'analyst'`. |

## Actions

| Action | Usage | Canonical owner |
| --- | --- | --- |
| `create` | `usage: x86decomp hypothesis create [-h] --origin ORIGIN statement scope_kind scope_id` | `governance` |
| `dependency` | `usage: x86decomp hypothesis dependency [-h] hypothesis_id depends_on_id` | `governance` |
| `evidence` | `usage: x86decomp hypothesis evidence [-h] --stance STANCE --weight WEIGHT --kind KIND --group GROUP [--artifact-sha256 ARTIFACT_SHA256] [--details-json DETAILS_JSON] hypothesis_id evidence_id` | `governance` |
| `gate` | `usage: x86decomp hypothesis gate [-h] hypothesis_id` | `governance` |
| `list` | `usage: x86decomp hypothesis list [-h] [--state STATE] [--scope-id SCOPE_ID]` | `governance` |
| `show` | `usage: x86decomp hypothesis show [-h] hypothesis_id` | `governance` |
| `transition` | `usage: x86decomp hypothesis transition [-h] --reason REASON [--lock] hypothesis_id state` | `governance` |

### `x86decomp hypothesis create`

```text
usage: x86decomp hypothesis create [-h] --origin ORIGIN
                                   statement scope_kind scope_id
```

| Argument | Details |
| --- | --- |
| `statement` | required. |
| `scope_kind` | required. |
| `scope_id` | required. |
| `--origin` | required. |

### `x86decomp hypothesis dependency`

```text
usage: x86decomp hypothesis dependency [-h] hypothesis_id depends_on_id
```

| Argument | Details |
| --- | --- |
| `hypothesis_id` | required. |
| `depends_on_id` | required. |

### `x86decomp hypothesis evidence`

```text
usage: x86decomp hypothesis evidence [-h] --stance STANCE --weight WEIGHT
                                     --kind KIND --group GROUP
                                     [--artifact-sha256 ARTIFACT_SHA256]
                                     [--details-json DETAILS_JSON]
                                     hypothesis_id evidence_id
```

| Argument | Details |
| --- | --- |
| `hypothesis_id` | required. |
| `evidence_id` | required. |
| `--stance` | required. |
| `--weight` | required · type: `float`. |
| `--kind` | required. |
| `--group` | required · default: `'hypothesis'`. |
| `--artifact-sha256` | — |
| `--details-json` | — |

### `x86decomp hypothesis gate`

```text
usage: x86decomp hypothesis gate [-h] hypothesis_id
```

| Argument | Details |
| --- | --- |
| `hypothesis_id` | required. |

### `x86decomp hypothesis list`

```text
usage: x86decomp hypothesis list [-h] [--state STATE] [--scope-id SCOPE_ID]
```

| Argument | Details |
| --- | --- |
| `--state` | — |
| `--scope-id` | — |

### `x86decomp hypothesis show`

```text
usage: x86decomp hypothesis show [-h] hypothesis_id
```

| Argument | Details |
| --- | --- |
| `hypothesis_id` | required. |

### `x86decomp hypothesis transition`

```text
usage: x86decomp hypothesis transition [-h] --reason REASON [--lock]
                                       hypothesis_id state
```

| Argument | Details |
| --- | --- |
| `hypothesis_id` | required. |
| `state` | required. |
| `--reason` | required. |
| `--lock` | nargs: `0` · default: `False`. |


