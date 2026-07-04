---
title: x86decomp proof
description: Command reference for `x86decomp proof`.
---


# `x86decomp proof`

Canonical proof commands implemented by the current capability subsystem.

## Usage

```text
usage: x86decomp proof [-h] [--project PROJECT] [--actor ACTOR]
                       {evaluate,export,inspect,obligation,result,verify} ...
```

## Arguments

| Argument | Details |
| --- | --- |
| `--project` | default: `'.'`. project root used by the capability implementation (default: current directory) |
| `--actor` | default: `'analyst'`. |

## Actions

| Action | Usage | Canonical owner |
| --- | --- | --- |
| `evaluate` | `usage: x86decomp proof evaluate [-h] obligation_id` | `governance` |
| `export` | `usage: x86decomp proof export [-h] [--include INCLUDE] output` | `governance` |
| `inspect` | `usage: x86decomp proof inspect [-h] path` | `governance` |
| `obligation` | `usage: x86decomp proof obligation [-h] [--assumptions-json ASSUMPTIONS_JSON] scope_kind scope_id property_name required_status` | `governance` |
| `result` | `usage: x86decomp proof result [-h] [--artifact-sha256 ARTIFACT_SHA256] obligation_id status validator report_json` | `governance` |
| `verify` | `usage: x86decomp proof verify [-h] path` | `governance` |

### `x86decomp proof evaluate`

```text
usage: x86decomp proof evaluate [-h] obligation_id
```

| Argument | Details |
| --- | --- |
| `obligation_id` | required. |

### `x86decomp proof export`

```text
usage: x86decomp proof export [-h] [--include INCLUDE] output
```

| Argument | Details |
| --- | --- |
| `output` | required. |
| `--include` | default: `[]`. |

### `x86decomp proof inspect`

```text
usage: x86decomp proof inspect [-h] path
```

| Argument | Details |
| --- | --- |
| `path` | required. |

### `x86decomp proof obligation`

```text
usage: x86decomp proof obligation [-h] [--assumptions-json ASSUMPTIONS_JSON]
                                  scope_kind scope_id property_name
                                  required_status
```

| Argument | Details |
| --- | --- |
| `scope_kind` | required. |
| `scope_id` | required. |
| `property_name` | required. |
| `required_status` | required. |
| `--assumptions-json` | — |

### `x86decomp proof result`

```text
usage: x86decomp proof result [-h] [--artifact-sha256 ARTIFACT_SHA256]
                              obligation_id status validator report_json
```

| Argument | Details |
| --- | --- |
| `obligation_id` | required. |
| `status` | required. |
| `validator` | required. |
| `report_json` | required. |
| `--artifact-sha256` | — |

### `x86decomp proof verify`

```text
usage: x86decomp proof verify [-h] path
```

| Argument | Details |
| --- | --- |
| `path` | required. |


