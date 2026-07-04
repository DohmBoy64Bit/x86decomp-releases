---
title: x86decomp plugin
description: Command reference for `x86decomp plugin`.
---


# `x86decomp plugin`

Canonical plugin commands implemented by the current capability subsystem.

## Usage

```text
usage: x86decomp plugin [-h] [--project PROJECT] [--actor ACTOR]
                        {doctor,install,invoke,list,validate} ...
```

## Arguments

| Argument | Details |
| --- | --- |
| `--project` | default: `'.'`. project root used by the capability implementation (default: current directory) |
| `--actor` | default: `'analyst'`. |

## Actions

| Action | Usage | Canonical owner |
| --- | --- | --- |
| `doctor` | `usage: x86decomp plugin doctor [-h] plugin_id` | `governance` |
| `install` | `usage: x86decomp plugin install [-h] manifest` | `governance` |
| `invoke` | `usage: x86decomp plugin invoke [-h] [--timeout TIMEOUT] plugin_id capability request_json` | `governance` |
| `list` | `usage: x86decomp plugin list [-h]` | `governance` |
| `validate` | `usage: x86decomp plugin validate [-h] manifest` | `governance` |

### `x86decomp plugin doctor`

```text
usage: x86decomp plugin doctor [-h] plugin_id
```

| Argument | Details |
| --- | --- |
| `plugin_id` | required. |

### `x86decomp plugin install`

```text
usage: x86decomp plugin install [-h] manifest
```

| Argument | Details |
| --- | --- |
| `manifest` | required. |

### `x86decomp plugin invoke`

```text
usage: x86decomp plugin invoke [-h] [--timeout TIMEOUT]
                               plugin_id capability request_json
```

| Argument | Details |
| --- | --- |
| `plugin_id` | required. |
| `capability` | required. |
| `request_json` | required. |
| `--timeout` | type: `int` · default: `60`. |

### `x86decomp plugin list`

```text
usage: x86decomp plugin list [-h]
```

### `x86decomp plugin validate`

```text
usage: x86decomp plugin validate [-h] manifest
```

| Argument | Details |
| --- | --- |
| `manifest` | required. |


